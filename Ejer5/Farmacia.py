class Farmacia:
    def __init__(self, nombre="", sucursal=0, direccion=""):
        self.nombreFarmacia = nombre
        self.sucursal = sucursal
        self.direccion = direccion
        self.nroMedicamentos = 0
        self.m = []

    def leer(self):
        self.nombreFarmacia = input("Nombre de farmacia: ")
        self.sucursal = int(input("Sucursal: "))
        self.direccion = input("Dirección: ")

        self.nroMedicamentos = int(input("Cuántos medicamentos deseas registrar?: "))
        
        for i in range(self.nroMedicamentos):
            print(f"Medicamento {i+1}:")
            from Medicamento import Medicamento
            med = Medicamento()
            med.leer()
            self.m.append(med)

    def mostrar(self):
        print(f"\nFarmacia: {self.nombreFarmacia}  Sucursal: {self.sucursal}")
        print(f"Dirección: {self.direccion}")
        print("Medicamentos:")
        for med in self.m:
            med.mostrar()

    def getSucursal(self):
        return self.sucursal

    def getDireccion(self):
        return self.direccion

    def mostrarMedicamentos(self, tipoBuscado):
        for med in self.m:
            if med.tipo == tipoBuscado:
                med.mostrar()

    def buscaMedicamento(self, nombreBuscado):
        for med in self.m:
            if med.nombre.lower() == nombreBuscado.lower():
                return True
        return False
