import argparse
import utils.maze as mz
import matplotlib.pyplot as plt

from heapq import heappush, heappop

parser = argparse.ArgumentParser("a-star", description="A* search algorithm collection")
parser.add_argument("--maze", help="The size of the map square (side length)", type=int, default=20)

args = parser.parse_args()

size = args.maze


def plot_init() -> None:
    plt.figure(figsize=(12, 12))
    plt.ion()
    plt.title("Maze solver")


def plot_progress(p: list[tuple[int, int]], visited: list[tuple[int, int]], final_path=False) -> None:
    p = list(map(lambda x: (x[1], x[0]), p))
    visited = list(map(lambda x: (x[1], x[0]), visited))
    plt.clf()
    plt.imshow(maze, cmap="binary", interpolation="none", origin="upper")
    plt.xticks([]), plt.yticks([])
    plt.tick_params(axis="both", which="both", length=0)
    plt.plot(*zip(*p), marker="o", color="blue" if final_path else "red")
    plt.scatter(*zip(*visited), marker="o", color="green")
    plt.pause(0.1)


def plot_end() -> None:
    plt.ioff()  # Turn off interactive mode
    plt.show()


def astar(g: dict, start_node: tuple[int, int], goal_node: tuple[int, int]) -> list | None:
    plot_init()

    # A commonly used heuristic for maze-solving is the Manhattan distance
    def heuristic(node: tuple[int, int], goal: tuple[int, int]):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def rebuild_path(n):
        p = [n]
        while n in came_from:
            n = came_from[n]
            p.append(n)
        return p

    open_set = [(0, start_node)]
    came_from = {}
    cost_so_far = {start_node: 0}

    while len(open_set) > 0:
        curr_cost, curr_node = heappop(open_set)
        if curr_node == goal_node:
            goal_path = rebuild_path(goal_node)
            plot_progress([goal_node] + goal_path, cost_so_far.keys(), True)
            return goal_path

        for neighbor in g[curr_node]:
            new_cost = cost_so_far.get(curr_node) + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal_node)
                heappush(open_set, (priority, neighbor))
                came_from[neighbor] = curr_node
                plot_progress(rebuild_path(neighbor), cost_so_far.keys())

    return None


# Get a maze sample
maze = mz.gen(size)

# Convert maze to a graph
adjacency_list = mz.maze2graph(maze)

# Start at the most top left corner of the maze and end at the most bottom right cell
start = (1, 1)
end = (size * 2 - 1, size * 2 - 1)

path = astar(adjacency_list, start, end)

path.reverse()
print(path + [end])

input("Press any key to exit")
plot_end()
