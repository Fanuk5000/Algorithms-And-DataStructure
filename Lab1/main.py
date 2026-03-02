from random import randint
from typing import Iterable

from data_structures import IntList, StringDeque


def print_iterator(arr: Iterable) -> None:
    for i in arr:
        print(i, end=" ")
    print()


def main() -> None:
    print("1 -------------- Список цілих чисел --------------")
    int_arr: IntList = IntList(max_size=10)
    for _ in range(10):
        int_arr.insert(randint(-100, 100))
    print_iterator(int_arr.data)
    int_arr.delete()
    print(
        "\n2 -------------- Двоспрямований список Рядковий(цілі додатні числа) --------------"
    )
    string_deque: StringDeque = StringDeque(max_size=10)
    for _ in range(5):
        string_deque.insert_back(str(randint(1, 100)))
        string_deque.insert_front(str(randint(-100, -1)))
    print_iterator(string_deque.data)

    print(
        "\n3 -------------- Список цілих чисел та Двоспрямований список Рядковий(цілі додатні числа) --------------"
    )
    # Видалити зі списку парні додатні числа та вставити їх у список у відсортованому за спаданням.
    int_arr2: IntList = int_arr.copy()
    string_deque2: StringDeque = string_deque.copy(max_size=30)
    print("До видалення та вставки:", end=" ")
    print_iterator(int_arr2.data)

    for value in int_arr.data:
        if value > 0 and value % 2 == 0:
            string_deque2.insert_back(str(value))
            int_arr2.delete(value)
    print("Після видалення та вставки: ")
    print_iterator(int_arr2.data)
    print_iterator(string_deque2.data)

    print("Після сортування:", end=" ")
    string_deque2.sort(reverse=True)
    print_iterator(string_deque2.data)


if __name__ == "__main__":
    main()
