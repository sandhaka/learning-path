def find_path(alist):
    in_edges, out_edges = [0] * len(alist), [0] * len(alist)
    path = []

    def enumerate_degrees():
        for k in alist.keys():
            out_edges[k] = len(alist[k])
            for e in alist[k]:
                in_edges[e] += 1

    def path_exists():
        start_nodes, end_nodes = 0, 0
        for i in alist.keys():
            if out_edges[i] - in_edges[i] > 1:
                return False
            if in_edges[i] - out_edges[i] > 1:
                return False
            # has 1 extra outgoing
            elif out_edges[i] - in_edges[i] == 1:
                start_nodes += 1
            # has 1 extra incoming
            elif in_edges[i] - out_edges[i] == 1:
                end_nodes += 1
        return (start_nodes == 0 and end_nodes == 0) or (
            start_nodes == 1 and end_nodes == 1
        )

    def find_start_node():
        start = 0
        for i in alist.keys():
            if out_edges[i] - in_edges[i] == 1:
                return i
            if out_edges[i] > 0:
                start = i
        return start

    def dfs(node_id):
        while len(alist[node_id]) > 0:
            neighbor = alist[node_id].pop()
            dfs(neighbor)
        path.insert(0, node_id)

    enumerate_degrees()  # n + e
    if not path_exists():  # n
        return None
    start_node = find_start_node()  # n
    dfs(start_node)  # n + e
    return path


# Total: O(2(n+e)+2n) ~ O(n + e)

# GPT Q&A:
"""
ME: Takes 'enumerate_degrees' function, why his time complexity is O(V+E)?
    Why not O(V*E)? When '*' operator come into play?

G:  The enumerate_degrees function has a time complexity of O(V+E) because it iterates through all the vertices (V) in 
the adjacency list and for each vertex, it iterates through all its neighbors (E).

Here is the pseudocode for the enumerate_degrees function:

for each vertex v in the adjacency list:
    out_edges[v] = number of neighbors of v
    for each neighbor w of v:
        in_edges[w] += 1
        
The first loop iterates through all the vertices in the adjacency list, which takes O(V) time. 
The inner loop iterates through all the neighbors of each vertex, which takes O(E) time. Therefore, the overall 
time complexity of the enumerate_degrees function is O(V+E).

The time complexity of an algorithm is typically expressed in terms of the number of steps it takes, 
rather than the actual time it takes to run. 
The "big O" notation is a way of expressing the upper bound of an algorithm's time complexity.

In the case of the enumerate_degrees function, the time complexity is O(V+E), because the number of steps it takes is 
proportional to the number of vertices (V) plus the number of edges (E) in the graph.

The "*" operator comes into play when an algorithm has nested loops that are both dependent on the size of the input. 
For example, consider the following algorithm:

for i in range(n):
    for j in range(m):
        do_something()
        
In this case, the inner loop runs m times for each iteration of the outer loop, so the total number of steps is n * m. 
The time complexity of this algorithm would be O(n * m).
In contrast, the enumerate_degrees function does not have nested loops that are both dependent on the size of the input. 
The inner loop iterates through the neighbors of each vertex, which is a fixed number for each vertex. 
The outer loop iterates through all the vertices in the adjacency list, which is proportional to the number of 
vertices (V) in the graph. Therefore, the time complexity of the enumerate_degrees function is O(V+E).
"""

adjacency_lists = [
    {
        0: [],
        1: [2, 3],
        2: [2, 4, 4],
        3: [1, 2, 5],
        4: [3, 6],
        5: [6],
        6: [3],
    },
    {0: [1], 1: [2, 3], 2: [1], 3: [4], 4: []},
    {0: [1], 1: [2, 2], 2: [0, 3], 3: [1]},
]

for a in adjacency_lists:
    path_found = find_path(a)
    print(path_found)
