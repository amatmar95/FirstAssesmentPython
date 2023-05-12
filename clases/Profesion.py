
from abc import ABC, abstractmethod

class Profesion(ABC):
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    @abstractmethod
    def descripcion(self):
        pass