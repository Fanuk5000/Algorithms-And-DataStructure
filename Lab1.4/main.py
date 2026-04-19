from collections import deque

from data_scructures import StudentDeque
from student import Student

STUDENTS = (
    Student(name="John", surname="Smith", average_mark=85.5, group="A"),
    Student(name="Jane", surname="Doe", average_mark=92.0, group="B"),
    Student(name="Charlie", surname="Brown", average_mark=78.0, group="A"),
    Student(name="Michael", surname="Davis", average_mark=88.5, group="C"),
    Student(name="Emily", surname="Johnson", average_mark=91.0, group="B"),
    Student(name="David", surname="Wilson", average_mark=80.0, group="C"),
    Student(name="Sarah", surname="Miller", average_mark=89.5, group="A"),
)


def first_task() -> None:
    # - описати студента згідно з варіантом завдання (дод. 4, табл.
    # Д4.1, «Поля класу «Студент»»);
    # - описати метод, який сортує одновимірний масив студентів
    # за заданим алгоритмом у заданій послідовності сортування згідно з
    # варіантом завдання (дод. 4, табл. Д4.1, «Алгоритм сортування»,
    # «Порядок сортування»);
    # - створити та ініціювати екземпляр лінійної структури даних
    # (одновимірний масив студентів);
    # - вивести вміст одновимірного масиву перед сортуванням;
    # - сортувати одновимірний масив;
    # - вивести вміст одновимірного масиву після сортування.
    print("------------------------ First task ------------------------")
    student_double_arr = StudentDeque(deque([student for student in STUDENTS]))
    students = student_double_arr.get_data()

    for student in students:
        print(student.get_info())
    print("Sorting...")
    student_double_arr.shake_sort_by_avg_mark()
    students = student_double_arr.get_data()

    for student in students:
        print(student.get_info())


def second_task() -> None:
    first_task()


def third_task() -> None:
    # - описати метод, який сортує одновимірний масив студентів
    # за заданим алгоритмом у заданій послідовності сортування згідно з
    # варіантом завдання (дод. 4, табл. Д4.3);
    # - вивести вміст структури даних до сортування;
    # - сортувати структуру даних;
    # - вивести вміст структури даних після сортування.
    print("------------------------ Third task ------------------------")
    student_double_arr = StudentDeque(deque([student for student in STUDENTS]))
    students = student_double_arr.get_data()

    for student in students:
        print(student.get_info())
    print("Sorting...")
    student_double_arr.pyramid_sort_by_avg_mark()
    students = student_double_arr.get_data()

    for student in students:
        print(student.get_info())


if __name__ == "__main__":
    first_task()
    second_task()
    third_task()
