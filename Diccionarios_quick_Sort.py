def quick_sort(lista):
    if len(lista) <= 1:
        return lista

estudiantes = {}

cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))

for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}")

    carnet = input("Ingrese el número de carnet: ")
    estudiantes[carnet] = {}

    estudiantes[carnet]["nombre"] = input("Ingrese el nombre: ")
    estudiantes[carnet]["edad"] = int(input("Ingrese la edad: "))
    estudiantes[carnet]["carrera"] = input("Ingrese la carrera: ")
    estudiantes[carnet]["correo"] = input("Ingrese el correo: ")
    estudiantes[carnet]["telefono"] = input("Ingrese el  teléfono: ")
    estudiantes[carnet]["cursos"] = {}

    cantidad_cursos = int(input("¿A cuantos cursos se inscribirá? "))
    for j in range(cantidad_cursos):
        print(f"\nCurso #{j + 1}")
        codigo_curso = input("Código del curso: ")
        nombre_curso = input("Nombre del curso: ")
        tarea = float(input("Nota de tarea (0 a 100): "))
        parcial = float(input("Nota de parcial (0 a 100): "))
        proyecto = float(input("Nota de proyecto (0 a 100): "))

        estudiantes[carnet]["cursos"][codigo_curso] = {
            "nombre": nombre_curso,
            "tarea": tarea,
            "parcial": parcial,
            "proyecto": proyecto
        }

print("\nLista de estudiantes registrados:")
for carnet, datos in estudiantes.items():
    print(f"\nCarnet: {carnet}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Carrera: {datos['carrera']}")
    print(f"Correo: {datos['correo']}")
    print(f"Teléfono: {datos['telefono']}")
    print("Cursos:")
    for codigo, curso in datos["cursos"].items():
        promedio = (curso["tarea"] + curso["parcial"] + curso["proyecto"]) / 3
        print(f"  - Código: {codigo}")
        print(f"     Nombre: {curso['nombre']}")
        print(f"     Tarea: {curso['tarea']}")
        print(f"     Parcial: {curso['parcial']}")
        print(f"     Proyecto: {curso['proyecto']}")
        print(f"     Promedio: {promedio:.2f}")
"""
print("\nBúsqueda de estudiante")
buscado = input("Ingrese el número de carnet que desea buscar: ")

if buscado in estudiantes:
    est = estudiantes[buscado]
    print("\nEstudiante encontrado:")
    print(f"Nombre: {est['nombre']}")
    print(f"Edad: {est['edad']}")
    print(f"Carrera: {est['carrera']}")
    print(f"Correo: {est['correo']}")
    print(f"Teléfono: {est['telefono']}")
    print("Cursos:")
    for codigo, curso in est["cursos"].items():
        promedio = (curso["tarea"] + curso["parcial"] + curso["proyecto"]) / 3
        print(f"  - Código: {codigo}")
        print(f"     Nombre: {curso['nombre']}")
        print(f"     Tarea: {curso['tarea']}")
        print(f"     Parcial: {curso['parcial']}")
        print(f"     Proyecto: {curso['proyecto']}")
        print(f"     Promedio: {promedio:.2f}")
else:
    print("Estudiante no encontrado.")
"""