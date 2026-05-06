from student import Student

STUDENTS = [
    Student("John", "Doe", "Engineering", 50),
    Student("Jane", "Smith", "Medicine", 30),
    Student("Bob", "Johnson", "Business", 70),
    Student("Alice", "Williams", "Law", 20),
    Student("Charlie", "Brown", "Arts", 40),
    Student("Eve", "Davis", "Science", 60),
    Student("Frank", "Miller", "Education", 10),
    Student("Grace", "Wilson", "Architecture"),
    Student("Hank", "Moore", "Philosophy", 80),
    Student("Ivy", "Taylor", "Psychology", 90),
    Student("Jack", "Anderson", "Sociology", 15),
    Student("Karen", "Thomas", "History", 25),
    Student("Leo", "Jackson", "Mathematics", 100),
    Student("Mia", "White", "Physics", 5),
    Student("Nina", "Harris", "Chemistry", 35),
    Student("Oscar", "Martin", "Biology", 45),
    Student("Paul", "Thompson", "Computer Science", 55),
    Student("Quinn", "Garcia", "Economics", 65),
    Student("Rachel", "Martinez", "Political Science", 75),
    Student("Sam", "Robinson", "Literature", 85),
    Student("Magnus", "Parker", "Literature", 85),
]


def first_task() -> None:
    from student import StudentArray

    print("-" * 50 + f"{first_task.__name__.capitalize()}" + "-" * 50)

    student_array = StudentArray()
    for student in STUDENTS:
        try:
            student_array.add_student(student)
        except ValueError as e:
            print(f"Error adding student {student.name} {student.surname}: {e}")

    print()
    student_array.sort_students_by_skipped_lessons()
    for info in student_array.get_all_students_info():
        print(info)
    student = student_array.binary_search(skipped_hours=100)

    if student:
        print("\nStudent found with 100 skipped hours: ", student)
    else:
        print("\nStudent with 100 skipped hours not found")


def second_task() -> None:
    from binary_tree import StudentBinaryTree

    print()
    print("-" * 50 + f"{second_task.__name__.capitalize()}" + "-" * 50)
    student_tree = StudentBinaryTree()

    for student in STUDENTS[:6]:
        student_tree.insert(student)

    johnson = student_tree.search("Johnson")

    if johnson is None:
        print("Student with surname 'Johnson' not found")
    else:
        print(f"Student with surname 'Johnson' found: {johnson}")

    print("\nOriginal tree:")
    student_tree.display_beautiful_tree(student_tree.root)

    student_tree.root = student_tree.rotate_left()
    print("\nTree after left rotation:")
    student_tree.display_beautiful_tree(student_tree.root)

    student_tree.root = student_tree.rotate_right()
    print("\nTree after right rotation:")
    student_tree.display_beautiful_tree(student_tree.root)


def third_task() -> None:
    from binary_tree import StudentTreeBalanced

    print()
    print("-" * 50 + f"{third_task.__name__.capitalize()}" + "-" * 50)
    balanced_tree = StudentTreeBalanced()

    for student in STUDENTS[:6]:
        balanced_tree.insert(student)

    print("\nBalanced tree:")
    balanced_tree.display_beautiful_tree(balanced_tree.root)


if __name__ == "__main__":
    first_task()
    second_task()
    third_task()
