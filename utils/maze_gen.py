# Generate a random maze to use as graph map for shortest path algorithm searches

import argparse
import random
from colorama import init, Fore

parser = argparse.ArgumentParser("maze_gen")
parser.add_argument("--size", help="The size of the map square (side length)", type=int, default=30)

args = parser.parse_args()

wall = "w"
passage = "_"
size = args.size * 2 + 1
maze_map = [[wall] * size for _ in range(size)]
maze_graph = {}

for a in range(size):
    for b in range(size):
        maze_graph[(a, b)] = []


def get_neighbors(r, c):
    _n = []
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        x, y = r + dx, c + dy
        if 0 <= x < size and 0 <= y < size and maze_map[x][y] != passage:
            _n.append((x, y))
    return _n


def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == "u":
                print(Fore.WHITE, f"{maze[i][j]}", end="    ")
            elif maze[i][j] == passage:
                print(Fore.GREEN, f"{maze[i][j]}", end="    ")
            else:
                print(Fore.RED, f"{maze[i][j]}", end="    ")
        print("\n")


"""
Iterative implementation (with stack)
https://en.wikipedia.org/wiki/Maze_generation_algorithm#Iterative_implementation_(with_stack)
---
.1 Select a random cell, mark it as visited and push it into the stack
.2 While the stack is not empty:
    .A Pop a cell from the stack and make it the current cell
    .B If the current cell has any unvisited neighbour cells:
        .a Push it into the stack
        .b Select a random neighbors not yet visited
        .c Remove the wall between the current cell and the chosen cell
        .d Mark the chosen cell as visited and push it to the stack
"""


def build():
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


# Initialize colorama

init()
build()
print_maze(maze_map)
