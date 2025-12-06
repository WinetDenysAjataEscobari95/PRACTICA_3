class Medicamento:
    def __init__(self, nombre="", cod=0, tipo="", precio=0.0):
        self.nombre = nombre
        self.codMedicamento = cod
        self.tipo = tipo
        self.precio = precio

    def leer(self):
        self.nombre = input("Nombre del medicamento: ")
        self.codMedicamento = int(input("Código: "))
        self.tipo = input("Tipo (tos, resfrio, gripe, etc): ")
        self.precio = float(input("Precio: "))

    def mostrar(self):
        print(f"{self.nombre} - Código: {self.codMedicamento} - Tipo: {self.tipo} - Precio: {self.precio}")

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio
