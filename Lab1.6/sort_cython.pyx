from libc.stdlib cimport malloc, free
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def insert_sort(list arr):
    cdef int n = len(arr)
    cdef long *c_arr = <long *>malloc(n * sizeof(long))
    cdef int i, j
    cdef long key

    for i in range(n):
        c_arr[i] = arr[i]

    for i in range(1, n):
        key = c_arr[i]
        j = i - 1
        while j >= 0 and key < c_arr[j]:
            c_arr[j + 1] = c_arr[j]
            j -= 1
        c_arr[j + 1] = key

    cdef list result = [0] * n
    for i in range(n):
        result[i] = c_arr[i]

    free(c_arr)
    return result