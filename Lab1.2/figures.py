from random import randint


class Figure:
    def __init__(self) -> None:
        self.A: tuple = (randint(1, 20), randint(1, 20))
        self.B: tuple = (randint(1, 20), randint(1, 20))


class ParalleloGram(Figure):
    def __init__(self) -> None:
        super().__init__()
        self.C: tuple = (randint(1, 20), randint(1, 20))
        self.D: tuple = (randint(1, 20), randint(1, 20))

        if not self.__is_paralleloGram():
            raise ValueError("Wrong parallelogram was generated")
        self.__calculate_sides()

    def calc_perimeter(self) -> float:
        return round(self.A_SIDE + self.B_SIDE + self.C_SIDE + self.D_SIDE, 2)

    def calc_area(self) -> float:
        y1 = self.A[1]
        y2 = self.B[1]
        return round(self.D_SIDE * abs(y2 - y1), 2)

    def __repr__(self) -> str:
        return f"""ParalleloGram(A={self.A}, B={self.B}, C={self.C}, D={self.D})
Sides: A={self.A_SIDE}, B={self.B_SIDE}, C={self.C_SIDE}, D={self.D_SIDE}
Perimeter: {self.calc_perimeter()}
Area: {self.calc_area()}\n"""

    def __calculate_sides(self) -> None:
        x1, y1 = self.A
        x2, y2 = self.B
        x3, y3 = self.C
        x4, y4 = self.D

        self.A_SIDE: int = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        self.B_SIDE: int = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.C_SIDE: int = ((x2 - x4) ** 2 + (y2 - y4) ** 2) ** 0.5
        self.D_SIDE: int = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5

    def __is_paralleloGram(self) -> bool:
        print(f"Generated figure: A={self.A}, B={self.B}, C={self.C}, D={self.D}")
        if self.A[0] == self.B[0] or self.A[1] == self.B[1]:
            return True
        if self.C[0] == self.D[0] or self.C[1] == self.D[1]:
            return True
        if self.A[0] == self.C[0] or self.A[1] == self.C[1]:
            return True
        if self.B[0] == self.D[0] or self.B[1] == self.D[1]:
            return True
        return False
