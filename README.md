# DBLP Co-authorship Network Analysis

Temporal analysis of a researcher co-authorship network using DBLP publication data, graph analysis, Louvain community detection, and modularity.

## Project Overview

This project analyzes collaboration patterns between researchers by constructing yearly co-authorship networks from DBLP publication data.

Each researcher is represented as a node, and a connection is created between researchers who co-authored the same publication.

The project studies how the structure of the research network changes over time.

## Objectives

- Construct yearly co-authorship networks from DBLP publication data.
- Analyze researchers and collaboration links.
- Detect research communities using the Louvain algorithm.
- Calculate modularity to evaluate community structure.
- Visualize network evolution over time.

## Methodology

The project follows these main steps:

1. Retrieve publication data from the DBLP search API.
2. Extract publication years and author information.
3. Construct a co-authorship graph for each year.
4. Apply Louvain community detection.
5. Calculate network modularity.
6. Track changes in researchers, collaboration links, communities, and modularity.
7. Generate network and evolution visualizations.

## Technologies

- Python
- NetworkX
- Pandas
- Matplotlib
- DBLP XML API

## Community Detection

The project uses the Louvain community detection algorithm to identify groups of researchers with stronger collaboration patterns.

Modularity is calculated to quantitatively evaluate the detected community structure.

## Project Structure

```text
dblp-coauthorship-network/
│
├── final_assignment_pipeline.py
└── README.md
