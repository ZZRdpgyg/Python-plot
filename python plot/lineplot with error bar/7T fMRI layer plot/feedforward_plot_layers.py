# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:22:09 2024

@author: Zirui Zhang
"""

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
#RH_V1_0p1
#RH_V1_0p26
#RH_V1_0p42
#RH_V1_0p58
#RH_V1_0p74
#RH_V1_0p9

# Read data
data = pd.read_csv('./Feedforward_layers.csv') 

Conditions = ['10%','26%','42%','58%','74%','90%']
# Extract data
N_conditions = ['N_RH_V1_0p1', 'N_RH_V1_0p26', 'N_RH_V1_0p42','N_RH_V1_0p58','N_RH_V1_0p74','N_RH_V1_0p9']
Nov_values = [data[col].mean() for col in N_conditions]  # Example: mean of each column
Nov_errors = [data[col].sem() for col in N_conditions]   # Example: standard deviation for error bars

F_conditions = ['F_RH_V1_0p1', 'F_RH_V1_0p26', 'F_RH_V1_0p42','F_RH_V1_0p58','F_RH_V1_0p74','F_RH_V1_0p9']
Fam_values = [data[col].mean() for col in F_conditions]  # Example: mean of each column
Fam_errors = [data[col].sem() for col in F_conditions]   # Example: standard deviation for error bars

V_conditions = ['V_RH_V1_0p1', 'V_RH_V1_0p26', 'V_RH_V1_0p42','V_RH_V1_0p58','V_RH_V1_0p74','V_RH_V1_0p9']
Vfa_values = [data[col].mean() for col in V_conditions]  # Example: mean of each column
Vfa_errors = [data[col].sem() for col in V_conditions]   # Example: standard deviation for error bars

# Create the plot with a specified figure size
fig, ax = plt.subplots(figsize=(8, 6))  # Width of 10 inches and height of 6 inches
fig.set_facecolor('black')
# Define custom color palette and alpha values


alphas = [1 for i in range(6)]
alphass = [1 for i in range(6)]
N_custom_color = "#04B05E"  # Green
F_custom_color = "#f1b3a9"  # Pink
V_custom_color = "#0fc5e3"  # Cyan

# Plot bars with custom colors
Nov_plot = sns.lineplot(x=Conditions, y=Nov_values, color=N_custom_color, ax=ax, ci=None, linewidth=4,label="Novelty",linestyle='dashed')

# Add error bars manually
for i, (value, error, alpha) in enumerate(zip(Nov_values, Nov_errors, alphas)):
    ax.errorbar(x=i, y=value, yerr=error, fmt='', color=N_custom_color, alpha=alpha, capsize=5, capthick=2, elinewidth=4)

Fam_plot = sns.lineplot(x=Conditions, y=Fam_values, color=F_custom_color, ax=ax, ci=None, linewidth=4,label="Familiar",linestyle='dashed')

# Add error bars manually
for i, (value, error, alpha) in enumerate(zip(Fam_values, Fam_errors, alphas)):
    ax.errorbar(x=i, y=value, yerr=error, fmt='', color=F_custom_color, alpha=alpha, capsize=5, capthick=2, elinewidth=4)

Vfa_plot = sns.lineplot(x=Conditions, y=Vfa_values, color=V_custom_color, ax=ax, ci=None, linewidth=4,label="Very Familiar",linestyle='dashed')

# Add error bars manually
for i, (value, error, alpha) in enumerate(zip(Vfa_values, Vfa_errors, alphas)):
    ax.errorbar(x=i, y=value, yerr=error, fmt='', color = V_custom_color, alpha=alpha, capsize=5, capthick=2, elinewidth=4)
    
legend = ax.legend(facecolor='black', edgecolor='white', fontsize=10, title_fontsize=12)
plt.setp(legend.get_texts(), color='white')  # Set the color of the text to white
plt.setp(legend.get_title(), color='white')  # Set the color of the title to white

   



# Format y-axis as percentage
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x * 100)}%'))

# Set y-axis limits (0 to 100%)
ax.set_ylim(0.4, 0.7)

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

# Set the title and labels
ax.set_facecolor("black")
ax.set_title('Feedforward V1 layers image category decoding', fontsize=18, pad=20, color = 'white')
ax.set_ylabel('Accuracy Percentage (%)', fontsize=15, color = 'white')
# Adjust the layout to make room for the title and labels


# Save and show plot
plt.savefig('Feedforward_layers_accuracy.png', dpi=300)
plt.show()


#........................................plot City vs Office..............................
C_conditions = ['C_RH_V1_0p1', 'C_RH_V1_0p26', 'C_RH_V1_0p42','C_RH_V1_0p58','C_RH_V1_0p74','C_RH_V1_0p9']
CO_values = [data[col].mean() for col in C_conditions]  # Example: mean of each column
CO_errors = [data[col].sem() for col in C_conditions]   # Example: standard deviation for error bars

fig1, axx = plt.subplots(figsize=(8, 6))  # Width of 10 inches and height of 6 inches
fig1.set_facecolor('black')
# Define custom color palette and alpha values


alphas = [1 for i in range(6)]
alphass = [1 for i in range(6)]
C_custom_color = '#FDFDFD'


# Plot bars with custom colors
CO_plot = sns.lineplot(x=Conditions, y= CO_values, color=C_custom_color, ax=axx, ci=None, linewidth=4,label="City vs Office",linestyle='dashed')

# Add error bars manually
for i, (value, error, alpha) in enumerate(zip(CO_values, CO_errors, alphas)):
    axx.errorbar(x=i, y=value, yerr=error, fmt='', color=C_custom_color, alpha=alpha, capsize=5, capthick=2, elinewidth=4)

    
legend = axx.legend(facecolor='black', edgecolor='white', fontsize=10, title_fontsize=12)
plt.setp(legend.get_texts(), color='white')  # Set the color of the text to white
plt.setp(legend.get_title(), color='white')  # Set the color of the title to white

   



# Format y-axis as percentage
axx.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x * 100)}%'))

# Set y-axis limits (0 to 100%)
axx.set_ylim(0.4, 0.7)

# Hide the right and top spines
axx.spines['right'].set_visible(False)
axx.spines['top'].set_visible(False)

axx.tick_params(axis='x', colors='white')
axx.tick_params(axis='y', colors='white')

axx.spines['bottom'].set_color('white')
axx.spines['top'].set_color('white')
axx.spines['right'].set_color('white')
axx.spines['left'].set_color('white')
axx.spines['bottom'].set_color('white')

# Set the title and labels
axx.set_facecolor("black")
axx.set_title('Feedforward V1 layers overall City vs Office', fontsize=18, pad=20, color = 'white')
axx.set_ylabel('Accuracy Percentage (%)', fontsize=15, color = 'white')
# Adjust the layout to make room for the title and labels


# Save and show plot
plt.savefig('City_vs_Office_Feedforward_layers_accuracy.png', dpi=300)
plt.show()