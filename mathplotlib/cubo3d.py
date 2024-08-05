import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Definimos los colores
colores = ['blue', 'green', 'red', 'purple']

# Definimos los datos de los cubos
datos = [
    {'nombre': 'Cobertura Publica', 'x': 36.9, 'y': 90, 'z': 70},
    {'nombre': 'PAMI', 'x': 9.6, 'y': 80, 'z': 75},
    {'nombre': 'Obras Sociales Nacionales', 'x': 27.6, 'y': 70, 'z': 70},
    {'nombre': 'Medicina Prepaga', 'x': 12.6, 'y': 50, 'z': 85}
]

# Creamos la figura y el subplot en 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Iteramos sobre los datos y creamos los cubos
for i, dato in enumerate(datos):
    # Definimos los vértices del cubo
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

    # Definimos las caras del cubo
    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 4, 5, 1],
        [1, 5, 6, 2],
        [2, 6, 7, 3],
        [0, 3, 7, 4]
    ]

    # Creamos las caras del cubo
    poly3d = [[vertices[vertex] for vertex in face] for face in faces]
    #poly3d = [[vertices[vertex] for vertex in faces[i]]]  # Use 'faces' here
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors=colores[i], linewidths=1, edgecolors='black', alpha=0.5))

# Set limits manually
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_zlim(0, 100)

# Mostramos el gráfico
plt.show()
