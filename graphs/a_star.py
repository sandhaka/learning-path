import argparse
import utils.maze as maze_generator
import matplotlib.pyplot as plt

from heapq import heappush, heappop
from colorama import init, Fore

parser = argparse.ArgumentParser("a-star", description="A* search algorithm collection")
parser.add_argument("--maze", help="The size of the map square (side length)", type=int, default=35)

args = parser.parse_args()

mz = maze_generator.MazeBlocks
size = args.maze


def print_maze_on_console(m: list[list[int]]) -> None:
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] == mz.PASSAGE:
                print(Fore.GREEN, f"{m[i][j]}", end="    ")
            else:
                print(Fore.RED, f"{m[i][j]}", end="    ")
        print("\n")


def a_star_search(g: dict) -> list:
    pass


# def plot_graph_verification(m, g) -> None:
#     plt.figure(figsize=(8, 8))
#     plt.ion()  # Turn on interactive mode
#     for node in g.keys():
#         plt.clf()  # Clear the previous plot
#         plt.imshow(m, cmap="binary", interpolation="none", origin="upper")
#         passage = [node] + g[node]
#         for point in passage:
#             plt.scatter(point[1], point[0], marker="o", color="red")
#         plt.title(f"Node {node}: {g[node]}")
#         plt.pause(5)
#     plt.ioff()  # Turn off interactive mode
#     plt.show()


# Init colorama
init()
# Get a maze sample
maze = maze_generator.gen(size)
adjacency_list = maze_generator.maze2graph(maze)

print_maze_on_console(maze)
