class Trabajador:
    def __init__(self, nombre, carnet, salario):
        self.nombre = nombre
        self.carnet = carnet
        self.salario = salario

    def mostrar(self):
        return f"{self.nombre}  CI:{self.carnet}  Salario:{self.salario}"
