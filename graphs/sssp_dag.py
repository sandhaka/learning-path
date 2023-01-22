# Single Source Shortest Path Alg.
import math


def visit(m, n, u, visited, index, order):
    if u in visited:
        return index
    visited.append(u)
    for v in range(n):
        if m[u][v] is not None and v not in visited:
            index = visit(m, n, v, visited, index, order)
    order[index] = u
    index -= 1
    return index


# DFS on DAG as sorting method
def topological_sort(m):
    n = len(m)
    visited = []
    order = [None for _ in range(n)]
    index = n - 1
    for u in range(n):
        if u not in visited:
            index = visit(m, n, u, visited, index, order)
    return order


def sssp(m, start):
    n = len(m)
    min_dist = [math.inf for _ in range(n)]
    min_dist[start] = 0.0
    nodes = topological_sort(m)
    for i in nodes:
        for j in range(n):
            if m[i][j] is not None:
                arc_d = m[i][j] + min_dist[i]
                if arc_d < min_dist[j]:
                    min_dist[j] = arc_d
    return min_dist


# DAG Adjacency matrix
graph_adj_matrix = [[None for _ in range(7)] for _ in range(7)]
graph_adj_matrix[0][1] = 3
graph_adj_matrix[0][2] = 2
graph_adj_matrix[0][5] = 3
graph_adj_matrix[1][3] = 1
graph_adj_matrix[1][2] = 6
graph_adj_matrix[2][3] = 1
graph_adj_matrix[2][4] = 1
graph_adj_matrix[3][4] = 5
graph_adj_matrix[5][4] = 7

# Find shortest distance from node 0 to all other nodes
sssp_results = sssp(graph_adj_matrix, 0)
print(sssp_results)
# Find shortest distance from node 6 to all other nodes
sssp_results = sssp(graph_adj_matrix, 6)
print(sssp_results)
# Find shortest distance from node 3 to all other nodes
sssp_results = sssp(graph_adj_matrix, 3)
print(sssp_results)
