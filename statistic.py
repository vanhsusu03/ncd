# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.patches import Patch

# # Load the dataset
# df = pd.read_csv("./data/2.2,2.3_train_5k.csv")

# # Count the target relation frequencies
# target_counts = df["target"].value_counts()

# # Define your relation groups
# relation_groups = {
#     "SO": ["wife", "husband"],
#     "in-law": ["son-in-law", "daughter-in-law"],
#     "inv-in-law": ["father-in-law", "mother-in-law"],
#     "grand": ["grandson", "granddaughter"],
#     "child": ["son", "daughter"],
#     "inv-un": ["uncle", "aunt"],
#     "inv-grand": ["grandfather", "grandmother"],
#     "inv-child": ["father", "mother"],
#     "un": ["nephew", "niece"],
#     "sibling": ["brother", "sister"]
# }

# # Filter and order the relations according to the group
# sorted_relations = []
# for group in relation_groups.values():
#     for rel in group:
#         if rel in target_counts:
#             sorted_relations.append(rel)

# # Filter and sort the target_counts accordingly
# target_counts_sorted = target_counts[sorted_relations]

# # Assign distinct clean colors (no pink, purple, gray)
# group_palette = [
#     '#528B8B', '#EEE8AA', '#528B8B', '#EE7600', '#7CCD7C', 
#     '#EEB4B4', '#EE6363', '#FFCC99', '#008B45', '#00CED1',
# ]

# # Map colors to relation groups
# relation_color_map = {}
# for (group_name, relations), color in zip(relation_groups.items(), group_palette):
#     for rel in relations:
#         relation_color_map[rel] = color

# # Prepare plot data
# relations = target_counts_sorted.index.tolist()
# frequencies = target_counts_sorted.values.tolist()
# bar_colors = [relation_color_map.get(rel, "gray") for rel in relations]

# # Plotting
# plt.figure(figsize=(12, 6))
# bars = plt.bar(relations, frequencies, color=bar_colors)

# # Add labels and formatting
# plt.xlabel("Relation", fontsize=10)
# plt.ylabel("Frequency", fontsize=10)
# plt.xticks(rotation=45, ha="right")

# # Add value labels above bars
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height + 2, str(int(height)), 
#              ha='center', va='bottom', fontsize=9)

# # Create legend
# legend_elements = [
#     Patch(facecolor=group_palette[i], label=list(relation_groups.keys())[i])
#     for i in range(len(group_palette))
# ]
# plt.legend(handles=legend_elements, title="Relation Groups", bbox_to_anchor=(1.05, 1), loc='upper left')

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd

freq_head = {
    "husband" : [7, 0],
    "wife" : [7, 0],
    "son-in-law" : [1, 1],
    "daughter-in-law" : [1, 1],
    "father-in-law" : [2, 2],
    "mother-in-law" : [2, 2],    
    "grandson" : [10, 6],   
    "granddaughter" : [10, 6],   
    "son" : [21, 4],   
    "daughter" : [21, 4],   
    "uncle" : [4, 2],    
    "aunt" : [4, 2],   
    "grandfather" : [8, 4],   
    "grandmother" : [8, 4],  
    "father" : [16, 4],  
    "mother" : [16, 4], 
    "nephew" : [2, 2], 
    "niece" : [2, 2], 
    "brother" : [22, 6], 
    "sister" : [22, 6]
}
# Convert to DataFrame
df = pd.DataFrame(freq_head, index=["frequency", "head_count"]).T
df = df.sort_values(by="frequency", ascending=True)

# Plot 1: Line graph
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["frequency"], marker='o', label='Frequency')
plt.plot(df.index, df["head_count"], marker='s', label='Head Count')
plt.xlabel("Relation")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()






