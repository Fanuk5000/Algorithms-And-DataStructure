from collections import deque


class IntList:
    def __init__(self, max_size: int, data: list[int] | None = None) -> None:
        self.data: list[int] = data if data is not None else []
        self.max_size = max_size

    def is_full(self) -> bool:
        return len(self.data) >= self.max_size

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def insert(self, value: int) -> int:
        if self.is_full():
            raise ValueError("List is full")

        self.data.append(value)
        return value

    def delete(self, value: int | None = None) -> int | None:
        if self.is_empty():
            raise ValueError("List is empty")

        if value is None:
            return self.data.pop()

        if value in self.data:
            return self.data.pop(self.data.index(value))

    def copy(self, max_size: int | None = None) -> "IntList":
        local_max_size = max_size if max_size is not None else self.max_size
        return IntList(max_size=local_max_size, data=self.data.copy())


class StringDeque:
    def __init__(self, max_size: int, data: deque[str] | None = None) -> None:
        self.data: deque[str] = data if data is not None else deque()
        self.max_size = max_size

    def is_full(self) -> bool:
        return len(self.data) >= self.max_size

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def insert_back(self, value: str) -> str:
        if self.is_full():
            raise ValueError("Deque is full")

        self.data.append(value)
        return value

    def insert_front(self, value: str) -> str:
        if self.is_full():
            raise ValueError("Deque is full")

        self.data.appendleft(value)
        return value

    def delete_back(self) -> str:
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.data.pop()

    def delete_front(self) -> str:
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self.data.popleft()

    def copy(self, max_size: int | None = None) -> "StringDeque":
        local_max_size = max_size if max_size is not None else self.max_size

        return StringDeque(max_size=local_max_size, data=self.data.copy())

    def sort(self, reverse: bool = False) -> None:
        self.data = deque(sorted(self.data, reverse=reverse))
