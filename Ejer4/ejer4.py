import pickle
import os

class Estudiante:
    def __init__(self, ru, nombre, paterno, materno, edad):
        self.ru = ru
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
    
    def __str__(self):
        return f"{self.ru}: {self.nombre} {self.paterno} {self.materno}, {self.edad} años"
    
    def __repr__(self):
        return f"Estudiante({self.ru})"

class Nota:
    def __init__(self, materia, notaFinal, estudiante):
        self.materia = materia
        self.notaFinal = notaFinal
        self.estudiante = estudiante
    
    def __str__(self):
        return f"{self.materia}: {self.notaFinal:.2f} - {self.estudiante.nombre}"
    
    def __repr__(self):
        return f"Nota({self.materia}, {self.notaFinal})"

class ArchiNota:
    def __init__(self, nombreArchi="notas.dat"):
        self.nombreArchi = nombreArchi
        self.notas = []
        self.cargar_datos()
    
    def guardar_datos(self):
        with open(self.nombreArchi, 'wb') as f:
            pickle.dump(self.notas, f)
    
    def cargar_datos(self):
        if os.path.exists(self.nombreArchi):
            try:
                with open(self.nombreArchi, 'rb') as f:
                    self.notas = pickle.load(f)
            except Exception as e:
                print(f"Error al cargar datos: {e}")
                self.notas = []
        else:
            self.notas = []
    
    # b) Método para agregar varios estudiantes
    def agregar_varios_estudiantes(self, lista_notas):
        """
        Agrega varias notas de estudiantes a la vez
        lista_notas: lista de tuplas (materia, notaFinal, estudiante)
        """
        for materia, notaFinal, estudiante in lista_notas:
            nueva_nota = Nota(materia, notaFinal, estudiante)
            self.notas.append(nueva_nota)
        self.guardar_datos()
        print(f"Se agregaron {len(lista_notas)} notas de estudiantes")
    
    # c) Obtener promedio de notas de todos los estudiantes
    def promedio_notas(self):
        if not self.notas:
            return 0.0
        
        suma_notas = sum(nota.notaFinal for nota in self.notas)
        return suma_notas / len(self.notas)
    
    # d) Buscar estudiantes con la mejor nota
    def mejores_estudiantes(self):
        if not self.notas:
            return []
        
        # Encontrar la nota máxima
        mejor_nota = max(self.notas, key=lambda x: x.notaFinal).notaFinal
        
        # Encontrar todos los estudiantes con esa nota
        mejores = []
        for nota in self.notas:
            if nota.notaFinal == mejor_nota:
                mejores.append(nota)
        
        return mejores
    
    # e) Eliminar estudiantes de una determinada materia
    def eliminar_por_materia(self, materia):
        notas_originales = len(self.notas)
        
        # Filtrar las notas que NO son de la materia especificada
        self.notas = [nota for nota in self.notas if nota.materia.lower() != materia.lower()]
        
        notas_eliminadas = notas_originales - len(self.notas)
        
        if notas_eliminadas > 0:
            self.guardar_datos()
        
        return notas_eliminadas
    
    def listar_todo(self):
        if not self.notas:
            print("No hay notas registradas")
            return
        
        for i, nota in enumerate(self.notas, 1):
            print(f"{i}. {nota}")
    
    def contar_estudiantes(self):
        # Obtener estudiantes únicos por RU
        estudiantes_unicos = set()
        for nota in self.notas:
            estudiantes_unicos.add(nota.estudiante.ru)
        return len(estudiantes_unicos)

def crear_estudiante():
    print("\n--- CREAR NUEVO ESTUDIANTE ---")
    ru = input("RU: ")
    nombre = input("Nombre: ")
    paterno = input("Apellido paterno: ")
    materno = input("Apellido materno: ")
    
    while True:
        try:
            edad = int(input("Edad: "))
            if edad > 0:
                break
            else:
                print("La edad debe ser positiva")
        except ValueError:
            print("Ingrese un número válido")
    
    return Estudiante(ru, nombre, paterno, materno, edad)

def agregar_nota_estudiante(archi_nota):
    estudiante = crear_estudiante()
    
    materia = input("Materia: ")
    
    while True:
        try:
            notaFinal = float(input("Nota final (0-100): "))
            if 0 <= notaFinal <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100")
        except ValueError:
            print("Ingrese un número válido")
    
    nota = Nota(materia, notaFinal, estudiante)
    archi_nota.notas.append(nota)
    archi_nota.guardar_datos()
    print(f"Nota agregada: {nota}")

def menu_principal():
    archi_nota = ArchiNota()
    
    while True:
        print("\n" + "="*60)
        print("SISTEMA DE GESTIÓN DE ESTUDIANTES Y NOTAS")
        print("="*60)
        print(f"Estudiantes: {archi_nota.contar_estudiantes()} | Notas: {len(archi_nota.notas)}")
        print("="*60)
        print("1. Agregar nueva nota de estudiante")
        print("2. Agregar varios estudiantes (ejercicio b)")
        print("3. Ver promedio de notas (ejercicio c)")
        print("4. Buscar mejores estudiantes (ejercicio d)")
        print("5. Eliminar estudiantes por materia (ejercicio e)")
        print("6. Listar todas las notas")
        print("7. Generar datos de prueba")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_nota_estudiante(archi_nota)
        
        elif opcion == "2":
            print("\n--- AGREGAR VARIOS ESTUDIANTES ---")
            print("Ingrese los datos de varios estudiantes")
            
            lista_notas = []
            while True:
                print(f"\nEstudiante {len(lista_notas) + 1}:")
                estudiante = crear_estudiante()
                materia = input("Materia: ")
                
                while True:
                    try:
                        notaFinal = float(input("Nota final (0-100): "))
                        if 0 <= notaFinal <= 100:
                            break
                        else:
                            print("La nota debe estar entre 0 y 100")
                    except ValueError:
                        print("Ingrese un número válido")
                
                lista_notas.append((materia, notaFinal, estudiante))
                
                continuar = input("¿Agregar otro estudiante? (s/n): ").lower()
                if continuar != 's':
                    break
            
            if lista_notas:
                archi_nota.agregar_varios_estudiantes(lista_notas)
        
        elif opcion == "3":
            promedio = archi_nota.promedio_notas()
            print(f"\nPromedio de todas las notas: {promedio:.2f}")
            
            if archi_nota.notas:
                # Mostrar también promedio por materia
                materias = {}
                for nota in archi_nota.notas:
                    if nota.materia not in materias:
                        materias[nota.materia] = []
                    materias[nota.materia].append(nota.notaFinal)
                
                print("\nPromedio por materia:")
                for materia, notas in materias.items():
                    promedio_materia = sum(notas) / len(notas)
                    print(f"  {materia}: {promedio_materia:.2f}")
        
        elif opcion == "4":
            mejores = archi_nota.mejores_estudiantes()
            if mejores:
                mejor_nota = mejores[0].notaFinal
                print(f"\nMejor nota: {mejor_nota:.2f}")
                print(f"Estudiantes con la mejor nota ({len(mejores)}):")
                
                for i, nota in enumerate(mejores, 1):
                    estudiante = nota.estudiante
                    print(f"{i}. {estudiante.nombre} {estudiante.paterno} - {nota.materia}: {nota.notaFinal:.2f}")
            else:
                print("No hay notas registradas")
        
        elif opcion == "5":
            materia = input("Ingrese la materia a eliminar: ")
            eliminados = archi_nota.eliminar_por_materia(materia)
            
            if eliminados > 0:
                print(f"Se eliminaron {eliminados} registros de la materia '{materia}'")
            else:
                print(f"No se encontraron registros de la materia '{materia}'")
        
        elif opcion == "6":
            print("\n--- LISTA DE TODAS LAS NOTAS ---")
            archi_nota.listar_todo()
        
        elif opcion == "7":
            # Generar datos de prueba
            estudiantes_prueba = [
                Estudiante("12345", "Juan", "Pérez", "Gómez", 20),
                Estudiante("23456", "María", "López", "García", 21),
                Estudiante("34567", "Carlos", "Rodríguez", "Martínez", 22),
                Estudiante("45678", "Ana", "González", "Fernández", 19),
                Estudiante("56789", "Luis", "Sánchez", "Díaz", 23),
            ]
            
            notas_prueba = [
                ("Programación II", 85.5, estudiantes_prueba[0]),
                ("Base de Datos", 92.0, estudiantes_prueba[1]),
                ("Programación II", 78.5, estudiantes_prueba[2]),
                ("Base de Datos", 95.0, estudiantes_prueba[1]),
                ("Estructuras de Datos", 88.0, estudiantes_prueba[3]),
                ("Programación II", 95.0, estudiantes_prueba[4]),
                ("Estructuras de Datos", 76.5, estudiantes_prueba[0]),
                ("Base de Datos", 89.0, estudiantes_prueba[3]),
            ]
            
            archi_nota.agregar_varios_estudiantes(notas_prueba)
            print("Datos de prueba generados exitosamente")
        
        elif opcion == "8":
            print("¡Hasta luego!")
            archi_nota.guardar_datos()
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

def ejecutar_pruebas():
    print("=== EJECUTANDO PRUEBAS DEL EJERCICIO ===")
    
    # Crear archivo de prueba
    archi_prueba = ArchiNota("prueba_notas.dat")
    archi_prueba.notas = []  # Limpiar datos existentes
    
    # Crear estudiantes de prueba
    est1 = Estudiante("1001", "Ana", "Torres", "Méndez", 20)
    est2 = Estudiante("1002", "Juan", "Castro", "Ríos", 21)
    est3 = Estudiante("1003", "María", "Vargas", "Luna", 22)
    
    # Agregar notas (ejercicio b)
    notas_prueba = [
        ("Matemáticas", 85.0, est1),
        ("Física", 92.0, est2),
        ("Matemáticas", 78.0, est3),
        ("Química", 95.0, est1),  # Mejor nota
        ("Física", 88.0, est3),
        ("Química", 90.0, est2),
    ]
    
    archi_prueba.agregar_varios_estudiantes(notas_prueba)
    
    print("\nDatos cargados:")
    archi_prueba.listar_todo()
    
    # c) Promedio de notas
    promedio = archi_prueba.promedio_notas()
    print(f"\nc) Promedio de notas: {promedio:.2f}")
    
    # d) Mejores estudiantes
    mejores = archi_prueba.mejores_estudiantes()
    print(f"\nd) Mejor(es) estudiante(s):")
    for nota in mejores:
        print(f"  - {nota.estudiante.nombre}: {nota.materia} = {nota.notaFinal}")
    
    # e) Eliminar por materia
    print(f"\ne) Eliminando registros de 'Física'...")
    eliminados = archi_prueba.eliminar_por_materia("Física")
    print(f"  Eliminados: {eliminados} registros")
    print(f"  Notas restantes: {len(archi_prueba.notas)}")
    
    # Limpiar archivo de prueba
    if os.path.exists("prueba_notas.dat"):
        os.remove("prueba_notas.dat")
    
    print("\nPruebas completadas exitosamente")

if __name__ == "__main__":
    print("EJERCICIO 4 - GESTIÓN DE ESTUDIANTES Y NOTAS")
    print("Clases: Estudiante, Nota, ArchiNota")
    
    # Descomentar para ejecutar pruebas automáticas
    # ejecutar_pruebas()
    
    # Ejecutar menú principal
    menu_principal()