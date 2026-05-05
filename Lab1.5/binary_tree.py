from typing import Optional

from student import Student


class StudentNode:
    def __init__(self, value: Student):
        if not isinstance(value, Student):
            raise TypeError("Value must be an instance of Student")

        self.value = value
        self.left: Optional["StudentNode"] = None
        self.right: Optional["StudentNode"] = None


class StudentBinaryTree:
    def __init__(self):
        self.__root: Optional["StudentNode"] = None

    def insert(self, value: Student):
        if self.__root is None:
            self.__root = StudentNode(value)
        else:
            self.__insert_recursive(self.__root, value)

    def __insert_recursive(self, current_node: StudentNode, value: Student):
        if value.surname < current_node.value.surname:
            if current_node.left is None:
                current_node.left = StudentNode(value)
            else:
                self.__insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = StudentNode(value)
            else:
                self.__insert_recursive(current_node.right, value)

    def search(self, surname: str) -> Optional[Student]:
        return self.__search_recursive(self.__root, surname)

    def __search_recursive(
        self, current_node: Optional[StudentNode], surname: str
    ) -> Optional[Student]:
        if current_node is None:
            return None
        if current_node.value.surname == surname:
            return current_node.value

        if surname < current_node.value.surname:
            return self.__search_recursive(current_node.left, surname)
        else:
            return self.__search_recursive(current_node.right, surname)

    def rotate_left(self):
        if self.__root is None or self.__root.right is None:
            return

        old_root = self.__root
        new_root = old_root.right

        t2_subtree = new_root.left

        new_root.left = old_root
        old_root.right = t2_subtree

        self.__root = new_root

    def rotate_right(self):
        if self.__root is None or self.__root.left is None:
            return

        old_root = self.__root
        new_root = old_root.left

        t2_subtree = new_root.right

        new_root.right = old_root
        old_root.left = t2_subtree

        self.__root = new_root
