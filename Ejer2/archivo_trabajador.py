class ArchivoTrabajador:
    def __init__(self, nombreArch):
        self.nombreArch = nombreArch

    def crearArchivo(self):
        f = open(self.nombreArch, "w")
        f.close()

    def guardarTrabajador(self, t):
        linea = f"{t.nombre},{t.carnet},{t.salario}\n"
        f = open(self.nombreArch, "a")
        f.write(linea)
        f.close()

    def aumentarSalario(self, monto, t):
        t.salario += monto
        return t.salario

    def trabajadorMayorSalario(self):
        f = open(self.nombreArch, "r")
        mayor = None
        for lin in f:
            nom, car, sal = lin.strip().split(",")
            sal = float(sal)
            if mayor is None or sal > mayor.salario:
                from trabajador import Trabajador
                mayor = Trabajador(nom, int(car), sal)
        f.close()
        return mayor

    def ordenarPorSalario(self):
        f = open(self.nombreArch, "r")
        lista = []
        for lin in f:
            nom, car, sal = lin.strip().split(",")
            from trabajador import Trabajador
            lista.append(Trabajador(nom, int(car), float(sal)))
        f.close()

        lista.sort(key=lambda x: x.salario)

        print("=== Ordenados por salario ===")
        for x in lista:
            print(x.mostrar())
