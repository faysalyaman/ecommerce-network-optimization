import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/network_data.csv")

G = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='time')

start_node = "Depot"
end_node = "Levent"

shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='time')
shortest_time = nx.shortest_path_length(G, source=start_node, target=end_node, weight='time')

print("Shortest Path:", shortest_path)
print("Total Time:", shortest_time, "minutes")

pos = nx.spring_layout(G)

plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)

labels = nx.get_edge_attributes(G, 'time')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("E-commerce Delivery Network")
plt.savefig("../results/network_visualization.png")
plt.show()
