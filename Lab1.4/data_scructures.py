from collections import deque

from student import Student


class StudentDeque:
    def __init__(self, data: deque[Student] | None = None) -> None:
        self.__data: deque[Student] = data if data is not None else deque()

    def is_empty(self) -> bool:
        return len(self.__data) == 0

    def insert_back(self, value: Student) -> None:
        self.__data.append(value)

    def insert_front(self, value: Student) -> None:
        self.__data.appendleft(value)

    def delete_back(self) -> Student:
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.__data.pop()

    def delete_front(self) -> Student:
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.__data.popleft()

    def copy(self, max_size: int | None = None) -> "StudentDeque":
        return StudentDeque(data=self.__data.copy())

    def shake_sort_by_avg_mark(self) -> None:
        n = len(self.__data)
        if n < 2:
            return
        left = 0
        right = n - 1

        for item in self.__data:
            if not isinstance(item, Student):
                raise TypeError("To sort by avg mark all objects must be Student")

        while left < right:
            swapped = False

            # Forward pass: bubble largest to the right end
            for i in range(left, right):
                student1 = self.__data[i]
                student2 = self.__data[i + 1]

                if student1.average_mark < student2.average_mark:
                    self.__data[i], self.__data[i + 1] = student2, student1
                    swapped = True

            right -= 1
            if not swapped:  # already sorted
                break

            swapped = False

            # Backward pass: bubble smallest to the left end
            for i in range(right, left, -1):
                student1 = self.__data[i - 1]
                student2 = self.__data[i]

                if student1.average_mark < student2.average_mark:
                    self.__data[i - 1], self.__data[i] = student2, student1
                    swapped = True

            left += 1

    def pyramid_sort_by_avg_mark(self) -> None:
        n = len(self.__data)
        if n < 2:
            return

        arr = list(self.__data)

        for item in arr:
            if not isinstance(item, Student):
                raise TypeError("To sort by avg mark all objects must be Student")

        def _sift_down(start: int, end: int) -> None:
            root = start
            while True:
                child = 2 * root + 1
                if child > end:  # no leafs
                    return
                swap = root
                if (
                    arr[swap].average_mark < arr[child].average_mark
                ):  # left child is greater
                    swap = child

                if child + 1 <= end and (
                    arr[swap].average_mark < arr[child + 1].average_mark
                ):  # right child is greater
                    swap = child + 1

                if swap == root:  # already in correct position
                    return
                arr[root], arr[swap] = arr[swap], arr[root]
                root = swap

        # Build max-heap
        for start in range((n - 2) // 2, -1, -1):
            _sift_down(start, n - 1)

        # Heap sort (results in ascending order), then reverse for descending
        for end in range(n - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            _sift_down(0, end - 1)

        arr.reverse()
        self.__data = deque(arr)

    def get_data(self) -> list[Student]:
        return list(self.__data)

    def __str__(self) -> str:
        return f"StudentDeque(data={list(self.__data)})"
