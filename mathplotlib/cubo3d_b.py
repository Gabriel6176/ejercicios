import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import mplcursors
import matplotlib.patches as patches

# Define data for the cubes
datos = [
    {'nombre': 'Cobertura Pública', 'x': 60, 'y': 36.9, 'z': 90},
    {'nombre': 'PAMI', 'x': 75, 'y': 9.6, 'z': 80},
    {'nombre': 'Obras Sociales Nacionales', 'x': 75, 'y': 27.6, 'z': 70},
    {'nombre': 'Medicina Prepaga', 'x': 85, 'y': 12.6, 'z': 50}
]

# Define colors for the cubes (you can customize these)
colores = ['red', 'green', 'blue', 'yellow']

# Create a figure and subplots (2x2 grid)
fig, axes = plt.subplots(2, 2, figsize=(12, 12), subplot_kw={'projection': '3d'})
axes = axes.flatten()  # Flatten the subplots into a 1D array

# Iterate over data and create cubes in separate subplots
for i, dato in enumerate(datos):
    # Define vertices and faces (unchanged)
    vertices = np.array([
        [0, 0, 0],
        [dato['x'], 0, 0],
        [dato['x'], dato['y'], 0],
        [0, dato['y'], 0],
        [0, 0, dato['z']],
        [dato['x'], 0, dato['z']],
        [dato['x'], dato['y'], dato['z']],
        [0, dato['y'], dato['z']]
    ])

    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 4, 5, 1],
        [1, 5, 6, 2],
        [2, 6, 7, 3],
        [0, 3, 7, 4]
    ]


    # Create the cube
    poly3d = [[vertices[vertex] for vertex in face] for face in faces]
    axes[i].add_collection3d(Poly3DCollection(poly3d, facecolors=colores[i], linewidths=1, edgecolors='black', alpha=0.5))

    # Ajustar la vista y etiquetas (opcional)
    for ax in axes:
        ax.view_init(90, 45)  # Ángulos de visión ajustados para una vista más lateral
        ax.set_xlabel('Servicios Cubiertos')
        ax.set_ylabel('Población Cubierta')
        ax.set_zlabel('Participación de los Gastos y Cuotas')

    # Set limits for each subplot (you can adjust these)
    #axes[i].set_xlim(0, 100)
    axes[i].set_xlim(100, 0)  # Set maximum at 0 and minimum at 100
    axes[i].set_ylim(100, 0)
    axes[i].set_zlim(0, 100)
    axes[i].set_title(dato['nombre'])  # Title for each subplot

# Adjust viewing angle for all subplots
for ax in axes:
    ax.view_init(30, 45)  # Change these values for different viewing angles


plt.tight_layout()
plt.show()
