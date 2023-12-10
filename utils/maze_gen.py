# Generate a random maze to use as graph map for shortest path algorithm searches

import argparse
import random
from colorama import init, Fore

parser = argparse.ArgumentParser("maze_gen")
parser.add_argument("--size", help="The size of the map square (side length)", type=int, default=8)

args = parser.parse_args()

wall = "w"
passage = "_"
size = args.size
maze_map = [[wall for _ in range(size)] for _ in range(size)]
maze_graph = {}

for a in range(size):
    for b in range(size):
        maze_graph[(a, b)] = []


def get_neighbors(r, c):
    _n = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= r + dx < size and 0 <= c + dy < size:
            _n.append((r + dx, c + dy))
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
    stack = []
    visited = []
    starting_cell = (random.randint(0, size - 1), random.randint(0, size - 1))
    visited.append(starting_cell)
    stack.append(starting_cell)
    maze_map[starting_cell[0]][starting_cell[1]] = passage
    while len(stack) > 0:
        i, j = stack.pop()
        neighbors = get_neighbors(i, j)
        neighbors = list(filter(lambda n: n not in visited, neighbors))
        if len(neighbors) > 0:
            stack.append(starting_cell)
            neighbor = random.choice(neighbors)
            # Create the passage
            maze_map[neighbor[0]][neighbor[1]] = passage
            visited.append(neighbor)
            stack.append(neighbor)


# Initialize colorama
init()

build()

print_maze(maze_map)

print(maze_graph)