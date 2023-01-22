import random


# n = array length
# m = target sum
def how_sum(target, array, memo=None):
    if target < 0:
        return None
    if target == 0:
        return []
    if memo is None:
        memo = dict()
    if target in memo.keys():
        return memo[target]
    random.shuffle(array)  # Optional: Increase results variability
    for i in array:  # n
        rem = how_sum(target - i, array, memo)  # m
        if rem is not None:
            memo[target] = rem + [i]  # m (Array copy)
            return memo[target]
    memo[target] = None
    return None
# Time O(n*m^2)


def test_how_sum():
    """
    target sum  | available numbers     | feasible:
    """

    test_cases = [
        (7,     [4, 3, 7, 2],           True),
        (7,     [4, 2],                 False),
        (11,    [1, 2, 5, 10, 8, 3, 9], True),
        (1024,  [1, 2, 5, 10, 8, 3, 9], True),
        (300,   [7, 14],                False)
    ]

    for p in test_cases:
        solution = how_sum(p[0], p[1])
        if not p[-1]:
            assert solution is None
        else:
            assert p[0] == sum(solution)
