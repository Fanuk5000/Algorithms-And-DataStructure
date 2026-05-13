from functools import wraps
from typing import Callable

from algorithms import randint


def check_launch_time(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from time import perf_counter

        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(
            f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds"
        )
        return result

    return wrapper


@check_launch_time
def start_insert_sort(pow: int):
    from algorithms import generate_rnd_arr
    from sort_cython import insert_sort  # pyright: ignore[reportMissingImports]

    arr = generate_rnd_arr(pow)
    sorted_arr = insert_sort(arr)  # noqa: F841


@check_launch_time
def start_binary_search(arr: list[int], target: int):
    from algorithms import binary_search

    return binary_search(arr, target)


@check_launch_time
def start_interpolation_search(arr: list[int], target: int):
    from algorithms import interpolation_search

    return interpolation_search(arr, target)


def task_one():
    print("-" * 40 + "Task one" + "-" * 40)
    start_insert_sort(1)
    start_insert_sort(2)
    start_insert_sort(3)


def task_two():
    print("-" * 40 + "Task two" + "-" * 40)
    from algorithms import generate_rnd_arr

    arr_1: list[int] = generate_rnd_arr(1)
    arr_2: list[int] = generate_rnd_arr(2)
    arr_3: list[int] = generate_rnd_arr(3)
    arr_1.sort()
    arr_2.sort()
    arr_3.sort()

    start_binary_search(arr_1, 100000000)
    start_binary_search(arr_2, 100000000)
    start_binary_search(arr_3, 100000000)

    start_interpolation_search(arr_1, 100000000)
    start_interpolation_search(arr_2, 100000000)
    start_interpolation_search(arr_3, 100000000)


def task_three():
    print("-" * 40 + "Task three" + "-" * 40)
    N = 10000

    @check_launch_time
    def start_insert_sort2(arr: list[int]):
        from sort_cython import insert_sort  # pyright: ignore[reportMissingImports]

        sorted_arr = insert_sort(arr)  # noqa: F841

    best_case_arr = list(range(1, N + 1))
    worst_case_arr = list(range(N, 0, -1))
    avg_case_arr = [randint(-99999, 99999) for _ in range(N)]

    start_insert_sort2(best_case_arr)
    start_insert_sort2(worst_case_arr)
    start_insert_sort2(avg_case_arr)


if __name__ == "__main__":
    task_one()
    task_two()
    task_three()
