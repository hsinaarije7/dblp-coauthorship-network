import pandas as pd
import networkx as nx
import community.community_louvain as community_louvain
import matplotlib.pyplot as plt
import ast

df = pd.read_csv("data/papers.csv")

G = nx.Graph()

for _, row in df.iterrows():
    authors = ast.literal_eval(row['authors'])

    for i in range(len(authors)):
        for j in range(i + 1, len(authors)):
            G.add_edge(authors[i], authors[j])

# Community detection
partition = community_louvain.best_partition(G)

# Layout
pos = nx.spring_layout(G, seed=42)

# Colors = communities
colors = [partition[node] for node in G.nodes()]

plt.figure(figsize=(10, 8))

nx.draw_networkx_nodes(G, pos, node_color=colors, cmap=plt.cm.rainbow, node_size=300)
nx.draw_networkx_edges(G, pos, alpha=0.3)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("DBLP Co-Authorship Communities (Louvain)")
plt.axis("off")
plt.show()