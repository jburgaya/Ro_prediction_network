import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='ticks', rc={"axes.facecolor": "none", "legend.frameon": True})
sns.set_context('talk')

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

import numpy as np

# Define the values of Ro
Ro_values = [3, 4, 9, 17]

# Define the labels for each Ro value
labels = ["SARS-CoV-2", "Smallpox", "Mumps\nChickenpox", "Measles\nPertussis"]

# Compute the corresponding vaccination fractions
p_values = [1 - (1 / Ro) for Ro in Ro_values]

# Define the x values
x = np.arange(1, 21)

# Compute the vaccination fractions for the x values
p_x = [1 - (1 / xi) for xi in x]

# Create the plot
fig, ax = plt.subplots()

# Add the distribution of vaccination fractions along the x-axis
ax.plot(x, p_x)

# Add lines for the specific Ro values
for i in range(len(Ro_values)):
    Ro = Ro_values[i]
    p = p_values[i]
    ax.plot([Ro, Ro], [0, p], linestyle="--", color="gray")
    ax.plot([0, Ro], [p, p], linestyle="--", color="gray")
    ax.scatter(Ro, p, color="black")
    ax.annotate(labels[i], xy=(Ro, p), xytext=(Ro + 0.5, p + 0.02), bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# Set the title and axis labels
ax.set_xlabel("Basic Reproduction Number (Ro)")
ax.set_ylabel("Vaccination Fraction (p)")

# Set the x and y axis labels to white
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Set the x and y limits
ax.set_xlim([0, 20])
ax.set_ylim([0, 1])

# Set the color of the axis ticks and tick labels
ax.tick_params(colors='white')

# Set the color of the bottom and left spines to white
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
# Remove the top and right spines
sns.despine()

# Save
plt.savefig('vaccination_Ro.png', dpi=300, bbox_inches='tight', transparent=True)
plt.savefig('vaccination_Ro.svg', bbox_inches='tight', transparent=True)

# Show the plot
plt.show()
