import math
from heapq import heappush, heappop

import utils.benchmarks

adjacency_list = {
    0: [(1, 7)],
    1: [(2, 4)],
    2: [(6, 7)],
    3: [],
    4: [(6, 3)],
    5: [],
    6: [(9, 6), (12, 8)],
    7: [],
    8: [(9, 8), (10, 5), (11, 3), (12, 3)],
    9: [],
    10: [(9, 8), (14, 3)],
    11: [(16, 7)],
    12: [(11, 10), (13, 3)],
    13: [(17, 1), (21, 2)],
    14: [(19, 1)],
    15: [(18, 4)],
    16: [(17, 10), (19, 3)],
    17: [(18, 9), (23, 1)],
    18: [(19, 9)],
    19: [(23, 1)],
    20: [(18, 1), (22, 3)],
    21: [],
    22: [(25, 2)],
    23: [(24, 5), (25, 9), (27, 9)],
    24: [(28, 4), (29, 1), (30, 1)],
    25: [(29, 4)],
    26: [(29, 6)],
    27: [(30, 2)],
    28: [(36, 10)],
    29: [(31, 8), (34, 7), (36, 8)],
    30: [(36, 3)],
    31: [(32, 6)],
    32: [(36, 8)],
    33: [(35, 4)],
    34: [(37, 10), (38, 7)],
    35: [(38, 6)],
    36: [],
    37: [],
    38: [(40, 7)],
    39: [],
    40: [(41, 4)],
    41: [],
    42: [],
}


@utils.benchmarks.benchmark
def dijkstra(alist: dict[int, list[tuple[int, int]]], s: int = 0, e: int = 0) -> tuple[list[float], list[int]]:
    n = len(alist)
    visited = [False] * (n + 1)
    prev: list[int] = [-1] * (n + 1)
    # Distance array
    dist: list[float] = [math.inf] * (n + 1)
    # Priority queue (using heap queue algorithm)
    pq = []
    # Setup
    heappush(pq, (0, s))
    dist[s] = 0
    while len(pq) > 0:
        _, node = heappop(pq)
        visited[node] = True
        # Explore next
        for next_node, next_arc_w in alist[node]:
            if visited[next_node]:
                continue
            distance = dist[node] + next_arc_w
            if distance < dist[next_node]:
                prev[next_node] = node
                heappush(pq, (distance, next_node))
                dist[next_node] = distance
        if e == node:
            break
    return dist, prev


# noinspection DuplicatedCode
def find_shortest_path(graph_adj_list, start_node, end_node):
    result, prev = dijkstra(graph_adj_list, start_node, end_node)
    path = []
    at = end_node
    if result[end_node] == math.inf:
        print(f"No path exist for node {end_node}")
        return
    while at > 0:
        path.append(at)
        at = prev[at]
    path.reverse()
    print(f"Shortest path from {start_node} to {end_node} is: {path}, total cost: {result[end_node]}")


find_shortest_path(adjacency_list, 1, 19)
find_shortest_path(adjacency_list, 1, 36)
