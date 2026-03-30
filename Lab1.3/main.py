from data_structures import StudentsBinaryTree
from student import Gender, Student

STUDENTS = (
    Student(
        name="John",
        surname="Smith",
        course=2,
        gender=Gender.MALE,
        residence="New York",
    ),
    Student(
        name="Jane", surname="Doe", course=5, gender=Gender.FEMALE, residence="Kyiv"
    ),
    Student(
        name="Charlie",
        surname="Brown",
        course=3,
        gender=Gender.MALE,
        residence="Los Angeles",
    ),
    Student(
        name="Michael",
        surname="Davis",
        course=1,
        gender=Gender.MALE,
        residence="Chicago",
    ),
    Student(
        name="Emily",
        surname="Johnson",
        course=5,
        gender=Gender.FEMALE,
        residence="Kyiv",
    ),
)


def first_task() -> None:
    # Виконати такі дії:
    # – описати студента згідно з варіантом завдання (дод. 3, табл.
    # Д3.1, «Поля класу «Студент»»);
    # – описати бінарне дерево;
    # – створити екземпляр бінарного дерева;
    # – додати елементи до дерева;
    # – вивести вміст дерева у табличному вигляді згідно з заданим
    # способом обходу дерева (дод. 3, табл. Д3.1, «Обхід дерева»).
    print("------------------------ First task ------------------------")
    tree = StudentsBinaryTree()

    for student in STUDENTS:
        tree.insert(student)
    tree.display_beautiful_tree(tree.root)
    print(*tree.levelOrder(), sep="\n")


def second_task() -> None:
    # Виконати такі дії:
    # – додати до опису бінарного дерева метод, який шукає у дереві вузол за визначеним у варіанті завдання критерієм пошуку
    # (дод. 3, табл. Д3.2);
    # – створити екземпляр бінарного дерева;
    # – додати елементи до дерева;
    # – вивести вміст дерева у табличному вигляді згідно з заданим
    # способом обходу дерева (дод. 3, табл. Д3.1, «Обхід дерева»);
    # – знайти та вивести вузли дерева за визначеним критерієм
    # пошуку.
    print("\n------------------------ Second task ------------------------")
    tree = StudentsBinaryTree()

    for student in STUDENTS:
        tree.insert(student)
    tree.display_beautiful_tree(tree.root)
    print(*tree.levelOrder(), sep="\n")
    print("5th course students who leave in Kyiv:\n")
    print(*tree.find_5_kyiv_course(), sep="\n")


def third_task() -> None:
    # Виконати такі дії:
    # – додати до опису бінарного дерева метод, який видаляє з дерева вузли, що відповідають визначеному у варіанті завдання критерію пошуку (дод. 3, табл. Д3.2);
    # – створити екземпляр бінарного дерева;
    # – додати елементи до дерева;
    # – вивести вміст дерева у табличному вигляді згідно з заданим
    # способом обходу дерева (дод. 3, табл. Д3.1, «Обхід дерева»);
    # 11
    # – знайти та видалити вузли дерева за визначеним критерієм
    # пошуку;
    # – вивести вміст дерева в табличному вигляді.
    print("\n------------------------ Third task ------------------------")
    tree = StudentsBinaryTree()

    for student in STUDENTS:
        tree.insert(student)

    tree.display_beautiful_tree(tree.root)
    print(*tree.levelOrder(), sep="\n")
    tree.del_5_course_kyiv()
    print()
    print(*tree.levelOrder(), sep="\n")


if __name__ == "__main__":
    first_task()
    second_task()
    third_task()
