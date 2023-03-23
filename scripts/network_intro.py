import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style='ticks', rc={"axes.facecolor": "none", "legend.frameon": True})
sns.set_context('talk')

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

# Generate a random graph with 100 nodes and preferential attachment
G = nx.barabasi_albert_graph(25, 2)

# Set node color to blue
node_color = 'blue'

# Draw the graph with blue nodes
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=node_color)
nx.draw_networkx_edges(G, pos)
plt.axis('off')

# save
plt.savefig('figures/network_intro.png', dpi=300, bbox_inches='tight', transparent=True)
plt.savefig('figures/network_intro.svg', bbox_inches='tight', transparent=True)

plt.show()
