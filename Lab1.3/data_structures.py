from collections import deque
from typing import Callable, Iterator

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

    def filter_students(self, predicate: Callable[[Student], bool]) -> list[Student]:
        return [n.data for n in self.__bfs_nodes() if predicate(n.data)]

    def del_5_course_kyiv(self) -> None:
        kept_data = [
            s
            for s in self.filter_students(
                lambda s: s.course != 5 and s.residence.lower() != "kyiv"
            )
        ]
        self.root = None
        for tree_data in kept_data:
            self.insert(tree_data)

    def find_5_kyiv_course(self) -> list[Student]:
        return self.filter_students(
            lambda s: s.course == 5 and s.residence.lower() == "kyiv"
        )

    def levelOrder(self) -> list[Student]:
        return [node.data for node in self.__bfs_nodes()]

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

    def __bfs_nodes(self) -> Iterator[Node]:
        if self.root is None:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
