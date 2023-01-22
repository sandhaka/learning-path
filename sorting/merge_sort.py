import math
import random


def merge(left, right):  # n - 1 comparisons
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result


"""
!!!
log_2 n is (with suitable rounding) the number of times you can divide n by 2 before reaching 1
(or, equivalently, the number of times you can double 1 before reaching n).
!!!

So for algorithms that involve dividing the input or the search space approximately in half
(merge sort, binary search, quick sort) log_2 appears naturally.
Likewise for the height of a full binary tree (and thus algorithms like heap sort): there's one node at the top level,
two at the next level, four at the next, and so on: log_2 n is the number of levels you need before you can fit n
objects on the bottom level (which means 2n - 1 in the whole tree).
"""


# n = array len
def sort(array):
    length = len(array)
    if length <= 1:
        return array
    half = math.ceil(length/2)
    left = array[:half]
    right = array[half:]
    left = sort(left)  # n / 2
    right = sort(right)  # n / 2, these are log(n)
    return merge(left, right)  # plus merge that is n
# O( n log(n)  )


tests_array = [
    [64, 25, 12, 22, 11],
    [123, 1, 34, 56, 78, 87, 22, 2, 33, 11, 32, 90, 0, 42],
    [123, 1, 34, 34, 78, 87, 22, 2, 33, 33, 32, 90, 0, 42],
    [1, 2, 4, 5, 6, 9, 112, 2, 1, 33, 44, 7],
    [random.randint(0, 1024) for _ in range(128)]
]

for test in tests_array:
    print(sort(test))