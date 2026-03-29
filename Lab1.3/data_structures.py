from collections import deque

from student import Student


class Node:
    def __init__(self, data: Student):
        self.data: Student = data
        self.left: None | Node = None
        self.right: None | Node = None


class StudentsBinaryTree:
    def __init__(self) -> None:
        self.root: None | Node = None

    def insert(self, data: Student) -> None:
        if not isinstance(data, Student):
            raise TypeError("Wrong type must be a Student")

        if not self.root:
            self.root = Node(data)
        else:
            self.__recursive_insert(self.root, data)

    def display_beautiful_tree(self, node: None | Node, prefix="", is_left=True):
        if node is None:
            return

        self.display_beautiful_tree(
            node.right, prefix + ("│   " if is_left else "    "), is_left=False
        )

        print(prefix + ("└── " if is_left else "┌── ") + str(node.data.name))

        self.display_beautiful_tree(
            node.left, prefix + ("    " if is_left else "│   "), is_left=True
        )

    def show_levelOrder(self, root) -> list[str]:
        tree_data = []
        if root is None:
            return tree_data

        queue = deque([root])

        while queue:
            node: Node = queue.popleft()
            tree_data.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return tree_data

    def __recursive_insert(self, node: Node, data: Student) -> None:
        if data.student_id == node.data.student_id:
            return

        if data.student_id < node.data.student_id:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__recursive_insert(node.left, data)
        elif data.student_id > node.data.student_id:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__recursive_insert(node.right, data)
