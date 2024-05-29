import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

# Create the bar plot
fig, ax = plt.subplots()
bars = ax.bar(categories, values)

# Add labels to each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

# Show the plot
plt.show()