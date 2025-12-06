class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.ci = ci


class Niño(Persona):
    def __init__(self, nombre, apP, apM, ci, edad, peso, talla):
        super().__init__(nombre, apP, apM, ci)
        self.edad = edad
        self.peso = peso
        self.talla = talla


# "ArchNiño" → lista simulando archivo
arch_niños = []


# a) Crear, leer, listar y mostrar
def crear_nino(nombre, apP, apM, ci, edad, peso, talla):
    arch_niños.append(Niño(nombre, apP, apM, ci, edad, peso, talla))


def listar_ninos():
    for n in arch_niños:
        print(n.nombre, n.apellidoPaterno, n.apellidoMaterno,
              "| CI:", n.ci,
              "| Edad:", n.edad,
              "| Peso:", n.peso,
              "| Talla:", n.talla)


# b) Niños con peso adecuado (reglas simples por práctica)
def peso_adecuado(edad, talla, peso):
    # Regla referencial simple (puedes ajustar)
    # peso ideal aproximado: edad*2 + talla/10
    ideal = (edad * 2) + (talla / 10)
    return (ideal - 3) <= peso <= (ideal + 3)


def contar_niños_peso_adecuado():
    cont = 0
    for n in arch_niños:
        if peso_adecuado(n.edad, n.talla, n.peso):
            cont += 1
    print("Niños con peso adecuado:", cont)


# c) Mostrar niños con peso o talla NO adecuada
def mostrar_inadecuados():
    print("Niños con peso o talla NO adecuada:")
    for n in arch_niños:
        if not peso_adecuado(n.edad, n.talla, n.peso):
            print(n.nombre, n.apellidoPaterno, n.peso, n.talla)


# d) Promedio de edad
def promedio_edad():
    if not arch_niños:
        print("No hay datos")
        return
    prom = sum(n.edad for n in arch_niños) / len(arch_niños)
    print("Promedio de edad:", prom)


# e) Buscar niño por CI
def buscar_ci(ci):
    for n in arch_niños:
        if n.ci == ci:
            print("Encontrado:", n.nombre, n.apellidoPaterno, n.edad, "años")
            return
    print("No existe un niño con ese carnet.")


# f) Mostrar niños con la talla más alta
def niños_talla_mayor():
    if not arch_niños:
        print("No hay niños registrados")
        return
    max_talla = max(n.talla for n in arch_niños)

    print("Niños con la mayor talla:", max_talla)
    for n in arch_niños:
        if n.talla == max_talla:
            print(n.nombre, n.apellidoPaterno, n.talla)


# ------------------- MAIN -------------------
if __name__ == "__main__":
    print("Ejecución de Ejercicio 7...\n")

    # Datos de prueba
    crear_nino("Ana", "Pérez", "Loza", 123, 8, 24, 125)
    crear_nino("Luis", "Rojas", "Mamani", 456, 7, 20, 120)
    crear_nino("María", "Quispe", "Lima", 789, 9, 40, 130)

    print("a) Listado general:")
    listar_ninos()

    print("\nb) Peso adecuado:")
    contar_niños_peso_adecuado()

    print("\nc) Niños con peso o talla NO adecuada:")
    mostrar_inadecuados()

    print("\nd) Promedio de edad:")
    promedio_edad()

    print("\ne) Buscar niño con CI 456:")
    buscar_ci(456)

    print("\nf) Niños con mayor talla:")
    niños_talla_mayor()
