import random


# n = array len
def sort(array):
    for i, el in enumerate(array):  # n
        minj = i
        for j, el1 in enumerate(array[i + 1:]):  # n - i
            if el1 < array[minj]:
                minj = j + i + 1
        if minj != i:
            array[i] = array[minj]
            array[minj] = el
    return array
# O(n*n) == O(n^2)


tests_array = [
    [64, 25, 12, 22, 11],
    [123, 1, 34, 56, 78, 87, 22, 2, 33, 11, 32, 90, 0, 42],
    [123, 1, 34, 34, 78, 87, 22, 2, 33, 33, 32, 90, 0, 42],
    [1, 2, 4, 5, 6, 9, 112, 2, 1, 33, 44, 7],
    [random.randint(0, 1024) for _ in range(128)]
]

for test in tests_array:
    print(sort(test))
