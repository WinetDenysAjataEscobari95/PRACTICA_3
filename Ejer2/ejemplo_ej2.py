from trabajador import Trabajador
from archivo_trabajador import ArchivoTrabajador

arch = ArchivoTrabajador("trabajadores.txt")
arch.crearArchivo()

t1 = Trabajador("Ana", 123, 2500)
t2 = Trabajador("Luis", 456, 3100)
t3 = Trabajador("Maria", 789, 1800)

arch.guardarTrabajador(t1)
arch.guardarTrabajador(t2)
arch.guardarTrabajador(t3)

print("Mayor salario:")
m = arch.trabajadorMayorSalario()
print(m.mostrar())

arch.ordenarPorSalario()
