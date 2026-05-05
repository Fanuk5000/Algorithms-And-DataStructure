class Student:
    def __init__(self, name, surname, faculty, skipped_hours=0) -> None:
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.skipped_hours = skipped_hours

    def __str__(self) -> str:
        return f"Name: {self.name}, Surname: {self.surname}, Faculty: {self.faculty}, Lessons Skipped: {self.skipped_hours}"


class StudentArray:
    def __init__(self) -> None:
        self.__students: list[Student] = []
        self.__was_sorted = False

    def add_student(self, new_student) -> None:
        if not isinstance(new_student, Student):
            raise TypeError("Only instances of Student can be added")
        for existing_student in self.__students:
            if existing_student.skipped_hours == new_student.skipped_hours:
                raise ValueError(
                    "Student with the skipped hours already exists in the array"
                )
        self.__students.append(new_student)

    def sort_students_by_skipped_lessons(self) -> None:
        self.__students.sort(key=lambda student: student.skipped_hours)
        self.__was_sorted = True

    def binary_search(self, skipped_hours) -> Student | None:
        if not self.__was_sorted:
            raise ValueError("Array must be sorted before performing binary search")
        left, right = 0, len(self.__students) - 1

        while left <= right:
            middle = (left + right) // 2

            mid_skipped_hours = self.__students[middle].skipped_hours
            if mid_skipped_hours == skipped_hours:
                return self.__students[middle]
            elif skipped_hours > mid_skipped_hours:
                left = middle + 1
            elif skipped_hours < mid_skipped_hours:
                right = middle - 1
        return None

    def get_all_students_info(self) -> list[str]:
        return [str(student) for student in self.__students]
