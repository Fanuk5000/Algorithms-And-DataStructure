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
        for i in range(self.__matrix_len):
            for j in range(self.__matrix_len):
                if i == j:
                    self.__L[i][j] = 1

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
            for row in range(self.__matrix_len):
                if self.__matrix[row] == max_row:
                    self.__matrix[row] = first_row
                    self.__matrix[0] = max_row
                    return row
        return 0

    def decompose(self) -> None:
        mat_len = self.__matrix_len
        for column in range(mat_len):
            pivot = self.__matrix[column][column]
            for row in range(column + 1, mat_len):
                coef = self.__matrix[row][column] / pivot
                self.__L[row][column] = coef
                self.__matrix[row][column] = 0.0
                for j in range(column + 1, mat_len):
                    self.__matrix[row][j] -= coef * self.__matrix[column][j]

    def calculate_solution(self) -> list[float]:
        y = [0.0] * self.__matrix_len
        for i in range(self.__matrix_len):
            y[i] = self.__constants[self.__P[i]]
        for row in range(self.__matrix_len):
            for column in range(row):
                y[row] -= self.__L[row][column] * y[column]  # y[column] is previous y
        return y

    def get_matrix(self) -> list[list[float]]:
        return self.__matrix

    def get_Lower_triangle(self) -> list[list[float]]:
        return self.__L
