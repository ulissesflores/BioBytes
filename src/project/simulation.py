"""
Module: simulation.py

This module contains the simulation logic for the BioBytes project.

Este módulo contém a lógica de simulação para o projeto BioBytes.
"""

import os
import random

import matplotlib.pyplot as plt
from matplotlib import animation

from classes.world import World
from classes.organism import Organism
from classes.nutrient import Nutrient

# Define the size of the world
world_size = (50, 50)

# Create the world
world = World(world_size)

# Place some organisms in the world
num_organisms = random.randint(900, 1800)  # Random number of organisms
organisms = []
for _ in range(num_organisms):
    x = random.randint(0, world_size[0] - 1)
    y = random.randint(0, world_size[1] - 1)
    organism = Organism((x, y))
    organisms.append(organism)
    world.place_organisms([organism.position])

def generate_nutrients(world):
    """Generate nutrients in the world."""
    max_nutrients = int(num_organisms * 0.07)  # Generate nutrients up to 7% of the organism population
    num_nutrients = random.randint(0, max_nutrients)
    for _ in range(num_nutrients):
        x = random.randint(0, world_size[0] - 1)
        y = random.randint(0, world_size[1] - 1)
        nutrient = Nutrient((x, y))
        world.place_organisms([nutrient.position])

def update(frame):
    """Update function for animation."""
    global world, organisms

    # Move each organism
    for organism in organisms:
        organism.move(world.size)

    # Generate nutrients
    generate_nutrients(world)

    # Update the animation image
    im.set_array(world.matrix)

# Create a color map to represent organisms and nutrients
cmap = plt.cm.colors.ListedColormap(['white', 'red', 'brown'])
bounds = [0, 1, 2, 3]
norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

# Create the initial image for the animation
im = plt.imshow(world.matrix, animated=True, cmap=cmap, norm=norm)

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), update, frames=range(50), interval=200)

# Add a colorbar
plt.colorbar(ticks=[0.5, 1.5, 2.5], boundaries=[0, 1, 2, 3], label='0: Empty, 1: Organism, 2: Nutrient')

# Save the animation as a GIF file
OUTPUT_DIR = "../examples"
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_file = os.path.join(OUTPUT_DIR, "animation.gif")
ani.save(output_file, writer='pillow')

# Render the animation
plt.show()
