def grid_traveler(r, c, memo=None):
    if r < 1 or c < 1:
        return 0
    if r == 1 and c == 1:
        return 1
    memo_key = f'{r},{c}'
    if memo is None:
        memo = {}
    elif memo_key in memo.keys():
        return memo[memo_key]
    memo[memo_key] = grid_traveler(r - 1, c, memo) + grid_traveler(r, c - 1, memo)
    return memo[memo_key]


for rows, columns in [(2, 3), (9, 0), (1, 1), (3, 3), (18, 18)]:
    ways = grid_traveler(rows, columns)
    print(ways)
