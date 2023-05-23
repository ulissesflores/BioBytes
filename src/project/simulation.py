"""
BioBytes Simulation Module

This module contains the simulation logic for the BioBytes project. It simulates a dynamic 
world where organisms move
randomly to adjacent cells while nutrients remain static. The simulation runs for 50 frames, 
with a 200-millisecond
delay between frames.

Usage:
- Create a World object with a specific size.
- Place organisms and nutrients in the world.
- Use the matplotlib.animation module to visualize and save the simulation as a GIF.

Classes:
- Organism: Represents an organism with a position and movement behavior.
- Nutrient: Represents a nutrient with a fixed position.
- World: Represents the world matrix and provides methods for placing organisms and nutrients 
  and moving organisms.

The simulation utilizes the matplotlib.animation module to create a GIF representation of the 
dynamic world. The choice of GIF format is motivated by its lightweight nature, making it easy 
to share and visualize the simulation without requiring external video players or codecs.

The animation is saved as a GIF file named 'animation.gif'. It is stored in the 'examples' 
directory, which is created within the same directory as this script. If the 'examples' 
directory already exists, the animation file will be saved within it. If it doesn't exist, 
the directory will be created.

To run the simulation, execute the script or import the module in your project.

Note: Make sure to have the required dependencies installed, such as numpy and matplotlib.

Author: Ulisses Flores - MV9 Sistemas

"""

import os
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class Organism:
    def __init__(self, position):
        self.position = position
    def move(self, world_size):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x, y = self.position
        x = (x + dx) % world_size[0]
        y = (y + dy) % world_size[1]
        self.position = (x, y)

class Nutrient:
    def __init__(self, position):
        self.position = position

class World:
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros(self.size, dtype=np.uint8)
        self.organisms = []

    def place_organisms(self, organisms):
        self.organisms.extend(organisms)
        for organism in organisms:
            x, y = organism.position
            self.matrix[x, y] = 1

    def place_nutrients(self, nutrients):
        for nutrient in nutrients:
            x, y = nutrient.position
            self.matrix[x, y] = 2

    def move_organisms(self):
        for organism in self.organisms:
            old_position = organism.position
            organism.move(self.size)
            new_position = organism.position
            self.matrix[old_position] = 0  # clear old position
            self.matrix[new_position] = 1  # place organism at new position

# Define the size of the world
world_size = (100, 100)

# Create the world
world = World(world_size)

# Place some organisms in the world
num_organisms = int(world_size[0] * world_size[1] * 0.02)  # 2% of world size
organisms = []
for _ in range(num_organisms):
    position = random.randint(0, world_size[0] - 1), random.randint(0, world_size[1] - 1)
    organism = Organism(position)
    organisms.append(organism)
world.place_organisms(organisms)

# Place some nutrients in the world
num_nutrients = int(world_size[0] * world_size[1] * 0.01)  # 1% of world size
nutrients = []
for _ in range(num_nutrients):
    position = random.randint(0, world_size[0] - 1), random.randint(0, world_size[1] - 1)
    nutrient = Nutrient(position)
    nutrients.append(nutrient)
world.place_nutrients(nutrients)

# Create a color map to represent empty cells, organisms, and nutrients
cmap = plt.cm.colors.ListedColormap(['gray', 'black', 'green'])
bounds = [0, 1, 2, 3]
norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

# Create a plot to visualize the world
fig, ax = plt.subplots()
im = ax.imshow(world.matrix, cmap=cmap, norm=norm)

# Update function for the animation
def update(frame):
    world.move_organisms()
    im.set_array(world.matrix)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=200, blit=False)

# Save the animation as a GIF
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'examples'))
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_file = os.path.join(OUTPUT_DIR, "animation.gif")
ani.save(output_file, writer='pillow')


# Show the plot
plt.show()
