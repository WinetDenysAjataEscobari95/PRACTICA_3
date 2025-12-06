class Libro:
    def __init__(self, cod, titulo, precio):
        self.cod = cod
        self.titulo = titulo
        self.precio = precio

class Prestamo:
    def __init__(self, codCliente, codLibro, fecha, cantidad):
        self.codCliente = codCliente
        self.codLibro = codLibro
        self.fecha = fecha
        self.cantidad = cantidad

class Cliente:
    def __init__(self, codCliente, ci, nombre, apellido):
        self.codCliente = codCliente
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido


# --- ARCHIVOS (listas) ---
arch_libros = []
arch_clientes = []
arch_prestamos = []


# a) Libros con precio entre x e y
def libros_por_precio(x, y):
    for l in arch_libros:
        if x <= l.precio <= y:
            print(l.cod, l.titulo, l.precio)


# b) Ingreso total por un libro
def ingreso_libro(codLibro):
    total = 0
    for p in arch_prestamos:
        if p.codLibro == codLibro:
            total += p.cantidad
    print("Ingreso total:", total)


# c) Libros que nunca fueron prestados
def libros_no_vendidos():
    usados = set([p.codLibro for p in arch_prestamos])
    for l in arch_libros:
        if l.cod not in usados:
            print(l.cod, l.titulo)


# d) Clientes que compraron un libro
def clientes_que_compraron(codLibro):
    clientes_usaron = set([p.codCliente for p in arch_prestamos if p.codLibro == codLibro])
    for c in arch_clientes:
        if c.codCliente in clientes_usaron:
            print(c.nombre, c.apellido)


# e) Libro más prestado
def libro_mas_prestado():
    if not arch_prestamos:
        print("Sin préstamos")
        return

    cont = {}
    for p in arch_prestamos:
        cont[p.codLibro] = cont.get(p.codLibro, 0) + p.cantidad

    cod_max = max(cont, key=cont.get)

    for l in arch_libros:
        if l.cod == cod_max:
            print("El más prestado es:", l.titulo)
            break


# f) Cliente con más préstamos
def cliente_mas_prestamos():
    if not arch_prestamos:
        print("Sin préstamos")
        return

    cont = {}
    for p in arch_prestamos:
        cont[p.codCliente] = cont.get(p.codCliente, 0) + p.cantidad

    cod_max = max(cont, key=cont.get)

    for c in arch_clientes:
        if c.codCliente == cod_max:
            print("Cliente con más préstamos:", c.nombre, c.apellido)
            break



# ------------------ MAIN ------------------
if __name__ == "__main__":
    print("EJECUTANDO EJERCICIO 6...\n")

    # Cargando datos
    arch_libros.append(Libro(1, "Python Básico", 50))
    arch_libros.append(Libro(2, "Java Intermedio", 80))
    arch_libros.append(Libro(3, "C++ Avanzado", 120))

    arch_clientes.append(Cliente(1, 123456, "Ana", "Pérez"))
    arch_clientes.append(Cliente(2, 789101, "Luis", "Rojas"))
    arch_clientes.append(Cliente(3, 456789, "María", "Loza"))

    arch_prestamos.append(Prestamo(1, 1, "2024-01-10", 2))
    arch_prestamos.append(Prestamo(2, 2, "2024-02-11", 1))
    arch_prestamos.append(Prestamo(1, 2, "2024-03-01", 3))
    arch_prestamos.append(Prestamo(3, 1, "2024-03-05", 1))

    print("a) Libros entre 40 y 100:")
    libros_por_precio(40, 100)

    print("\nb) Ingreso del libro 1:")
    ingreso_libro(1)

    print("\nc) Libros nunca vendidos:")
    libros_no_vendidos()

    print("\nd) Clientes que compraron el libro 2:")
    clientes_que_compraron(2)

    print("\ne) Libro más prestado:")
    libro_mas_prestado()

    print("\nf) Cliente con más préstamos:")
    cliente_mas_prestamos()
