import re


class LUPSolver:
    def __init__(self, equations):
        self.__matrix_len = len(equations)
        self.__L: list[list[float]] = [
            [0] * self.__matrix_len for _ in range(self.__matrix_len)
        ]

        self.__matrix, self.__constants = self.__equation_to_matrix(equations)

        self.__set_1_for_L()
        change_row: int = self.__move_high_to_up()

        self.__P: list[int] = list(range(self.__matrix_len))

        if change_row:
            self.__P[0], self.__P[change_row] = self.__P[change_row], self.__P[0]

    def __set_1_for_L(self) -> None:
        for row_idx in range(self.__matrix_len):
            for col_idx in range(self.__matrix_len):
                if row_idx == col_idx:
                    self.__L[row_idx][col_idx] = 1

    def __equation_to_matrix(
        self, equations: list[str]
    ) -> tuple[list[list[float]], list[float]]:
        matrix: list[list[float]] = [[], [], [], []]
        constants: list[float] = []

        row = 0
        for equation in equations:
            # Extract coefficients and constant term
            eq = equation.replace(" ", "")  # remove spaces so "- z" -> "-z"
            matches = re.findall(r"([+-]?\d*)([a-zA-Z])", eq)
            constant_match = re.search(r"=([+-]?\d+)", eq)

            if constant_match:
                constant = int(constant_match.group(1))
            else:
                raise ValueError(
                    f"Equation '{equation}' does not contain a valid constant term."
                )

            coeffs = {"x": 0, "y": 0, "z": 0, "w": 0}
            for coeff, var in matches:
                if coeff == "" or coeff == "+":
                    coeffs[var] += 1
                elif coeff == "-":
                    coeffs[var] -= 1
                else:
                    coeffs[var] += int(coeff)

            matrix[row] = [coeffs["x"], coeffs["y"], coeffs["z"], coeffs["w"]]
            constants.append(constant)
            row += 1

        return matrix, constants

    def __move_high_to_up(self) -> int:
        max_row: list[float] = max(self.__matrix, key=lambda x: x[0])
        first_row = self.__matrix[0]
        if first_row[0] < max_row[0]:
            for candidate_row in range(self.__matrix_len):
                if self.__matrix[candidate_row] == max_row:
                    self.__matrix[candidate_row] = first_row
                    self.__matrix[0] = max_row
                    return candidate_row
        return 0

    def decompose(self) -> None:
        for pivot_idx in range(self.__matrix_len):
            pivot = self.__matrix[pivot_idx][pivot_idx]
            if abs(pivot) < 1e-12:
                raise ValueError("Zero or nearly-zero pivot")
            for row_idx in range(pivot_idx + 1, self.__matrix_len):
                coef = self.__matrix[row_idx][pivot_idx] / pivot
                self.__L[row_idx][pivot_idx] = coef
                for col_idx in range(pivot_idx, self.__matrix_len):
                    self.__matrix[row_idx][col_idx] -= (
                        coef * self.__matrix[pivot_idx][col_idx]
                    )
                    self.__matrix[row_idx][pivot_idx] = 0.0

    def calculate_solution(self) -> list[float]:
        # Apply permutation to constants: Pb
        y = [float(self.__constants[self.__P[i]]) for i in range(self.__matrix_len)]

        # Forward substitution: solve L * y = P * b
        for column in range(1, self.__matrix_len):
            y[column] -= sum(self.__L[column][row] * y[row] for row in range(column))

        # Backward substitution: solve U * x = y
        x: list[float] = [0.0] * self.__matrix_len
        for i in range(self.__matrix_len - 1, -1, -1):
            s = y[i] - sum(
                self.__matrix[i][j] * x[j] for j in range(i + 1, self.__matrix_len)
            )
            x[i] = s / self.__matrix[i][i]

        # Round results: prefer ints when value is very close to an integer
        def _round_val(v: float):
            rv = round(v, 12)
            return int(round(rv)) if abs(rv - round(rv)) < 1e-9 else rv

        return [_round_val(v) for v in x]

    def get_matrix(self) -> list[list[float]]:
        return self.__matrix

    def get_Lower_triangle(self) -> list[list[float]]:
        return self.__L
