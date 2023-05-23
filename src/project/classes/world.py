"""
This module contains the World class, which represents the world of the simulation.

The World class provides functionalities to manage and interact with the simulation's world.
It allows placing organisms, moving organisms, clearing the world, and generating nutrients.

The world is represented by a matrix, where each element represents a specific state 
or entity in the world.

Attributes:
    size (tuple): The size of the world as a tuple (width, height).
    matrix (ndarray): The matrix representing the world.

Methods:
    __init__(size: tuple) -> None:
        Initializes a new World instance.
    place_organisms(organisms: list) -> None:
        Places organisms in the world.
    move_organisms() -> None:
        Move organisms in the world.
    clear() -> None:
        Clears the world.
    generate_nutrients() -> None:
        Generates nutrients in the world.
"""

import random
import numpy as np


class World:
    """
    Represents the world of the simulation.

    A class that manages the world of the simulation. 
    It provides functionalities for placing organisms,
    moving organisms, and clearing the world.
    """

    def __init__(self, size):
        """
        Initializes a new World instance.

        Args:
            size (tuple): The size of the world as a tuple (width, height).
        """
        self.size = size
        self.matrix = np.zeros(self.size)
        self.organisms = []

    def place_organisms(self, organisms):
        """
        Places organisms in the world.

        Args:
            organisms (list): List of Organism objects.
        """
        self.organisms.extend(organisms)
        for organism in organisms:
            x, y = organism.position
            self.matrix[x, y] = 1

    def move_organisms(self):
        """
        Move organisms in the world.

        Randomly moves organisms to adjacent cells (up, right, down, or left).
        Updates the position of each organism and the world matrix accordingly.
        """
        for organism in self.organisms:
            x, y = organism.position
            direction = random.randint(0, 3)

            if direction == 0:  # Up
                y -= 1
            elif direction == 1:  # Right
                x += 1
            elif direction == 2:  # Down
                y += 1
            elif direction == 3:  # Left
                x -= 1

            if 0 <= x < self.size[0] and 0 <= y < self.size[1]:
                organism.position = (x, y)
                self.matrix[x, y] = 1
            else:
                self.organisms.remove(organism)

    def clear(self):
        """
        Clears the world.

        Resets the world matrix to all zeros.
        """
        self.matrix = np.zeros(self.size)
