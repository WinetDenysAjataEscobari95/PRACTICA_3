import pickle
import os

class Charango:
    def __init__(self, material, nro_cuerdas, cuerdas):
        self.material = material
        self.nro_cuerdas = nro_cuerdas
        self.cuerdas = cuerdas
    
    def __str__(self):
        cuerdas_str = ''.join(['T' if c else 'F' for c in self.cuerdas[:self.nro_cuerdas]])
        return f"Charango[{self.material}, {self.nro_cuerdas} cuerdas: {cuerdas_str}]"

class GestorCharangos:
    def __init__(self, archivo='charangos.dat'):
        self.archivo = archivo
        self.charangos = []
        self.cargar_datos()
    
    def guardar_datos(self):
        with open(self.archivo, 'wb') as f:
            pickle.dump(self.charangos, f)
    
    def cargar_datos(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'rb') as f:
                    self.charangos = pickle.load(f)
            except:
                self.charangos = []
        else:
            self.charangos = []
    
    def agregar_charango(self, charango):
        self.charangos.append(charango)
        self.guardar_datos()
    
    def eliminar_false_mayor_a_6(self):
        charangos_eliminar = []
        
        for charango in self.charangos:
            cuerdas_false = 0
            for i in range(charango.nro_cuerdas):
                if i < len(charango.cuerdas) and not charango.cuerdas[i]:
                    cuerdas_false += 1
            
            if cuerdas_false > 6:
                charangos_eliminar.append(charango)
        
        for charango in charangos_eliminar:
            self.charangos.remove(charango)
        
        if charangos_eliminar:
            self.guardar_datos()
        
        return len(charangos_eliminar)
    
    def listar_por_material(self, material):
        resultado = []
        for charango in self.charangos:
            if charango.material.lower() == material.lower():
                resultado.append(charango)
        return resultado
    
    def buscar_con_10_cuerdas(self):
        resultado = []
        for charango in self.charangos:
            if charango.nro_cuerdas == 10:
                resultado.append(charango)
        return resultado
    
    def ordenar_por_material(self):
        self.charangos.sort(key=lambda x: x.material.lower())
        self.guardar_datos()
    
    def mostrar_todos(self):
        for i, charango in enumerate(self.charangos, 1):
            print(f"{i}. {charango}")

def menu_principal():
    gestor = GestorCharangos()
    
    while True:
        print("\n" + "="*50)
        print("GESTOR DE CHARANGOS")
        print("="*50)
        print("1. Agregar nuevo charango")
        print("2. Eliminar charangos con >6 cuerdas false")
        print("3. Listar charangos por material")
        print("4. Buscar charangos con 10 cuerdas")
        print("5. Ordenar charangos por material")
        print("6. Mostrar todos los charangos")
        print("7. Generar datos de prueba")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            material = input("Material del charango: ")
            
            while True:
                try:
                    nro_cuerdas = int(input("Número de cuerdas (1-10): "))
                    if 1 <= nro_cuerdas <= 10:
                        break
                    else:
                        print("Debe ser entre 1 y 10")
                except ValueError:
                    print("Debe ingresar un número válido")
            
            print("Estado de las cuerdas (T=true/afinada, F=false/desafinada)")
            cuerdas = []
            for i in range(nro_cuerdas):
                while True:
                    estado = input(f"Cuerda {i+1} (T/F): ").upper()
                    if estado == 'T':
                        cuerdas.append(True)
                        break
                    elif estado == 'F':
                        cuerdas.append(False)
                        break
                    else:
                        print("Ingrese T o F")
            
            charango_nuevo = Charango(material, nro_cuerdas, cuerdas)
            gestor.agregar_charango(charango_nuevo)
            print(f"Charango agregado: {charango_nuevo}")
        
        elif opcion == "2":
            eliminados = gestor.eliminar_false_mayor_a_6()
            print(f"Se eliminaron {eliminados} charango(s)")
        
        elif opcion == "3":
            material = input("Ingrese el material a buscar: ")
            charangos = gestor.listar_por_material(material)
            if charangos:
                print(f"\nCharangos de material '{material}':")
                for i, c in enumerate(charangos, 1):
                    print(f"{i}. {c}")
            else:
                print(f"No hay charangos de material '{material}'")
        
        elif opcion == "4":
            charangos = gestor.buscar_con_10_cuerdas()
            if charangos:
                print("\nCharangos con 10 cuerdas:")
                for i, c in enumerate(charangos, 1):
                    print(f"{i}. {c}")
            else:
                print("No hay charangos con 10 cuerdas")
        
        elif opcion == "5":
            gestor.ordenar_por_material()
            print("Charangos ordenados por material alfabéticamente")
            gestor.mostrar_todos()
        
        elif opcion == "6":
            if gestor.charangos:
                print("\nTodos los charangos:")
                gestor.mostrar_todos()
            else:
                print("No hay charangos registrados")
        
        elif opcion == "7":
            datos_prueba = [
                Charango("Madera", 10, [True, True, False, False, False, False, False, False, False, False]),
                Charango("Madera", 8, [True, True, True, True, False, False, False, False]),
                Charango("Plástico", 10, [True, True, True, True, True, True, True, True, True, True]),
                Charango("Metal", 5, [False, False, False, False, False]),
                Charango("Madera", 10, [False, False, False, False, False, False, False, True, True, True]),
                Charango("Plástico", 7, [True, False, False, False, False, False, False]),
                Charango("Metal", 10, [True, False, True, False, True, False, True, False, True, False])
            ]
            
            for charango in datos_prueba:
                gestor.agregar_charango(charango)
            
            print("Datos de prueba generados exitosamente")
        
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

def pruebas_unitarias():
    print("=== PRUEBAS UNITARIAS ===")
    
    gestor_prueba = GestorCharangos('prueba.dat')
    
    # Limpiar archivo de prueba
    gestor_prueba.charangos = []
    
    # Crear charangos de prueba
    c1 = Charango("Madera", 10, [True]*10)
    c2 = Charango("Plástico", 10, [False]*10)  # 10 falses
    c3 = Charango("Metal", 8, [False]*8)  # 8 falses
    c4 = Charango("Madera", 5, [True]*5)
    
    gestor_prueba.agregar_charango(c1)
    gestor_prueba.agregar_charango(c2)
    gestor_prueba.agregar_charango(c3)
    gestor_prueba.agregar_charango(c4)
    
    # Prueba b) Eliminar con >6 falses
    print("\n1. Eliminar charangos con >6 cuerdas false:")
    eliminados = gestor_prueba.eliminar_false_mayor_a_6()
    print(f"Eliminados: {eliminados}")
    print(f"Quedan: {len(gestor_prueba.charangos)} charangos")
    
    # Prueba c) Listar por material
    print("\n2. Listar charangos de material 'Madera':")
    madera = gestor_prueba.listar_por_material("Madera")
    for c in madera:
        print(f"  - {c}")
    
    # Prueba d) Buscar con 10 cuerdas
    print("\n3. Buscar charangos con 10 cuerdas:")
    diez_cuerdas = gestor_prueba.buscar_con_10_cuerdas()
    for c in diez_cuerdas:
        print(f"  - {c}")
    
    # Prueba e) Ordenar por material
    print("\n4. Ordenar por material:")
    gestor_prueba.ordenar_por_material()
    gestor_prueba.mostrar_todos()
    
    # Limpiar archivo de prueba
    if os.path.exists('prueba.dat'):
        os.remove('prueba.dat')

if __name__ == "__main__":
    print("PRÁCTICA DE AUXILIATURA - PROGRAMACIÓN II")
    print("TEMA: PERSISTENCIA DE OBJETOS")
    print("Ejercicio: Gestión de Charangos\n")
    
    menu_principal()