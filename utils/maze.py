import random

wall = 1
passage = 0

"""
Generate a random maze to use as graph map for shortest path algorithm searches
Iterative implementation (with stack)
https://en.wikipedia.org/wiki/Maze_generation_algorithm#Iterative_implementation_(with_stack)
"""


def gen(size: int):
    def get_neighbors(r, c):
        _n = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            x, y = r + dx, c + dy
            if 0 <= x < size and 0 <= y < size and maze_map[x][y] != passage:
                _n.append((x, y))
        return _n

    size = size * 2 + 1
    maze_map = [[wall] * size for _ in range(size)]

    stack = [(1, 1)]
    maze_map[1][1] = passage

    while stack:
        i, j = stack[-1]
        maze_map[i][j] = passage

        neighbors = get_neighbors(i, j)

        if neighbors:
            neighbor = random.choice(neighbors)

            maze_map[(i + neighbor[0]) // 2][(j + neighbor[1]) // 2] = passage

            stack.append(neighbor)
        else:
            stack.pop()

    # Create the entrance and the exit
    maze_map[0][1] = passage
    maze_map[size - 1][size - 2] = passage

    return maze_map
