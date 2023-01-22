def grid_traveler(r, c):
    table = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    table[1][1] = 1
    for row in range(r + 1):
        for col in range(c + 1):
            if row + 1 <= r:
                table[row + 1][col] += table[row][col]
            if col + 1 <= c:
                table[row][col + 1] += table[row][col]
    return table[r][c]


for rows, columns in [(2, 3), (1, 1), (3, 3), (18, 18)]:
    ways = grid_traveler(rows, columns)
    print(ways)
