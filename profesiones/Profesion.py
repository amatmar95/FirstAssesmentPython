
from abc import ABC, abstractmethod

class Profesion(ABC):
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area

    @abstractmethod
    def descripcion(self):
        pass

class Abogado(Profesion):
    def __init__(self, nombre, area, especialidad):
        super().__init__(nombre, area)
        self.especialidad = especialidad

    def descripcion(self):
        return f"El abogado {self.nombre} es especialista en {self.especialidad}, dentro del área de {self.area}."
    
class Medico(Profesion):
    def __init__(self, nombre, area, especialidad):
        super().__init__(nombre, area)
        self.especialidad = especialidad

    def descripcion(self):
        return f"El médico {self.nombre} es especialista en {self.especialidad}, dentro del área de {self.area}."

class Ingeniero(Profesion):
    def __init__(self, nombre, area, especialidad):
        super().__init__(nombre, area)
        self.especialidad = especialidad

    def descripcion(self):
        return f"El ingeniero {self.nombre} es especialista en {self.especialidad}, dentro del área de {self.area}."
