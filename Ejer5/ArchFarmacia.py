import pickle

class ArchFarmacia:
    def __init__(self, nombreArch):
        self.na = nombreArch

    def crearArchivo(self):
        with open(self.na, "wb") as f:
            pass

    def adicionar(self, farmacia):
        with open(self.na, "ab") as f:
            pickle.dump(farmacia, f)

    def listar(self):
        try:
            with open(self.na, "rb") as f:
                print("\nListado de Farmacias:")
                while True:
                    obj = pickle.load(f)
                    obj.mostrar()
        except EOFError:
            pass
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def mostrarMedicamentosResfrios(self):
        try:
            with open(self.na, "rb") as f:
                while True:
                    obj = pickle.load(f)
                    print(f"\nSucursal {obj.sucursal}: Medicamentos para resfrío")
                    obj.mostrarMedicamentos("resfrio")
        except:
            pass

    def precioMedicamentoTos(self):
        total = 0
        try:
            with open(self.na, "rb") as f:
                while True:
                    obj = pickle.load(f)
                    for m in obj.m:
                        if m.tipo == "tos":
                            total += m.precio
        except:
            pass
        return total

    def mostrarMedicamentosMenorTos(self):
        menor = None
        try:
            with open(self.na, "rb") as f:
                while True:
                    obj = pickle.load(f)
                    for m in obj.m:
                        if m.tipo == "tos":
                            if menor is None or m.precio < menor:
                                menor = m
        except:
            pass
        
        if menor:
            print("\nMedicamento para la tos más barato:")
            menor.mostrar()
