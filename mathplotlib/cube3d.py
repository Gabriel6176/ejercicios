import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define vertices of the cube with a length of 100 units
def get_cube_vertices(x, y, z, size):
    r = [0, size]
    vertices = [[x + a, y + b, z + c] for a in r for b in r for c in r]
    return np.array(vertices)

# Define the faces of the cube using vertex indices
def get_cube_faces():
    return [
        [0, 1, 5, 4],  # Face 1 (bottom)
        [1, 2, 6, 5],  # Face 2 (side)
        [2, 3, 7, 6],  # Face 3 (top)
        [3, 0, 4, 7],  # Face 4 (side)
        [4, 5, 6, 7],  # Face 5 (back)
        [0, 1, 2, 3]   # Face 6 (front)
    ]

# Create the plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the size of the cube
size = 100
x, y, z = 0, 0, 0

# Get the vertices and faces
vertices = get_cube_vertices(x, y, z, size)
faces = get_cube_faces()

# Plot each face of the cube
for face in faces:
    poly3d = [[vertices[vertice] for vertice in face]]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

# Set the plot limits
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_xlim(x, size + x)
ax.set_ylim(y, size + y)
ax.set_zlim(z, size + z)

plt.show()
