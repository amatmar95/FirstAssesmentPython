
class Medico(Profesion):
    def __init__(self, nombre, area, especialidad):
        super().__init__(nombre, area)
        self.especialidad = especialidad

    def descripcion(self):
        print(f"El médico {self.nombre} es especialista en {self.especialidad}, dentro del área de {self.area}.")
