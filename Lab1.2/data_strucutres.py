from random import randint
from typing import Any

type HashTableElementReturn = str | int | tuple | float


class HashTableElement:
    def __init__(self, key, value) -> None:
        self.key = key
        self.__key_hash: int = hash(self.key)
        self.__value = value

    @property
    def key(self) -> HashTableElementReturn:
        return self.__key

    @key.setter
    def key(self, new_key) -> None:
        if isinstance(new_key, (dict, list, set)):
            raise TypeError("Key must be unchangeable type")

        self.__key = new_key

    @property
    def key_hash(self) -> int:
        return self.__key_hash

    @property
    def value(self) -> Any:
        return self.__value

    def __repr__(self) -> str:
        return f"HashTableElement({self.__key!r}, {self.__value!r})"


class HashTable:
    def __init__(self, size) -> None:
        self.__size = size
        self.__table: list[HashTableElement | None] = [None] * size

    def __choice_rnd_place(self) -> int:
        while True:
            idx = randint(0, self.__size - 1)
            if self.__table[idx] is None:
                return idx

    def __setitem__(self, key, value) -> None:
        key_hash = hash(key)
        for idx, element in enumerate(self.__table):
            if isinstance(element, HashTableElement) and element.key_hash == key_hash:
                self.__table[idx] = HashTableElement(key, value)
                return

        idx = self.__choice_rnd_place()
        self.__table[idx] = HashTableElement(key, value)

    def __getitem__(self, key) -> HashTableElementReturn:
        key_hash = hash(key)
        for element in self.__table:
            if isinstance(element, HashTableElement) and element.key_hash == key_hash:
                return element.value
        raise KeyError

    def __delitem__(self, key) -> None:
        key_hash = hash(key)
        for idx, element in enumerate(self.__table):
            if isinstance(element, HashTableElement) and element.key_hash == key_hash:
                self.__table[idx] = None
                return
        raise KeyError

    def __contains__(self, key) -> bool:
        key_hash = hash(key)
        for element in self.__table:
            if isinstance(element, HashTableElement) and element.key_hash == key_hash:
                return True
        return False

    def __len__(self) -> int:
        counter = 0
        for element in self.__table:
            if isinstance(element, HashTableElement):
                counter += 1
        return counter

    def items(self):
        for element in self.__table:
            if isinstance(element, HashTableElement):
                yield (element.key, element.value)

    def __iter__(self):
        for key, _ in self.items():
            yield key

    def __repr__(self):
        pairs = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"HashTable({{{pairs}}})"
