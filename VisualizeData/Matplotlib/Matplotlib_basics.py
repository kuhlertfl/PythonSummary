# =============================================================================
# Matplotlib Data Sheet
# =============================================================================

# =============================================================================
# Import the Library
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

# A figure is the outer container for your plots. You can have multiple plots (subplots) within a single figure.
fig = plt.figure()

# =============================================================================
# Basic Plotting: Line Plot
# =============================================================================

# Line plots are used to display information as a series of data points connected by straight line segments.
# Use case: When you want to show a trend over time or location.

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()

# =============================================================================
# Customizing the Plot
# =============================================================================

# Explanation: Adding labels and a title makes the plot more informative and readable.

plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()

# =============================================================================
# Multiple Plots and Colors
# =============================================================================

# Explanation: Multiple data sets can be plotted on the same graph. Legends help in distinguishing between different datasets.

plt.plot([1, 2, 3], [1, 4, 9], label='Line 1')
plt.plot([1, 2, 3], [1, 2, 3], label='Line 2')
plt.legend()
plt.show()

# =============================================================================
# Scatter Plot
# =============================================================================

# Explanation: Scatter plots display individual data points. They are good for showing the distribution or clustering of data.
# Use case: When you want to check for correlations or outliers in your data.

plt.scatter([1, 2, 3], [1, 4, 9])
plt.show()

# =============================================================================
# Bar Chart
# =============================================================================

# Explanation: Bar charts represent categorical data with rectangular bars.
# Use case: Comparing quantities of different categories.

plt.bar([1, 2, 3], [1, 4, 9])
plt.show()

# =============================================================================
# Subplots
# =============================================================================

# Explanation: Subplots allow you to place multiple plots in a single figure, organized in a grid.
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot([1, 2, 3], [1, 4, 9])
axs[1].plot([1, 2, 3], [1, 2, 3])
plt.show()

# =============================================================================
# 3D Plots
# =============================================================================

# Explanation: 3D plots are used to represent three-dimensional data.
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([1, 2, 3], [1, 2, 3], [1, 4, 9])
plt.show()

# =============================================================================
# Annotations
# =============================================================================

# Explanation: Annotations are used to add text notes or arrows at specific points in the plot.
plt.plot([1, 2, 3], [1, 4, 9])
plt.annotate('This is a point', xy=(2, 4), xytext=(2.5, 7), arrowprops=dict(arrowstyle='->'))
plt.show()

# =============================================================================
# Explanations and Use Cases
# =============================================================================

# 1. Basic Plotting: The most straightforward way to create a simple line plot.
# 2. Customizing the Plot: How to add labels, title, and grid to make the plot clearer.
# 3. Multiple Plots and Colors: Show multiple datasets in a single figure.
# 4. Scatter Plot: Good for showing the distribution or clustering of data.
# 5. Bar Chart: Used for comparing quantities of different categories.
# 6. Subplots: Place multiple plots in a single figure.
# 7. 3D Plots: For representing three-dimensional data.
# 8. Annotations: Add text notes or arrows at specific points in the plot.

# This should give you a comprehensive understanding of Matplotlib's capabilities, why certain plots are used, and how to customize them for your needs.
