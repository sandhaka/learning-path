# Weighted DAG generator by forward layers
import argparse
import random

parser = argparse.ArgumentParser("dag_gen2")
parser.add_argument(
    "--layers",
    help="DAG forward layers. Default=5",
    type=int,
    default=5,
)
args = parser.parse_args()
layers = [[] for _ in range(args.layers)]
edges = {}
node_index = -1


print(f"Creating {len(layers)} layers graph")

# Random horizontal connections -low probability-
def random_horizontal(layer):
    for node1 in layer:
        # Avoid cycles
        for node2 in filter(
            lambda n2: node1 != n2 and node1 not in map(lambda el: el[0], edges[n2]),
            layer,
        ):
            if random.randint(0, 100) < 10:
                w = random.randint(1, 10)
                edges[node1].append((node2, w))


# Connect two layers
def connect(layer1, layer2):
    random_horizontal(layer1)
    for node1 in layer1:
        for node2 in layer2:
            if random.randint(0, 100) < 30:
                w = random.randint(1, 10)
                edges[node1].append((node2, w))


# Start nodes 1 to 3
start_nodes = random.randint(1, 3)
start_layer = []

for sn in range(start_nodes + 1):
    node_index += 1
    start_layer.append(node_index)

# Gen nodes
for layer in layers:
    nodes = random.randint(2, 5)
    for n in range(nodes):
        node_index += 1
        layer.append(node_index)

# Connect all
layers.insert(0, start_layer)
for layer in layers:
    for node in layer:
        edges[node] = []
for i, layer in enumerate(layers[:-1]):
    connect(layer, layers[i + 1])

# Print in DOT language
print("digraph {")
for node_key in [node_key for node_key in edges.keys() if len(edges[node_key]) > 0]:
    for node_dst, weight in edges[node_key]:
        print(f" {node_key} -> {node_dst} [label={weight}];")
print("}")
print("---- Adjacency list ----")
print(edges)
