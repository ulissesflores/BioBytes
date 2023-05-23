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
        """
        Move the organism to an adjacent cell within the world, avoiding collisions.

        The organism randomly selects a direction (up, down, left, or right) and attempts to move to the adjacent cell.
        However, it anticipates its trajectory for the next 10 blocks to avoid collisions with the map boundaries or other organisms.
        If a collision is detected, the organism adjusts its route to avoid the collision, choosing the next available cell in the desired direction.

        Args:
            world_size (tuple): The size of the world as a tuple (width, height).

        Returns:
            None
        """
        dx, dy = self._choose_direction()
        x, y = self.position
        new_x = x + dx
        new_y = y + dy

        # Check if the next position is within the boundaries of the world
        new_x = max(0, min(new_x, world_size[0] - 1))
        new_y = max(0, min(new_y, world_size[1] - 1))

        # Check if the next position collides with other organisms
        for organism in organisms:
            if (new_x, new_y) == organism.position:
                # Collision with another organism detected
                self._adjust_route(world_size, organisms)
                return

        self.position = (new_x, new_y)


    def _choose_direction(self):
        """
        Choose a random direction.

        Returns:
            tuple: The chosen direction as a tuple (dx, dy).
        """
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

    def _simulate_trajectory(self, world_size, steps=10):
        """
        Simulate the organism's trajectory for the next steps.

        Args:
            world_size (tuple): The size of the world as a tuple (width, height).
            steps (int): The number of steps to simulate.

        Returns:
            list: The list of simulated positions.
        """
        positions = [self.position]
        x, y = self.position

        for _ in range(steps):
            dx, dy = self._choose_direction()
            x += dx
            y += dy

            # Check if the simulated position is within the boundaries of the world
            x = max(0, min(x, world_size[0] - 1))
            y = max(0, min(y, world_size[1] - 1))

            positions.append((x, y))

        return positions

    def check_collision(self, world_size, organisms):
        """
        Check for collisions with the map boundaries or other organisms.

        The organism simulates its trajectory for the next 10 steps and checks if there are any collisions with the map boundaries or other organisms.
        If a collision is detected, the organism adjusts its route to avoid the collision, choosing the next available cell in the desired direction.

        Args:
            world_size (tuple): The size of the world as a tuple (width, height).
            organisms (list): List of other organisms in the world.

        Returns:
            None
        """
        trajectory = self._simulate_trajectory(world_size)

        for position in trajectory[1:]:
            if position[0] == 0 or position[0] == world_size[0] - 1 or position[1] == 0 or position[1] == world_size[1] - 1:
                # Collision with the map boundary detected
                self._adjust_route(world_size, organisms)
                break

            for organism in organisms:
                if position == organism.position:
                    # Collision with another organism detected
                    self._adjust_route(world_size, organisms)
                    break

    def _adjust_route(self, world_size, organisms):
        """
        Adjust the organism's route to avoid collisions.

        The organism tries all possible directions until it finds a cell that doesn't lead to a collision.

        Args:
            world_size (tuple): The size of the world as a tuple (width, height).
            organisms (list): List of other organisms in the world.

        Returns:
            None
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # up, down, right, left
        random.shuffle(directions)  # to choose a random direction

        x, y = self.position

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            # Check if the next position is within the boundaries of the world
            new_x = max(0, min(new_x, world_size[0] - 1))
            new_y = max(0, min(new_y, world_size[1] - 1))

            # Check if the next position collides with other organisms
            if not any(o.position == (new_x, new_y) for o in organisms):
                self.position = (new_x, new_y)
                break  # No collision with other organisms



class Nutrient:
    def __init__(self, position):
        self.position = position


class World:
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((self.size[0] + 2, self.size[1] + 2), dtype=np.uint8)

        
        self.organisms = []

    def place_organisms(self, organisms):
        self.organisms.extend(organisms)
        for organism in organisms:
            x, y = organism.position
            self.matrix[x + 1, y + 1] = 1

    def place_nutrients(self, nutrients):
        for nutrient in nutrients:
            x, y = nutrient.position
            self.matrix[x + 1, y + 1] = 2

    def move_organisms(self):
        for organism in self.organisms:
            old_position = organism.position
            organism.check_collision(self.size, self.organisms)
            new_position = organism.position

            new_x = min(new_position[0], self.size[0])  # limit the maximum x-coordinate
            new_y = min(new_position[1], self.size[1])  # limit the maximum y-coordinate

            self.matrix[old_position[0] + 1, old_position[1] + 1] = 0  # clear old position
            self.matrix[new_x + 1, new_y + 1] = 1  # place organism at new position





# Define the size of the world
world_size = (110, 110)

# Create the world
world = World(world_size)

# Place some organisms in the world
num_organisms = int(world_size[0] * world_size[1] * 0.02)  # 2% of world size
organisms = []
for _ in range(num_organisms):
    position = random.randint(0, world_size[0] - 2), random.randint(0, world_size[1] - 2)
    organism = Organism(position)
    organisms.append(organism)
world.place_organisms(organisms)

# Place some nutrients in the world
num_nutrients = int(world_size[0] * world_size[1] * 0.01)  # 1% of world size
nutrients = []
for _ in range(num_nutrients):
    position = random.randint(0, world_size[0] - 2), random.randint(0, world_size[1] - 2)
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
ani = animation.FuncAnimation(fig, update, frames=200, interval=200, blit=False)

# Save the animation as a GIF
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'examples'))
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_file = os.path.join(OUTPUT_DIR, "animation.gif")
ani.save(output_file, writer='pillow')

# Show the plot
plt.show()
