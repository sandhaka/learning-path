import argparse
from utils import maze
from colorama import init, Fore

parser = argparse.ArgumentParser("a-star")
parser.add_argument("--maze", help="The size of the map square (side length)", type=int, default=8)

args = parser.parse_args()

wall = 1
passage = 0
size = args.maze


def print_maze_on_console(m: list[list[int]]) -> None:
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] == "u":
                print(Fore.WHITE, f"{m[i][j]}", end="    ")
            elif m[i][j] == passage:
                print(Fore.GREEN, f"{m[i][j]}", end="    ")
            else:
                print(Fore.RED, f"{m[i][j]}", end="    ")
        print("\n")


# Init colorama
init()
# Get a maze sample
maze_board = maze.gen(size)
print_maze_on_console(maze_board)
