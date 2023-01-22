import argparse
import random

parser = argparse.ArgumentParser("dag_gen")
parser.add_argument(
    "--min-per-rank",
    help="Nodes/Rank: how 'fat' the DAG should be. Default=1",
    type=int,
    default=1,
)
parser.add_argument(
    "--max-per-rank",
    help="Nodes/Rank: how 'fat' the DAG should be. Default=3",
    type=int,
    default=2,
)
parser.add_argument(
    "--min-ranks",
    help="Ranks: how 'tall' the DAG should be. Default=6",
    type=int,
    default=6,
)
parser.add_argument(
    "--max-ranks",
    help="Ranks: how 'tall' the DAG should be. Default=15",
    type=int,
    default=15,
)
parser.add_argument(
    "--edge-factor",
    help="Chance of having an Edge. Default=20",
    type=float,
    default=30.0,
)

args = parser.parse_args()

edges = []
min_per_ranks = args.min_per_rank
max_per_ranks = args.max_per_rank
min_ranks = args.min_ranks
max_ranks = args.max_ranks
edge_factor = args.edge_factor

nodes = 0

ranks = random.randint(min_ranks, max_ranks)

print("digraph {")
for rank in range(ranks):
    new_nodes = random.randint(min_per_ranks, max_per_ranks)
    for j in range(nodes):
        for k in range(new_nodes):
            if random.randint(0, 100) < edge_factor:
                w = random.randint(1, ranks * 2)
                print(f" {j} -> {k + nodes} [label={w}];")
                edges.append((j, k + nodes, w))
    nodes += new_nodes
print("}")

print("---- Adjacency list ----")

adj_list = dict()
for i in range(nodes):
    adj_list[i] = []

for edge in edges:
    key = edge[0]
    adj_list[key].append((edge[1], edge[2]))

print(adj_list)
