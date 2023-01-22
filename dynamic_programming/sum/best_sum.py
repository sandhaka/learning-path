def best_sum(target, array, memo=None):
    if target < 0:
        return None
    if target == 0:
        return []
    if memo is None:
        memo = dict()
    else:
        if target in memo.keys():
            return memo[target]
    shortest_combination = None
    for i in array:
        remainder = target - i
        remainder_combination = best_sum(remainder, array, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [i]
            if shortest_combination is None or len(shortest_combination) > len(combination):
                shortest_combination = combination
    memo[target] = shortest_combination
    return memo[target]


tests = [
    (7, [5, 3, 4, 7]),
    (8, [2, 3, 5]),
    (8, [1, 4, 5]),
    (100, [1, 2, 5, 25])
]
for test in tests:
    best = best_sum(test[0], test[1])
    print(f'{test[0]}: {best}')
