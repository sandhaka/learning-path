# Eulerian paths and circuits on directed graphs

adjacency_list = {
    0: [],
    1: [2, 3],
    2: [2, 4, 4],
    3: [1, 2, 5],
    4: [3, 6],
    5: [6],
    6: [3],
}


def enumerate_degrees(al):
    in_edges = [0] * len(al)
    out_edges = [0] * len(al)
    # Count the incoming and outgoing edges
    for node_key in al.keys():
        out_edges[node_key] = len(al[node_key])
        for edge in al[node_key]:
            in_edges[edge] += 1
    return in_edges, out_edges


def has_path(in_edges, out_edges):
    start_nodes = 0
    end_nodes = 0
    for node_id, _ in enumerate(in_edges):
        if out_edges[node_id] - in_edges[node_id] > 1:
            return False
        if in_edges[node_id] - out_edges[node_id] > 1:
            return False
        # 1 Extra outgoing
        elif out_edges[node_id] - in_edges[node_id] == 1:
            start_nodes += 1
        # 1 Extra incoming
        elif in_edges[node_id] - out_edges[node_id] == 1:
            end_nodes += 1
    return (start_nodes == 0 and end_nodes == 0) or (start_nodes == 1 and end_nodes == 1)


incoming_edges, outgoing_edges = enumerate_degrees(adjacency_list)
print(f"Incoming edges: {incoming_edges}")
print(f"Outgoing edges: {outgoing_edges}")
print(f"Has path: {has_path(incoming_edges, outgoing_edges)}")
