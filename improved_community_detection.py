import pandas as pd
import networkx as nx
import community.community_louvain as community_louvain
from networkx.algorithms.community.quality import modularity
import ast
from collections import defaultdict

# Load data
df = pd.read_csv("data/papers.csv")

# Weighted graph (IMPORTANT IMPROVEMENT)
G = nx.Graph()

# Count collaboration frequency (improves accuracy)
edge_weights = defaultdict(int)

for _, row in df.iterrows():

    authors = ast.literal_eval(row['authors'])

    # clean small noise
    authors = [a.strip() for a in authors if a]

    for i in range(len(authors)):
        for j in range(i + 1, len(authors)):

            a1, a2 = authors[i], authors[j]

            # increase weight if repeated collaboration
            edge_weights[(a1, a2)] += 1

# Add weighted edges
for (a1, a2), w in edge_weights.items():
    G.add_edge(a1, a2, weight=w)

print("Graph improved:")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# Louvain with weights (VERY IMPORTANT)
partition = community_louvain.best_partition(G, weight='weight')

# Organize communities
communities = defaultdict(list)

for node, comm_id in partition.items():
    communities[comm_id].append(node)

community_list = list(communities.values())

# Modularity (weighted)
mod_score = modularity(G, community_list, weight='weight')

print("\nNumber of communities:", len(communities))
print("Improved Modularity Score:", mod_score)

# Show biggest communities
print("\nTop communities:")
for k, v in sorted(communities.items(), key=lambda x: len(x[1]), reverse=True)[:5]:
    print(f"Community {k}: {len(v)} authors")