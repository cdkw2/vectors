import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Input i, j, k components
i = float(input("Enter i component: "))
j = float(input("Enter j component: "))
k = float(input("Enter k component: "))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define origin and vector
origin = np.array([0, 0, 0])
vector = np.array([i, j, k])

# Plot the vector
ax.quiver(*origin, *vector, color='b', linewidth=1)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits
ax.set_xlim([0, max(abs(i), 5)])
ax.set_ylim([0, max(abs(j), 5)])
ax.set_zlim([0, max(abs(k), 5)])

# Make the plot interactive
mplcursors.cursor(hover=True)

# Show the plot
plt.show()
