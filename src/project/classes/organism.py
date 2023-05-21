"""
This module contains the Organism class, which represents an organism in the simulation.

O módulo contém a classe Organism, que representa um organismo na simulação.

The Organism class provides functionalities to manage and interact with individual organisms.
It allows moving organisms within the world and performing other relevant operations.

A classe Organism fornece funcionalidades para gerenciar e interagir com organismos individuais.
Ela permite mover organismos dentro do mundo e executar outras operações relevantes.

An organism is represented by its position within the world.

Um organismo é representado pela sua posição dentro do mundo.

Attributes:
    position (tuple): The position of the organism.

Atributos:
    position (tuple): A posição do organismo.

Methods:
    __init__(position: tuple) -> None:
        Initializes a new Organism instance.
    move(world_size: tuple) -> None:
        Moves the organism within the world.

Métodos:
    __init__(position: tuple) -> None:
        Inicializa uma nova instância da classe Organism.
    move(world_size: tuple) -> None:
        Move o organismo dentro do mundo.
"""
import random

class Organism:
    """
    Represents an organism in the simulation.
    
    A classe Organism representa um organismo na simulação.
    """

    def __init__(self, position):
        """
        Initializes a new Organism instance.
        
        Inicializa uma nova instância da classe Organism.

        Args:
            position (tuple): The position of the organism as a tuple (x, y).
                A posição do organismo como uma tupla (x, y).
        """
        self.position = position

    def move(self, world_size):
        """
        Moves the organism within the world.
        
        Move o organismo dentro do mundo.

        Args:
            world_size (tuple): The size of the world as a tuple (width, height).
                O tamanho do mundo como uma tupla (largura, altura).
        """
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x, y = self.position
        x = (x + dx) % world_size[0]
        y = (y + dy) % world_size[1]
        self.position = (x, y)  