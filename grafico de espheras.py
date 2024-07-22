import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data for variables
variables = {
    'x': np.array([2, 3, 4]),
    'y': np.array([2, 3, 4]),
    'z': np.array([2, 3, 4]),
    'size': np.array([500, 1100, 1050])  # Size of each sphere
}

# Ensure that the size array has the same length as the coordinate arrays
size_array_length = len(variables['size'])
for var, values in variables.items():
    if var != 'size' and len(values) != size_array_length:
        raise ValueError("Size array must have the same length as coordinate arrays.")

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a sphere for each variable
for i in range(size_array_length):
    ax.scatter(variables['x'][i], variables['y'][i], variables['z'][i], s=variables['size'][i], label=f"Sphere {i}")

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()



