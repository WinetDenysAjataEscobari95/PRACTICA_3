import pickle
import os

# ----------------------------------------------------------
#  CLASE ANIMAL
# ----------------------------------------------------------
class Animal:
    def __init__(self, especie, nombre, cantidad):
        self.especie = especie
        self.nombre = nombre
        self.cantidad = cantidad

    def __repr__(self):
        return f"{self.nombre} ({self.especie}) x {self.cantidad}"


# ----------------------------------------------------------
#  CLASE ZOOLÓGICO
# ----------------------------------------------------------
class Zoologico:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.animales = []  # lista de objetos Animal

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def cantidad_variedades(self):
        return len(self.animales)

    def esta_vacio(self):
        return len(self.animales) == 0

    def obtener_por_especie(self, especie):
        return [a for a in self.animales if a.especie == especie]

    def __repr__(self):
        return f"Zoológico {self.nombre} (ID {self.id})"


# ----------------------------------------------------------
#  CLASE ARCHZOO  (persistencia de objetos)
# ----------------------------------------------------------
class ArchZoo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        if not os.path.exists(nombre_archivo):
            with open(nombre_archivo, "wb") as f:
                pickle.dump([], f)

    # ---------- a) crear, modificar y eliminar ----------------

    def guardar(self, lista):
        with open(self.nombre_archivo, "wb") as f:
            pickle.dump(lista, f)

    def cargar(self):
        with open(self.nombre_archivo, "rb") as f:
            return pickle.load(f)

    def crear_zoo(self, zoo):
        datos = self.cargar()
        datos.append(zoo)
        self.guardar(datos)

    def modificar_zoo(self, id, nuevo_nombre):
        datos = self.cargar()
        for z in datos:
            if z.id == id:
                z.nombre = nuevo_nombre
        self.guardar(datos)

    def eliminar_zoo(self, id):
        datos = self.cargar()
        datos = [z for z in datos if z.id != id]
        self.guardar(datos)

    # ---------- b) listar zoológicos con mayor variedad ---------

    def listar_por_variedad(self):
        datos = self.cargar()
        datos.sort(key=lambda z: z.cantidad_variedades(), reverse=True)
        return datos

    # ---------- c) listar y eliminar los zoológicos vacíos -----

    def eliminar_vacios(self):
        datos = self.cargar()
        datos = [z for z in datos if not z.esta_vacio()]
        self.guardar(datos)

    # ---------- d) mostrar animales de especie X ---------------

    def animales_por_especie(self, especie):
        datos = self.cargar()
        resultado = []
        for z in datos:
            lista = z.obtener_por_especie(especie)
            if lista:
                resultado.append((z.nombre, lista))
        return resultado

    # ---------- e) mover animales de un zoo X a uno Y ----------

    def mover_animales(self, id_x, id_y):
        datos = self.cargar()
        zoo_x = None
        zoo_y = None

        for z in datos:
            if z.id == id_x:
                zoo_x = z
            if z.id == id_y:
                zoo_y = z

        if zoo_x and zoo_y:
            zoo_y.animales.extend(zoo_x.animales)
            zoo_x.animales = []

        self.guardar(datos)

def menu():
    arch = ArchZoo("zoologicos.dat")

    while True:
        print("\n--- MENU ZOOLOGICOS ---")
        print("1. Crear zoológico")
        print("2. Modificar zoológico")
        print("3. Eliminar zoológico")
        print("4. Listar por variedad")
        print("5. Eliminar vacíos")
        print("6. Mostrar animales por especie")
        print("7. Mover animales de un zoo a otro")
        print("8. Salir")

        op = input("Opción: ")

        if op == "1":
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            z = Zoologico(id, nombre)

            cant = int(input("Cantidad de animales a registrar: "))
            for _ in range(cant):
                esp = input("Especie: ")
                nom = input("Nombre animal: ")
                num = int(input("Cantidad: "))
                z.agregar_animal(Animal(esp, nom, num))

            arch.crear_zoo(z)
            print("Zoológico creado.")

        elif op == "2":
            id = int(input("ID a modificar: "))
            nombre = input("Nuevo nombre: ")
            arch.modificar_zoo(id, nombre)
            print("Modificado.")

        elif op == "3":
            id = int(input("ID a eliminar: "))
            arch.eliminar_zoo(id)
            print("Eliminado.")

        elif op == "4":
            lista = arch.listar_por_variedad()
            print("\n--- ORDENADOS POR VARIEDAD ---")
            for z in lista:
                print(f"{z.nombre}: {z.cantidad_variedades()} variedades")

        elif op == "5":
            arch.eliminar_vacios()
            print("Zoológicos vacíos eliminados.")

        elif op == "6":
            esp = input("Especie a buscar: ")
            datos = arch.animales_por_especie(esp)
            for nombre, animales in datos:
                print(f"\nEn {nombre}:")
                for a in animales:
                    print("  ", a)

        elif op == "7":
            x = int(input("ID origen: "))
            y = int(input("ID destino: "))
            arch.mover_animales(x, y)
            print("Animales movidos.")

        elif op == "8":
            print("Saliendo...")
            break

        else:
            print("Opción incorrecta.")


# Ejecutar menú solo si es archivo principal
if __name__ == "__main__":
    menu()
