import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style='ticks', rc={"axes.facecolor": "none", "legend.frameon": True})
sns.set_context('talk')

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

# Generate a network with high heterogeneity
network1 = nx.barabasi_albert_graph(n=1000, m=10)

# Generate a network with low heterogeneity
network2 = nx.erdos_renyi_graph(n=1000, p=0.05)

# Calculate degree distribution for each network
degree_dist1 = [d for n, d in network1.degree()]
degree_dist2 = [d for n, d in network2.degree()]

# Plot degree distribution
fig, ax = plt.subplots()
fig, ax = plt.subplots()
n_bins = 30
hist1, bin_edges1, _ = plt.hist(degree_dist1, bins=n_bins, alpha=0.8, label='High heterogeneity', edgecolor='none')
hist2, bin_edges2, _ = plt.hist(degree_dist2, bins=n_bins, alpha=0.8, label='Low heterogeneity', edgecolor='none')
plt.xlabel('Degree distribution')
plt.ylabel('Frequency')
plt.legend(facecolor='none', framealpha=1, edgecolor='white', labelcolor="white")

# Set the x and y axis labels to white
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Set the color of the axis ticks and tick labels
ax.tick_params(colors='white')

# Set the color of the bottom and left spines to white
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
# Remove the top and right spines
sns.despine()

# Add text in the right top corner
plt.text(0.98, 0.7, f"n={1000}", transform=ax.transAxes,
         fontsize=12, ha='right', va='top', color='white')

# Add a line connecting the midpoints of the bins
bin_centers1 = (bin_edges1[:-1] + bin_edges1[1:]) / 2
bin_centers2 = (bin_edges2[:-1] + bin_edges2[1:]) / 2
width = bin_centers1[1] - bin_centers1[0]
plt.plot(bin_centers1, hist1, color='blue', linewidth=2)
plt.plot(bin_centers2, hist2, color='orange', linewidth=2)

# save
plt.savefig('figures/heterogeneity.png', dpi=300, bbox_inches='tight', transparent=True)
plt.savefig('figures/heterogeneity.svg', bbox_inches='tight', transparent=True)


plt.show()
