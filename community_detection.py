import pandas as pd
import networkx as nx
import community.community_louvain as community_louvain
from networkx.algorithms.community.quality import modularity
import ast

# Load data
df = pd.read_csv("data/papers.csv")

# Build graph
G = nx.Graph()

for _, row in df.iterrows():
    authors = ast.literal_eval(row['authors'])

    for i in range(len(authors)):
        for j in range(i + 1, len(authors)):
            G.add_edge(authors[i], authors[j])

# Run Louvain (Fast Unfolding)
partition = community_louvain.best_partition(G)

print("\nAuthor Communities:\n")

for author, comm_id in partition.items():
    print(author, "-> Community", comm_id)

# Group communities
communities = {}

for node, comm_id in partition.items():
    if comm_id not in communities:
        communities[comm_id] = []
    communities[comm_id].append(node)

community_list = list(communities.values())

# Modularity
mod_score = modularity(G, community_list)

print("\nNumber of communities:", len(communities))
print("Modularity Score:", mod_score)