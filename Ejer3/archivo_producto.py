class ArchivoProducto:
    def __init__(self, nomA):
        self.nomA = nomA

    def crearArchivo(self):
        f = open(self.nomA, "w")
        f.close()

    def guardarProducto(self, p):
        linea = f"{p.codigo},{p.nombre},{p.precio}\n"
        f = open(self.nomA, "a")
        f.write(linea)
        f.close()

    def buscaProducto(self, cod):
        f = open(self.nomA, "r")
        for lin in f:
            c, nom, pre = lin.strip().split(",")
            if int(c) == cod:
                from producto import Producto
                f.close()
                return Producto(int(c), nom, float(pre))
        f.close()
        return None

    def promedioPrecios(self):
        f = open(self.nomA, "r")
        suma = 0
        cont = 0
        for lin in f:
            _, _, pre = lin.strip().split(",")
            suma += float(pre)
            cont += 1
        f.close()

        if cont == 0:
            return 0
        return suma / cont

    def productoMasCaro(self):
        f = open(self.nomA, "r")
        caro = None
        for lin in f:
            c, nom, pre = lin.strip().split(",")
            pre = float(pre)
            from producto import Producto
            p = Producto(int(c), nom, pre)
            if caro is None or p.precio > caro.precio:
                caro = p
        f.close()
        return caro
