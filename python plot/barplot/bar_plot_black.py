# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:06:10 2024

@author: Zirui Zhang
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:07:14 2024

@author: Zirui Zhang
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read data
data = pd.read_csv('./Feedback_18.csv') 

# Extract data
conditions = ['Novelty', 'Familiar', 'Very Familiar','City vs Office']
values = [data[col].mean() for col in conditions]  # Example: mean of each column
errors = [data[col].sem() for col in conditions]   # Example: standard deviation for error bars

# Create the plot with a specified figure size
fig, ax = plt.subplots(figsize=(8, 6))  # Width of 10 inches and height of 6 inches
fig.set_facecolor('black')
# Define custom color palette and alpha values
#custom_palette = ["#00CCCC", '#2141FF', '#2141FF', '#2141FF', '#2141FF', '#2141FF', '#2141FF', '#2141FF']
custom_palette = ["#04B05E", '#f1b3a9', '#0fc5e3','#2141FF']

alphas = [0.8 for i in range(4)]
alphass = [1 for i in range(4)]
# Plot bars
bar_plot = sns.barplot(x=conditions, y=values, palette=custom_palette, width=0.4, ax=ax, ci=None)
for bar, alpha in zip(ax.patches, alphas):
    bar.set_alpha(alpha)
# Add error bars manually
for i, (value, error, alpha) in enumerate(zip(values, errors, alphass)):
    # Add error bars with the same color as the bars but different transparency
    ax.errorbar(x=i, y=value, yerr=error, fmt='', color=custom_palette[i], alpha=alpha, capsize=5, capthick=2, elinewidth=2)

# Set the title and labels
ax.set_title('Scanning behaviour results', fontsize=18, pad=20)
ax.set_ylabel('Accuracy Percentage (%)', fontsize=15)

# Format y-axis as percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x * 100)}%'))

# Set y-axis limits (0 to 100%)
ax.set_ylim(0.3, 0.7)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')


ax.set_facecolor("black")
ax.set_title('Feedback V1 image category decoding', fontsize=18, pad=20, color = 'white')
ax.set_ylabel('Accuracy Percentage (%)', fontsize=15, color = 'white')
# Adjust the layout to make room for the title and labels


# Save and show plot
plt.savefig('feedback_accuracy.png', dpi=300)
plt.show()