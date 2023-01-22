import random


def swap(a, p1, p2):
    temp = a[p1]
    a[p1] = a[p2]
    a[p2] = temp


# i as swap index
# j as scan index
# to choose partition value
def partition(a, lo, hi):
    pivot = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i = i + 1
            swap(a, i, j)
    i = i + 1
    swap(a, i, hi)
    return i


def sort(array, lo, hi):
    if lo >= hi or lo < 0:
        return
    p = partition(array, lo, hi)
    sort(array, lo, p - 1)
    sort(array, p + 1, hi)


tests_array = [
    [64, 25, 12, 22, 11],
    [123, 1, 34, 56, 78, 87, 22, 2, 33, 11, 32, 90, 0, 42],
    [123, 1, 34, 34, 78, 87, 22, 2, 33, 33, 32, 90, 0, 42],
    [random.randint(0, 1024) for _ in range(16)],
    [random.randint(0, 1024) for _ in range(128)]
]

for test in tests_array:
    sort(test, 0, len(test) - 1)
    print(test)
