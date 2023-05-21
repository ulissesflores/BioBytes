"""
This module contains the World class, which represents the world of the simulation.

O módulo contém a classe World, que representa o mundo da simulação.

The World class provides functionalities to manage and interact with the simulation's world.
It allows placing organisms, clearing the world, and performing other relevant operations.

A classe World fornece funcionalidades para gerenciar e interagir com o mundo da simulação.
Ela permite colocar organismos, limpar o mundo e executar outras operações relevantes.

The world is represented by a matrix, where each element represents 
a specific state or entity in the world.

O mundo é representado por uma matriz, 
onde cada elemento representa um estado ou entidade específica no mundo.

Attributes:
    size (tuple): The size of the world as a tuple (width, height).
    matrix (ndarray): The matrix representing the world.

Atributos:
    size (tuple): O tamanho do mundo como uma tupla (largura, altura).
    matrix (ndarray): A matriz que representa o mundo.

Methods:
    __init__(size: tuple) -> None:
        Initializes a new World instance.
    place_organisms(organisms: list) -> None:
        Places organisms in the world.
    clear() -> None:
        Clears the world.

Métodos:
    __init__(size: tuple) -> None:
        Inicializa uma nova instância da classe World.
    place_organisms(organisms: list) -> None:
        Coloca organismos no mundo.
    clear() -> None:
        Limpa o mundo.

"""

import numpy as np


class World:
    """
    Represents the world of the simulation.

    A classe World representa o mundo da simulação.
    """

    def __init__(self, size):
        """
        Initializes a new World instance.

        Inicializa uma nova instância da classe World.

        Args:
            size (tuple): The size of the world as a tuple (width, height).
                O tamanho do mundo como uma tupla (largura, altura).
        """
        self.size = size
        self.matrix = np.zeros(self.size)

    def place_organisms(self, organisms):
        """
        Places organisms in the world.

        Coloca organismos no mundo.

        Args:
            organisms (list): List of organism positions as tuples (x, y).
                Lista de posições dos organismos como tuplas (x, y).
        """
        for organism in organisms:
            self.matrix[organism] = 1

    def clear(self):
        """
        Clears the world.

        Limpa o mundo.
        """
        self.matrix = np.zeros(self.size)
