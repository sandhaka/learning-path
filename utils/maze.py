import random


class MazeBlocks:
    WALL = 1
    PASSAGE = 0


"""
Generate a random maze to use as graph map for shortest path algorithm searches
Iterative implementation (with stack)
https://en.wikipedia.org/wiki/Maze_generation_algorithm#Iterative_implementation_(with_stack)
"""


def gen(size: int) -> list[list[int]]:
    def get_neighbors(r, c):
        _n = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            x, y = r + dx, c + dy
            if 0 <= x < size and 0 <= y < size and maze_map[x][y] != MazeBlocks.PASSAGE:
                _n.append((x, y))
        return _n

    size = size * 2 + 1
    maze_map = [[MazeBlocks.WALL] * size for _ in range(size)]

    stack = [(1, 1)]
    maze_map[1][1] = MazeBlocks.PASSAGE

    while stack:
        i, j = stack[-1]
        maze_map[i][j] = MazeBlocks.PASSAGE

        neighbors = get_neighbors(i, j)

        if neighbors:
            neighbor = random.choice(neighbors)

            maze_map[(i + neighbor[0]) // 2][(j + neighbor[1]) // 2] = MazeBlocks.PASSAGE

            stack.append(neighbor)
        else:
            stack.pop()

    # Create the entrance and the exit
    maze_map[0][1] = MazeBlocks.PASSAGE
    maze_map[size - 1][size - 2] = MazeBlocks.PASSAGE

    return maze_map


"""
Transform maze to graph
"""


def maze2graph(maze: list[list[int]]) -> dict:
    graph = {}

    def get_neighbors(i, j, size):
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            if 0 <= i + dx < size - 1 and 0 <= j + dy < size - 1:
                yield i + dx, j + dy

    for r in range(1, len(maze) - 1, 2):
        for c in range(1, len(maze[0]) - 1, 2):
            if (r, c) not in graph:
                graph[(r, c)] = []
            for neighbor in get_neighbors(r, c, len(maze)):
                if maze[(r + neighbor[0]) // 2][(c + neighbor[1]) // 2] == MazeBlocks.PASSAGE:
                    graph[(r, c)].append(neighbor)

    return graph
