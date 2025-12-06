import pickle
from datetime import datetime

ARCHIVO = "alimentos.dat"


class Alimento:
    def __init__(self, nombre, fecha, cantidad):
        self.nombre = nombre
        self.fecha = fecha      
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - {self.fecha} - Cant: {self.cantidad}"



def guardar(lista):
    with open(ARCHIVO, "wb") as f:
        pickle.dump(lista, f)


def cargar():
    try:
        with open(ARCHIVO, "rb") as f:
            return pickle.load(f)
    except:
        return []


def crear_alimento():
    lista = cargar()
    nombre = input("Nombre: ")
    fecha = input("Fecha vencimiento (dd/mm/aaaa): ")
    cantidad = int(input("Cantidad: "))

    lista.append(Alimento(nombre, fecha, cantidad))
    guardar(lista)
    print("Alimento registrado.")


def modificar_por_nombre():
    lista = cargar()
    nom = input("Nombre a modificar: ")

    for a in lista:
        if a.nombre.lower() == nom.lower():
            print("Encontrado. Ingrese nuevos datos.")
            a.nombre = input("Nuevo nombre: ")
            a.fecha = input("Nueva fecha (dd/mm/aaaa): ")
            a.cantidad = int(input("Nueva cantidad: "))
            guardar(lista)
            print("Modificado.")
            return

    print("No encontrado.")


def eliminar_por_nombre():
    lista = cargar()
    nom = input("Nombre a eliminar: ")

    nueva = [a for a in lista if a.nombre.lower() != nom.lower()]

    guardar(nueva)
    print("Eliminado si existía.")


def alimentos_caducados_antes():
    lista = cargar()
    x = input("Fecha límite (dd/mm/aaaa): ")

    fecha_x = datetime.strptime(x, "%d/%m/%Y")

    for a in lista:
        f = datetime.strptime(a.fecha, "%d/%m/%Y")
        if f < fecha_x:
            print(a)


def eliminar_cantidad_cero():
    lista = cargar()
    nueva = [a for a in lista if a.cantidad > 0]
    guardar(nueva)
    print("Eliminados los que tenían cantidad 0.")


def alimentos_vencidos():
    lista = cargar()
    hoy = datetime.now()

    for a in lista:
        f = datetime.strptime(a.fecha, "%d/%m/%Y")
        if f < hoy:
            print(a)


def alimento_mayor_cantidad():
    lista = cargar()
    if not lista:
        print("No hay alimentos.")
        return

    mayor = max(lista, key=lambda x: x.cantidad)
    print("Mayor cantidad:", mayor)


def mostrar_todos():
    lista = cargar()
    for a in lista:
        print(a)


# -------------------- MENÚ --------------------

if __name__ == "__main__":
    while True:
        print("\n=== MENU EJERCICIO 8 ===")
        print("1. Crear alimento")
        print("2. Modificar por nombre")
        print("3. Eliminar por nombre")
        print("4. Mostrar alimentos caducados antes de fecha X")
        print("5. Eliminar alimentos con cantidad 0")
        print("6. Buscar alimentos vencidos")
        print("7. Mostrar alimento con mayor cantidad")
        print("8. Mostrar todos")
        print("9. Salir")

        op = input("Opción: ")

        if op == "1":
            crear_alimento()
        elif op == "2":
            modificar_por_nombre()
        elif op == "3":
            eliminar_por_nombre()
        elif op == "4":
            alimentos_caducados_antes()
        elif op == "5":
            eliminar_cantidad_cero()
        elif op == "6":
            alimentos_vencidos()
        elif op == "7":
            alimento_mayor_cantidad()
        elif op == "8":
            mostrar_todos()
        elif op == "9":
            break
        else:
            print("Opción inválida.")
