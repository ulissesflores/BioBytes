"""
This module contains the Nutrient class, which represents a nutrient in the simulation.

O módulo contém a classe Nutrient, que representa um nutriente na simulação.

The Nutrient class provides functionalities to manage and interact with individual nutrients.
It allows performing operations related to nutrients.

A classe Nutrient fornece funcionalidades para gerenciar e interagir com nutrientes individuais.
Ela permite executar operações relacionadas a nutrientes.

Attributes:
    position (tuple): The position of the nutrient.

Atributos:
    position (tuple): A posição do nutriente.

Methods:
    __init__(position: tuple) -> None:
        Initializes a new Nutrient instance.

Métodos:
    __init__(position: tuple) -> None:
        Inicializa uma nova instância da classe Nutrient.
"""

class Nutrient:
    """
    Represents a nutrient in the simulation.
    
    A classe Nutrient representa um nutriente na simulação.
    """

    def __init__(self, position):
        """
        Initializes a new Nutrient instance.
        
        Inicializa uma nova instância da classe Nutrient.

        Args:
            position (tuple): The position of the nutrient as a tuple (x, y).
                A posição do nutriente como uma tupla (x, y).
        """
        self.position = position
