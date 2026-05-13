from random import randint, seed

seed(42)


def generate_rnd_arr(pow: int) -> list[int]:
    arr = [randint(-99999, 99999) for _ in range(100**pow)]
    return arr


def insert_sort(arr: list[int]) -> list[int]:
    arr_copy = arr[:]
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy


def binary_search(arr: list[int], target: int) -> int | None:
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        elif target < arr[middle]:
            right = middle - 1
    return None


def interpolation_search(arr: list[int], target: int) -> int | None:
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return arr[low]
            return None
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return arr[pos]

        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return None
