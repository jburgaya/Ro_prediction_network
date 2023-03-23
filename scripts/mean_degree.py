import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style='ticks', rc={"axes.facecolor": "none", "legend.frameon": True})
sns.set_context('talk')

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

# Generate a network with high mean degree distribution
high_degree_network = nx.powerlaw_cluster_graph(n=25, m=5, p=0.1)

# Generate a network with low mean degree distribution
low_degree_network = nx.erdos_renyi_graph(n=25, p=0.05)

# Set node colors and alpha values for the two networks
high_degree_colors = ['blue']*len(high_degree_network.nodes())
high_degree_alphas = [0.8]*len(high_degree_network.nodes())

low_degree_colors = ['orange']*len(low_degree_network.nodes())
low_degree_alphas = [0.8]*len(low_degree_network.nodes())

# Plot the two networks
plt.subplot(121)
nx.draw(high_degree_network, node_size=50, node_color=high_degree_colors, alpha=high_degree_alphas, edge_color="white", width=0.5)
plt.title("High dd", color="white")

plt.subplot(122)
nx.draw(low_degree_network, node_size=50, node_color=low_degree_colors, alpha=low_degree_alphas, edge_color="white", width=0.5)
plt.title("Low dd", color="white")

# Add text in the right top corner
plt.text(0.98, 0.98, f"n={25}", fontsize=12, ha='right', va='top', color='white')

# save
plt.savefig('figures/mean_dd.png', dpi=300, bbox_inches='tight', transparent=True)
plt.savefig('figures/mean_dd.svg', bbox_inches='tight', transparent=True)

plt.show()
