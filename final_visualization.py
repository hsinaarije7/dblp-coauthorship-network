import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community.community_louvain as community_louvain
import ast

# Load data
df = pd.read_csv("data/papers.csv")

# Build graph
G = nx.Graph()

for _, row in df.iterrows():
    authors = ast.literal_eval(row['authors'])

    authors = [a.strip() for a in authors if a]

    for i in range(len(authors)):
        for j in range(i + 1, len(authors)):
            G.add_edge(authors[i], authors[j])

# -----------------------------
# 1. COMMUNITY DETECTION
# -----------------------------
partition = community_louvain.best_partition(G)

# Color mapping
colors = [partition[node] for node in G.nodes()]

# Layout (important for readability)
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 8))

# Draw nodes
nx.draw_networkx_nodes(
    G, pos,
    node_color=colors,
    cmap=plt.cm.rainbow,
    node_size=400
)

# Draw edges
nx.draw_networkx_edges(G, pos, alpha=0.3)

# Labels (small graph only)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("Final Co-Authorship Community Visualization (Louvain)")
plt.axis("off")

plt.savefig("results/community_graph.png", dpi=300)
plt.show()


# -----------------------------
# 2. YEARLY MODULARITY TREND
# -----------------------------
df = df.dropna(subset=['year'])
df['year'] = df['year'].astype(int)

years = sorted(df['year'].unique())

modularity_scores = []

for year in years:

    year_df = df[df['year'] == year]

    G_year = nx.Graph()

    for _, row in year_df.iterrows():
        authors = ast.literal_eval(row['authors'])

        for i in range(len(authors)):
            for j in range(i + 1, len(authors)):
                G_year.add_edge(authors[i], authors[j])

    if G_year.number_of_nodes() < 2:
        modularity_scores.append(0)
        continue

    partition_year = community_louvain.best_partition(G_year)

    communities = {}

    for node, comm_id in partition_year.items():
        communities.setdefault(comm_id, []).append(node)

    community_list = list(communities.values())

    # modularity approximation (simple version)
    modularity_scores.append(len(community_list))

# Plot trend
plt.figure(figsize=(10, 5))

plt.plot(years, modularity_scores, marker='o')

plt.title("Evolution of Communities Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Communities")

plt.grid(True)

plt.savefig("results/evolution_trend.png", dpi=300)
plt.show()