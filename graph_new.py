import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pyvis.network import Network
from utils.store import relations
from utils.store import members

DG = nx.DiGraph()
DG.add_nodes_from(list(range(1, 19)), color="red", size=5)
DG.add_nodes_from(relations, color="skyblue", size=10)
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
DG.add_edges_from([("child", 17, {"color": "green"}), ("inv-grand", 17, {"color": "blue"}), (17, "inv-in-law", {"color": "black"})])
DG.add_edges_from([("child", 18, {"color": "green"}), ("inv-un", 18, {"color": "blue"}), (18, "sibling-in-law", {"color": "black"})])

all_graph = nx.DiGraph()
all_graph.add_nodes_from(list(range(1, 71)), color="red", size=5)
all_graph.add_nodes_from(members, color="skyblue", size=10)
all_graph.add_edges_from([("son", 1, {"color": "green"}), ("brother", 1, {"color": "blue"}), (1, "son", {"color": "black"})])
all_graph.add_edges_from([("daughter", 2, {"color": "green"}), ("sister", 2, {"color": "blue"}), (2, "daughter", {"color": "black"})])
all_graph.add_edges_from([("son", 3, {"color": "green"}), ("sister", 3, {"color": "blue"}), (3, "daughter", {"color": "black"})])
all_graph.add_edges_from([("daughter", 4, {"color": "green"}), ("brother", 4, {"color": "blue"}), (4, "son", {"color": "black"})])
all_graph.add_edges_from([("sister", 5, {"color": "green"}), ("sister", 5, {"color": "blue"}), (5, "sister", {"color": "black"})])
all_graph.add_edges_from([("brother", 6, {"color": "green"}), ("brother", 6, {"color": "blue"}), (6, "brother", {"color": "black"})])
all_graph.add_edges_from([("sister", 7, {"color": "green"}), ("brother", 7, {"color": "blue"}), (7, "brother", {"color": "black"})])
all_graph.add_edges_from([("brother", 8, {"color": "green"}), ("sister", 8, {"color": "blue"}), (8, "sister", {"color": "black"})])
all_graph.add_edges_from([("daughter", 9, {"color": "green"}), ("aunt", 9, {"color": "blue"}), (9, "sister", {"color": "black"})])
all_graph.add_edges_from([("son", 10, {"color": "green"}), ("uncle", 10, {"color": "blue"}), (10, "brother", {"color": "black"})])
all_graph.add_edges_from([("son", 11, {"color": "green"}), ("aunt", 11, {"color": "blue"}), (11, "sister", {"color": "black"})])
all_graph.add_edges_from([("daughter", 12, {"color": "green"}), ("uncle", 12, {"color": "blue"}), (12, "brother", {"color": "black"})])
all_graph.add_edges_from([("father", 13, {"color": "green"}), ("daughter", 13, {"color": "blue"}), (13, "sister", {"color": "black"})])
all_graph.add_edges_from([("mother", 14, {"color": "green"}), ("son", 14, {"color": "blue"}), (14, "brother", {"color": "black"})])
all_graph.add_edges_from([("father", 15, {"color": "green"}), ("son", 15, {"color": "blue"}), (15, "son", {"color": "black"})])
all_graph.add_edges_from([("mother", 16, {"color": "green"}), ("daughter", 16, {"color": "blue"}), (16, "daughter", {"color": "black"})])
all_graph.add_edges_from([("brother", 17, {"color": "green"}), ("father", 17, {"color": "blue"}), (17, "father", {"color": "black"})])
all_graph.add_edges_from([("brother", 18, {"color": "green"}), ("mother", 18, {"color": "blue"}), (18, "mother", {"color": "black"})])
all_graph.add_edges_from([("sister", 19, {"color": "green"}), ("mother", 19, {"color": "blue"}), (19, "mother", {"color": "black"})])
all_graph.add_edges_from([("sister", 20, {"color": "green"}), ("father", 20, {"color": "blue"}), (20, "father", {"color": "black"})])
all_graph.add_edges_from([("mother", 21, {"color": "green"}), ("sister", 21, {"color": "blue"}), (21, "aunt", {"color": "black"})])
all_graph.add_edges_from([("father", 22, {"color": "green"}), ("brother", 22, {"color": "blue"}), (22, "uncle", {"color": "black"})])
all_graph.add_edges_from([("mother", 23, {"color": "green"}), ("brother", 23, {"color": "blue"}), (23, "uncle", {"color": "black"})])
all_graph.add_edges_from([("father", 24, {"color": "green"}), ("sister", 24, {"color": "blue"}), (24, "aunt", {"color": "black"})])
all_graph.add_edges_from([("daughter", 25, {"color": "green"}), ("grandfather", 25, {"color": "blue"}), (25, "father", {"color": "black"})])
all_graph.add_edges_from([("sister", 26, {"color": "green"}), ("grandmother", 26, {"color": "blue"}), (26, "mother", {"color": "black"})])
all_graph.add_edges_from([("son", 27, {"color": "green"}), ("grandfather", 27, {"color": "blue"}), (27, "father", {"color": "black"})])
all_graph.add_edges_from([("daughter", 28, {"color": "green"}), ("grandmother", 28, {"color": "blue"}), (28, "mother", {"color": "black"})])
all_graph.add_edges_from([("husband", 29, {"color": "green"}), ("daughter", 29, {"color": "blue"}), (29, "daughter", {"color": "black"})])
all_graph.add_edges_from([("wife", 30, {"color": "green"}), ("son", 30, {"color": "blue"}), (30, "son", {"color": "black"})])
all_graph.add_edges_from([("husband", 31, {"color": "green"}), ("son", 31, {"color": "blue"}), (31, "son", {"color": "black"})])
all_graph.add_edges_from([("wife", 32, {"color": "green"}), ("daughter", 32, {"color": "blue"}), (32, "daughter", {"color": "black"})])
all_graph.add_edges_from([("brother", 33, {"color": "green"}), ("daughter", 33, {"color": "blue"}), (33, "niece", {"color": "black"})])
all_graph.add_edges_from([("sister", 34, {"color": "green"}), ("son", 34, {"color": "blue"}), (34, "nephew", {"color": "black"})])
all_graph.add_edges_from([("brother", 35, {"color": "green"}), ("son", 35, {"color": "blue"}), (35, "nephew", {"color": "black"})])
all_graph.add_edges_from([("sister", 36, {"color": "green"}), ("daughter", 36, {"color": "blue"}), (36, "niece", {"color": "black"})])
all_graph.add_edges_from([("son", 37, {"color": "green"}), ("son", 37, {"color": "blue"}), (37, "grandson", {"color": "black"})])
all_graph.add_edges_from([("daughter", 38, {"color": "green"}), ("daughter", 38, {"color": "blue"}), (38, "granddaughter", {"color": "black"})])
all_graph.add_edges_from([("daughter", 39, {"color": "green"}), ("son", 39, {"color": "blue"}), (39, "grandson", {"color": "black"})])
all_graph.add_edges_from([("son", 40, {"color": "green"}), ("daughter", 40, {"color": "blue"}), (40, "granddaughter", {"color": "black"})])
all_graph.add_edges_from([("grandson", 41, {"color": "green"}), ("sister", 41, {"color": "blue"}), (41, "granddaughter", {"color": "black"})])
all_graph.add_edges_from([("granddaughter", 42, {"color": "green"}), ("brother", 42, {"color": "blue"}), (42, "grandson", {"color": "black"})])
all_graph.add_edges_from([("granddaughter", 43, {"color": "green"}), ("sister", 43, {"color": "blue"}), (43, "granddaughter", {"color": "black"})])
all_graph.add_edges_from([("grandson", 44, {"color": "green"}), ("brother", 44, {"color": "blue"}), (44, "grandson", {"color": "black"})])
all_graph.add_edges_from([("husband", 45, {"color": "green"}), ("grandson", 45, {"color": "blue"}), (45, "grandson", {"color": "black"})])
all_graph.add_edges_from([("wife", 46, {"color": "green"}), ("granddaughter", 46, {"color": "blue"}), (46, "granddaughter", {"color": "black"})])
all_graph.add_edges_from([("wife", 47, {"color": "green"}), ("granddaughter", 47, {"color": "blue"}), (47, "granddaughter", {"color": "black"})])
all_graph.add_edges_from([("husband", 48, {"color": "green"}), ("grandson", 48, {"color": "blue"}), (48, "grandson", {"color": "black"})])
all_graph.add_edges_from([("husband", 49, {"color": "green"}), ("mother", 49, {"color": "blue"}), (49, "mother-in-law", {"color": "black"})])
all_graph.add_edges_from([("wife", 50, {"color": "green"}), ("father", 50, {"color": "blue"}), (50, "father-in-law", {"color": "black"})])
all_graph.add_edges_from([("wife", 51, {"color": "green"}), ("mother", 51, {"color": "blue"}), (51, "mother-in-law", {"color": "black"})])
all_graph.add_edges_from([("husband", 52, {"color": "green"}), ("father", 52, {"color": "blue"}), (52, "father-in-law", {"color": "black"})])
all_graph.add_edges_from([("mother", 53, {"color": "green"}), ("father", 53, {"color": "blue"}), (53, "grandfather", {"color": "black"})])
all_graph.add_edges_from([("father", 54, {"color": "green"}), ("mother", 54, {"color": "blue"}), (54, "grandmother", {"color": "black"})])
all_graph.add_edges_from([("mother", 55, {"color": "green"}), ("mother", 55, {"color": "blue"}), (55, "grandmother", {"color": "black"})])
all_graph.add_edges_from([("father", 56, {"color": "green"}), ("father", 56, {"color": "blue"}), (56, "grandfather", {"color": "black"})])
all_graph.add_edges_from([("brother", 57, {"color": "green"}), ("grandfather", 57, {"color": "blue"}), (57, "grandfather", {"color": "black"})])
all_graph.add_edges_from([("sister", 58, {"color": "green"}), ("grandmother", 58, {"color": "blue"}), (58, "grandmother", {"color": "black"})])
all_graph.add_edges_from([("sister", 59, {"color": "green"}), ("grandfather", 59, {"color": "blue"}), (59, "grandfather", {"color": "black"})])
all_graph.add_edges_from([("brother", 60, {"color": "green"}), ("grandmother", 60, {"color": "blue"}), (60, "grandmother", {"color": "black"})])
all_graph.add_edges_from([("son", 61, {"color": "green"}), ("wife", 61, {"color": "blue"}), (61, "daughter-in-law", {"color": "black"})])
all_graph.add_edges_from([("daughter", 62, {"color": "green"}), ("husband", 62, {"color": "blue"}), (62, "son-in-law", {"color": "black"})])
all_graph.add_edges_from([("daughter", 63, {"color": "green"}), ("grandfather", 63, {"color": "blue"}), (63, "father-in-law", {"color": "black"})])
all_graph.add_edges_from([("son", 64, {"color": "green"}), ("grandmother", 64, {"color": "blue"}), (64, "mother-in-law", {"color": "black"})])
all_graph.add_edges_from([("son", 65, {"color": "green"}), ("grandfather", 65, {"color": "blue"}), (65, "father-in-law", {"color": "black"})])
all_graph.add_edges_from([("daughter", 66, {"color": "green"}), ("grandmother", 66, {"color": "blue"}), (66, "mother-in-law", {"color": "black"})])
all_graph.add_edges_from([("daughter", 67, {"color": "green"}), ("uncle", 67, {"color": "blue"}), (67, "brother-in-law", {"color": "black"})])
all_graph.add_edges_from([("son", 68, {"color": "green"}), ("aunt", 68, {"color": "blue"}), (68, "sister-in-law", {"color": "black"})])
all_graph.add_edges_from([("son", 69, {"color": "green"}), ("uncle", 69, {"color": "blue"}), (69, "brother-in-law", {"color": "black"})])
all_graph.add_edges_from([("daughter", 70, {"color": "green"}), ("aunt", 70, {"color": "blue"}), (70, "sister-in-law", {"color": "black"})])
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

# plt.figure(figsize=(100, 100))
# pos = nx.spring_layout(all_graph, k=1)
# colors = nx.get_edge_attributes(all_graph, "color").values()
# nx.draw(all_graph, pos, edge_color=colors, with_labels=True, node_size=1000, font_size=5, node_color="skyblue")
# plt.show()

def visualize(graph):
    nt = Network("700px", "100%", directed=True, neighborhood_highlight=True, select_menu=True, filter_menu=True)
    nt.from_nx(graph)
    nt.show("nx.html", notebook=False)

#get list of all neighbours of a node
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
visualize(DG)