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
        self._root: None | StudentNode = None

    def insert(self, value: Student):
        if self._root is None:
            self._root = StudentNode(value)
        else:
            self._insert_recursive(self._root, value)

    def _insert_recursive(self, current_node: StudentNode, value: Student):
        if value.surname < current_node.value.surname:
            if current_node.left is None:
                current_node.left = StudentNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = StudentNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, surname: str) -> Optional[Student]:
        return self._search_recursive(self._root, surname)

    def _search_recursive(
        self, current_node: None | StudentNode, surname: str
    ) -> Optional[Student]:
        if current_node is None:
            return None
        if current_node.value.surname == surname:
            return current_node.value

        if surname < current_node.value.surname:
            return self._search_recursive(current_node.left, surname)
        else:
            return self._search_recursive(current_node.right, surname)

    def rotate_left(self, rotate_node: StudentNode | None = None):
        if rotate_node is None or rotate_node.right is None:
            rotate_node = self._root

        if rotate_node is None or rotate_node.right is None:
            return rotate_node

        old_root = rotate_node
        new_root = old_root.right

        if not new_root or not new_root.left:
            return rotate_node

        t2_subtree = new_root.left

        new_root.left = old_root
        old_root.right = t2_subtree

        return new_root

    def rotate_right(self, rotate_node: StudentNode | None = None):
        if rotate_node is None or rotate_node.left is None:
            rotate_node = self._root

        if rotate_node is None or rotate_node.left is None:
            return rotate_node

        old_root = rotate_node
        new_root = old_root.left

        if not new_root or not new_root.right:
            return rotate_node

        t2_subtree = new_root.right

        new_root.right = old_root
        old_root.left = t2_subtree

        return new_root

    @classmethod
    def display_beautiful_tree(cls, node: None | StudentNode, prefix="", is_left=True):
        if node is None:
            return

        cls.display_beautiful_tree(
            node.right, prefix + ("│   " if is_left else "    "), is_left=False
        )

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value.surname))

        cls.display_beautiful_tree(
            node.left, prefix + ("    " if is_left else "│   "), is_left=True
        )

    @property
    def root(self) -> None | StudentNode:
        return self._root

    @root.setter
    def root(self, value: None | StudentNode):
        if value is not None and not isinstance(value, StudentNode):
            raise TypeError("Root must be a StudentNode or None")
        self._root = value


class StudentTreeBalanced(StudentBinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value: Student):
        self._root = self._insert_recursive(self._root, value)

    def _insert_recursive(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, current_node: StudentNode | None, value: Student
    ) -> StudentNode | None:
        if current_node is None:
            return StudentNode(value)

        if value.surname < current_node.value.surname:
            current_node.left = self._insert_recursive(current_node.left, value)
        else:
            current_node.right = self._insert_recursive(current_node.right, value)

        return self.__balance(current_node)

    @classmethod
    def display_beautiful_tree(cls, node: None | StudentNode, prefix="", is_left=True):
        if node is None:
            return

        cls.display_beautiful_tree(
            node.right, prefix + ("│   " if is_left else "    "), is_left=False
        )

        print(
            prefix
            + ("└── " if is_left else "┌── ")
            + str(node.value.surname)
            + f" (ID: {node.value.id})"
        )

        cls.display_beautiful_tree(
            node.left, prefix + ("    " if is_left else "│   "), is_left=True
        )

    def __balance(self, node: StudentNode) -> StudentNode | None:
        if node is None:
            return node
        node_id = node.value.id
        max_id = node_id
        what_rotate = "0"

        if node.left is not None and max_id < node.left.value.id:
            max_id = node.left.value.id
            what_rotate = "r"

        if node.right is not None and max_id < node.right.value.id:
            max_id = node.right.value.id
            what_rotate = "l"

        if what_rotate == "r":
            return self.rotate_right(node)
        elif what_rotate == "l":
            return self.rotate_left(node)
        return node
