from typing import Any, Generator

from figures import Figure, ParalleloGram

type HashTableElementReturn = str | int | tuple | float | Figure


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
        self._size = size
        # allow storing a single element, None, or a chain (list) for subclasses
        self._table: list[Any] = [None] * size

    def _get_rnd_idx(self, key) -> int:
        return hash(key) % self._size

    def items(self) -> Generator[tuple[HashTableElementReturn, Any], Any, None]:
        for element in self._table:
            if isinstance(element, HashTableElement):
                yield (element.key, element.value)

    def display_figures(self) -> None:
        has_figure = False
        for inx, element in enumerate(self._table):
            if isinstance(element, HashTableElement) and isinstance(
                element.value, Figure
            ):
                print(repr(element.value))
                has_figure = True
        if not has_figure:
            print("Hash table do not have figures")

    def __setitem__(self, key, value) -> None:
        if self._table.count(None) == 0:
            raise OverflowError("Hash table is full")
        idx = self._get_rnd_idx(key)
        if self._table[idx] is not None:
            raise KeyError("Key already exist in hash table")

        self._table[idx] = HashTableElement(key, value)

    def __getitem__(self, key) -> HashTableElementReturn:
        key_hash = hash(key)
        element = self._table[key_hash % self._size]
        if isinstance(element, HashTableElement) and element.key_hash == hash(key):
            return element.value
        raise KeyError

    def __delitem__(self, key) -> None:
        key_hash = hash(key)
        element = self._table[key_hash % self._size]
        if isinstance(element, HashTableElement) and element.key_hash == hash(key):
            self._table[key_hash % self._size] = None
            return
        raise KeyError

    def __contains__(self, key) -> bool:
        key_hash = hash(key)
        element = self._table[key_hash % self._size]
        if isinstance(element, HashTableElement) and element.key_hash == key_hash:
            return True
        return False

    def __len__(self) -> int:
        counter = 0
        for element in self._table:
            if isinstance(element, HashTableElement):
                counter += 1
        return counter

    def __iter__(self):
        for key, _ in self.items():
            yield key

    def __repr__(self):
        pairs = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"HashTable({{{pairs}}})"


class HashTableSeparateChaining(HashTable):
    def __init__(self, size) -> None:
        super().__init__(size)
        self._chains: list[list[HashTableElement]] = [[] for _ in range(size)]

    def __setitem__(self, key, value) -> None:
        idx = self._get_rnd_idx(key)
        new_element = HashTableElement(key, value)
        if self.__len__() >= self._size**2:
            raise OverflowError("Hash table is full")
        self._chains[idx].append(new_element)

    def __len__(self) -> int:
        counter = 0
        for chain in self._chains:
            counter += len(chain)
        return counter

    def items(self) -> Generator[tuple[HashTableElementReturn, Any], Any, None]:
        # yield elements from open-addressing table
        for element in self._table:
            if isinstance(element, HashTableElement):
                yield (element.key, element.value)
        # yield elements from chaining storage if present
        if hasattr(self, "_chains"):
            for chain in self._chains:
                for element in chain:
                    if isinstance(element, HashTableElement):
                        yield (element.key, element.value)

    def display_figures(self) -> None:
        has_figure = False
        # check open-addressing table
        for inx, element in enumerate(self._table):
            if isinstance(element, HashTableElement) and isinstance(
                element.value, Figure
            ):
                print(repr(element.value))
                has_figure = True
        # check chaining storage if present
        if hasattr(self, "_chains"):
            for chain in self._chains:
                for element in chain:
                    if isinstance(element, HashTableElement) and isinstance(
                        element.value, Figure
                    ):
                        print(repr(element.value))
                        has_figure = True
        if not has_figure:
            print("Hash table do not have figures")


class HashTableSpecialDel(HashTableSeparateChaining):
    def __init__(self, size, max_area) -> None:
        super().__init__(size)
        self._chains: list[list[HashTableElement]] = [[] for _ in range(size)]
        self.__max_area = max_area

    def __setitem__(self, key, value) -> None:
        idx = self._get_rnd_idx(key)
        new_element = HashTableElement(key, value)
        if self.__len__() >= self._size**2:
            raise OverflowError("Hash table is full")
        if isinstance(value, ParalleloGram) and hasattr(value, "calc_area"):
            if value.calc_area() > self.__max_area:
                print(
                    f"Figure area {value.calc_area()} is too big for this hash table (max area: {self.__max_area})"
                )
                raise ValueError("Figure area is too big for this hash table")
        self._chains[idx].append(new_element)
