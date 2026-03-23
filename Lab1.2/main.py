from random import randint

from data_structures import HashTable, HashTableSeparateChaining, HashTableSpecialDel
from figures import ParalleloGram


def _add_figures_to_hashtable(size_of_PG_table: int, PG_table: HashTable) -> None:
    while True:
        print(f"Hash table size: {size_of_PG_table}, current size: {len(PG_table)}")
        try:
            paraleloGram = ParalleloGram()

            PG_table[paraleloGram.calc_perimeter()] = paraleloGram

        except (ValueError, KeyError, OverflowError) as e:
            if isinstance(e, ValueError):
                print("Wrong figure was generated, wanna remade?")
                if input("Press enter to remake figure, or 0 to exit: ") == "0":
                    break
            if isinstance(e, KeyError):
                print("Key already exist in hash table, wanna remade?")
                if input("Press enter to remake figure, or 0 to exit: ") == "0":
                    break
            if isinstance(e, OverflowError):
                print("Hash table is full")
                break
            continue
    print("----------------- Hash table content of Parallelograms -----------------")
    for key, value in PG_table.items():
        print(repr(value))


def first_task() -> None:
    # ! Завдання першого рівня
    # – елемент хеш-таблиці, який являє собою геометричну фігуру
    # відповідно до варіанта (дод. 2, табл. Д2.1, «Клас»);
    # – хеш-таблицю з відкритою адресацією, яка використовує
    # метод хешування (дod. 2, табл. Д2.1, «Метод хешування») для за-
    # даного ключа (дод. 2, табл. Д2.1, «Ключ»);
    # 8
    # Необхідно:
    # – створити екземпляр хеш-таблиці заданого розміру;
    # – уставити елементи в хеш-таблицю в такий спосіб, щоб вона
    # не мала колізій;
    # – вивести вміст хеш-таблиці.
    print(
        "--------------------------------- First task ---------------------------------"
    )
    size_of_PG_table = randint(3, 5)
    PG_table = HashTable(size_of_PG_table)
    _add_figures_to_hashtable(size_of_PG_table, PG_table)


def second_task() -> None:
    print(
        "--------------------------------- Second task ---------------------------------"
    )
    # ! Завдання другого рівня
    # Змінити опис хеш-таблиці із завдання першого рівня так, щоб
    # у разі виникнення колізії вона вирішувалася методом згідно з варі-
    # антом завдання (дод. 2, табл. Д2.2);
    # Необхідно:
    # – створити екземпляр хеш-таблиці заданого розміру;
    # – уставити елементи в хеш-таблицю з урахуванням колізії;
    # – вивести вміст хеш-таблиці.
    size_of_PG_table = randint(2, 3)
    PG_table = HashTableSeparateChaining(size_of_PG_table)
    _add_figures_to_hashtable(size_of_PG_table, PG_table)


def third_task() -> None:
    print(
        "--------------------------------- Third task ---------------------------------"
    )
    # ! Завдання третього рівня
    # Змінити опис хеш-таблиці із завдання другого рівня так, щоб
    # видалялися елементи згідно із заданим критерієм (дод. 2, табл.
    # Д2.3);
    # Необхідно:
    # – створити екземпляр хеш-таблиці заданого розміру;
    # – уставити елементи в хеш-таблицю з урахуванням колізії та
    # вивести вміст хеш-таблиці;
    # – видалити елементи за заданим критерієм і вивести вміст
    # хеш-таблиці.
    size_of_PG_table = randint(2, 3)
    PG_table = HashTableSpecialDel(size_of_PG_table, max_area=200)  # Example max area
    _add_figures_to_hashtable(size_of_PG_table, PG_table)


if __name__ == "__main__":
    first_task()
    second_task()
    third_task()
