import pandas as pd
import networkx as nx
import ast

# Read CSV file
df = pd.read_csv("data/papers.csv")

# Create empty graph
G = nx.Graph()

# Loop through every paper
for _, row in df.iterrows():

    # Convert string list into Python list
    authors = ast.literal_eval(row['authors'])

    # Connect every pair of authors
    for i in range(len(authors)):
        for j in range(i + 1, len(authors)):

            author1 = authors[i]
            author2 = authors[j]

            G.add_edge(author1, author2)

# Print graph information
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Show first few nodes
print("\nSome authors:")
print(list(G.nodes())[:10])

# Show first few edges
print("\nSome collaborations:")
print(list(G.edges())[:10])