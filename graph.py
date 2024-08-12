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

# def total_out_degree(node, memo=None):
#     if memo is None:
#         memo = {}
    
#     memo[node] = True
    
#     in_degree = DG.out_degree(node)
#     for successor in list(DG.successors(node)):
#         if successor not in memo:
#             in_degree += total_out_degree(successor, memo)
#     return in_degree

# def total_in_degree(node, memo=None):
#     if memo is None:
#         memo = {}
    
#     memo[node] = True
    
#     in_degree = DG.in_degree(node)
#     for predecessor in list(DG.predecessors(node)):
#         if predecessor not in memo:
#             in_degree += total_in_degree(predecessor, memo)
#     return in_degree

#sort nodes by total out degree node 1 to 16 with values
# out_degree = {}
# for node in list(range(1, 17)):
#     out_degree[node] = total_out_degree(node)
# out_degree = dict(sorted(out_degree.items(), key=lambda item: item[1], reverse=False))
# print(out_degree)

# plt.figure(figsize=(10, 10))
# pos = nx.spring_l(ayout(DG, k=10/np.sqrt(DG.order()))
# colors = nx.get_edge_attributes(DG, "color").values()
# nx.draw(DG, pos, edge_color=colors, with_labels=True, node_size=2000, font_size=10, node_color="skyblue")
# plt.show()

#get list of all neighbours of a node


def total_neighbours_degree(node):
    total = 0
    total_successors = 0
    total_predecessors = 0
    for successor in list(DG.successors(node)):
        total_successors += DG.degree(successor)
        total += DG.degree(successor)
    for predecessor in list(DG.predecessors(node)):
        total_predecessors += DG.degree(predecessor)
        total += DG.degree(predecessor)
    final_total = {
         "total": total,
         "successors": total_successors,
         "predecessors": total_predecessors
    }
    return final_total

#sort nodes by total neighbours degree node 1 to 16 with values, sort by successors
neighbours_degree = {}
for node in list(range(1, 17)):
    neighbours_degree[node] = total_neighbours_degree(node)
neighbours_degree = dict(sorted(neighbours_degree.items(), key=lambda item: item[1]["successors"], reverse=False))

#neighbours_degree_keys to array
sorted_nodes = list(neighbours_degree.keys())

#remove nodes from graph
def remove_nodes(percent):
    remove_nodes = sorted_nodes[:int(len(sorted_nodes) * (100 - percent) / 100)]
    return remove_nodes






