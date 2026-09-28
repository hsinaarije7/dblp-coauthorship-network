import pandas as pd
import networkx as nx
import community.community_louvain as community_louvain
from networkx.algorithms.community.quality import modularity
import ast

# Load data
df = pd.read_csv("data/papers.csv")

# Clean year column
df = df.dropna(subset=['year'])
df['year'] = df['year'].astype(int)

years = sorted(df['year'].unique())

results = []

for year in years:

    year_df = df[df['year'] == year]

    G = nx.Graph()

    # Build graph for that year
    for _, row in year_df.iterrows():

        authors = ast.literal_eval(row['authors'])

        for i in range(len(authors)):
            for j in range(i + 1, len(authors)):
                G.add_edge(authors[i], authors[j])

    if G.number_of_nodes() == 0:
        continue

    # Community detection
    partition = community_louvain.best_partition(G)

    communities = {}

    for node, comm_id in partition.items():
        communities.setdefault(comm_id, []).append(node)

    community_list = list(communities.values())

    # Modularity
    mod = modularity(G, community_list)

    results.append({
        "year": year,
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "communities": len(communities),
        "modularity": mod
    })

# Print results
for r in results:
    print(r)