import os

# Clase Empresa
class Empresa:
    def __init__(self, nombre, rubro, num_empleados):
        self.nombre = nombre
        self.rubro = rubro
        self.num_empleados = num_empleados

    def __str__(self):
        return f"Nombre: {self.nombre}, Rubro: {self.rubro}, Empleados: {self.num_empleados}"

# Clase GestorEmpresas (maneja persistencia)
class GestorEmpresas:
    def __init__(self, archivo="empresas.txt"):
        self.archivo = archivo
        # Crear archivo si no existe
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()

    # Guardar empresa en archivo
    def agregar_empresa(self, empresa):
        with open(self.archivo, "a") as f:
            f.write(f"{empresa.nombre},{empresa.rubro},{empresa.num_empleados}\n")

    # Mostrar todas las empresas
    def mostrar_todas(self):
        print("\n--- Lista de empresas ---")
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
            if not lineas:
                print("No hay empresas registradas.")
            for linea in lineas:
                nombre, rubro, num_empleados = linea.strip().split(",")
                print(f"Nombre: {nombre}, Rubro: {rubro}, Empleados: {num_empleados}")

    # Buscar empresa por nombre
    def buscar_por_nombre(self, nombre_buscar):
        with open(self.archivo, "r") as f:
            for linea in f:
                nombre, rubro, num_empleados = linea.strip().split(",")
                if nombre.lower() == nombre_buscar.lower():
                    print(f"Empresa encontrada: Nombre: {nombre}, Rubro: {rubro}, Empleados: {num_empleados}")
                    return
            print("Empresa no encontrada.")

# Menú interactivo
def menu():
    gestor = GestorEmpresas()
    while True:
        print("\n--- Gestión de Empresas ---")
        print("1. Agregar empresa")
        print("2. Mostrar todas las empresas")
        print("3. Buscar empresa por nombre")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la empresa: ")
            rubro = input("Rubro: ")
            num_empleados = input("Número de empleados: ")
            empresa = Empresa(nombre, rubro, num_empleados)
            gestor.agregar_empresa(empresa)
            print("Empresa agregada correctamente.")
        elif opcion == "2":
            gestor.mostrar_todas()
        elif opcion == "3":
            nombre = input("Nombre de la empresa a buscar: ")
            gestor.buscar_por_nombre(nombre)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar menú
if __name__ == "__main__":
    menu()
