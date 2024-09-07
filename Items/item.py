# item.py
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, description):
        """
        Initialize a generic item.
        
        :param name: The item's name
        :param description: A brief description of the item
        """
        self.name = name
        self.description = description

    @abstractmethod
    def use(self, player):
        """
        Abstract method to define how the item is used.
        This must be implemented by any subclass.
        """
        pass

    def __str__(self):
        return f"{self.name}: {self.description}"
