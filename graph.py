import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from utils.store import relations

DG = nx.DiGraph()
DG.add_nodes_from(list(range(1, 17)))
DG.add_nodes_from(relations)
DG.add_edges_from([("SO", 1, {"color": "green"}), ("grand", 1, {"color": "blue"}), (1, "grand", {"color": "black"})])
DG.add_edges_from([("child", 2, {"color": "green"}), ("SO", 2, {"color": "blue"}), (2, "in-law", {"color": "black"})])
DG.add_edges_from([("SO", 3, {"color": "green"}), ("child", 3, {"color": "blue"}), (3, "child", {"color": "black"})])
DG.add_edges_from([("child", 4, {"color": "green"}), ("inv-grand", 4, {"color": "blue"}), (4, "inv-child", {"color": "black"})])
DG.add_edges_from([("inv-child", 5, {"color": "green"}), ("child", 5, {"color": "blue"}), (5, "sibling", {"color": "black"})])
DG.add_edges_from([("SO", 6, {"color": "green"}), ("inv-child", 6, {"color": "blue"}), (6, "inv-in-law", {"color": "black"})])
DG.add_edges_from([("child", 7, {"color": "green"}), ("child", 7, {"color": "blue"}), (7, "grand", {"color": "black"})])
DG.add_edges_from([("child", 8, {"color": "green"}), ("inv-un", 8, {"color": "blue"}), (8, "sibling", {"color": "black"})])
DG.add_edges_from([("inv-child", 9, {"color": "green"}), ("inv-child", 9, {"color": "blue"}), (9, "inv-grand", {"color": "black"})])
DG.add_edges_from([("grand", 10, {"color": "green"}), ("sibling", 10, {"color": "blue"}), (10, "grand", {"color": "black"})])
DG.add_edges_from([("child", 11, {"color": "green"}), ("sibling", 11, {"color": "blue"}), (11, "child", {"color": "black"})])
DG.add_edges_from([("sibling", 12, {"color": "green"}), ("child", 12, {"color": "blue"}), (12, "un", {"color": "black"})])
DG.add_edges_from([("inv-child", 13, {"color": "green"}), ("sibling", 13, {"color": "blue"}), (13, "inv-un", {"color": "black"})])
DG.add_edges_from([("sibling", 14, {"color": "green"}), ("inv-child", 14, {"color": "blue"}), (14, "inv-child", {"color": "black"})])
DG.add_edges_from([("sibling", 15, {"color": "green"}), ("inv-grand", 15, {"color": "blue"}), (15, "inv-grand", {"color": "black"})])
DG.add_edges_from([("sibling", 16, {"color": "green"}), ("sibling", 16, {"color": "blue"}), (16, "sibling", {"color": "black"})])


# Define shells (concentric layers of nodes)
shells = [list(range(1, 17)), relations]  # numeric nodes inside, relations outside
pos = nx.shell_layout(DG, shells)

# Plot setup
plt.figure(figsize=(16, 10))

# Draw nodes
nx.draw_networkx_nodes(DG, pos, node_size=1000, node_color="skyblue")

# Draw edges with their colors
edge_colors = [DG[u][v]["color"] for u, v in DG.edges()]
nx.draw_networkx_edges(DG, pos, edge_color=edge_colors, arrows=True, width=2)

# Add node labels (show both number and relation names)
labels = {node: str(node) for node in DG.nodes()}
nx.draw_networkx_labels(DG, pos, labels, font_size=10)

def total_neighbours_degree(node):
    total = 0
    total_successors = 0
    total_predecessors = 0
    suc = []
    for successor in list(DG.successors(node)):
        total_successors += DG.degree(successor)
        total += DG.degree(successor)
        suc.append(successor)
    for predecessor in list(DG.predecessors(node)):
        total_predecessors += DG.degree(predecessor)
        total += DG.degree(predecessor)
    final_total = {
         "total": total,
         "successors": total_successors,
         "predecessors": total_predecessors,
         "detail": suc
    }
    return final_total

#sort nodes by total neighbours degree node 1 to 16 with values, sort by successors
neighbours_degree = {}
for node in list(range(1, 17)):
    neighbours_degree[node] = total_neighbours_degree(node)
neighbours_degree = dict(sorted(neighbours_degree.items(), key=lambda item: item[1]["successors"], reverse=False))
print(neighbours_degree)
#neighbours_degree_keys to array
sorted_nodes = list(neighbours_degree.keys())
print(sorted_nodes)
#remove nodes from graph
def remove_nodes(percent):
    remove_nodes = sorted_nodes[:int(len(sorted_nodes) * (100 - percent) / 100)]
    return remove_nodes

print(remove_nodes(60))

plt.title("Shell Layout DG: Rule Nodes & Relation Groups", fontsize=15)
plt.axis("off")
plt.tight_layout()
plt.show()
