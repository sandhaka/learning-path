"""
Strongly connected components has various usages.
SCC algorithms can be used as a first step in application that work only on strongly connected graphs.

In social networks, a group of people are generally strongly connected (students class, common games, common pages).
The scc algorithms can be used to suggest the commonly interests.

Navigation utility, search of two-way path in a streets map.

Used in 2SAT problem resolvers.
"""


def scc(g):
    stack = []
    low = [0] * len(g)
    ids = [-1] * len(g)
    c_label = 0
    scc_count = 0

    def dfs(i):
        nonlocal c_label, scc_count
        low[i] = c_label
        ids[i] = low[i]
        c_label += 1
        stack.append(i)
        # Visit all neighbors
        for j in g[i]:
            if ids[j] < 0:
                dfs(j)
            # Dfs callback: set low-link value
            if j in stack:
                low[i] = min(low[i], low[j])
        # After visiting all. If we are at the stack of as SCC empty
        # the stack until we're back of the start of the SCC
        if low[i] == ids[i]:
            while True:
                node = stack.pop()
                low[node] = ids[i]
                if node == i:
                    break
            scc_count += 1

    for k, v in enumerate(ids):
        if v < 0:
            dfs(k)
    return low


adj_list = {
    0: [1, 2],
    1: [0, 3],
    2: [3],
    3: [4, 5],
    4: [2, 5, 6],
    5: [7],
    6: [5],
    7: [6],
}

ret = scc(adj_list)
print(ret)
