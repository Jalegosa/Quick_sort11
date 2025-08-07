"""def obtener_numero_positivo():
  #while True:
   total_rep = int(input("¿Cuántos repartidores participaron hoy?: "))
    if total_rep > 0:
        return total_rep
    else:
        print("Error: El número debe ser positivo.")
  #  except ValueError:
#      print("Error: Ingrese un número entero válido.")

numero_valido = obtener_numero_positivo()
print(f"El número ingresado es: {numero_valido}")

obtener_numero_positivo()
"""


def quick_sort(lista):
    if len(lista) <=1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


repartidores = {}
total_rep =int(input("¿Cuántos repartidores participaron hoy?: "))
if total_rep >= 1:
    for i in range(total_rep):
        print(f"\nRepartidor #{i + 1}")

        nombre = input("Nombre: ")
        repartidores[nombre] = {}

        repartidores[nombre]["cant_paquete"] = int(input("Ingrese la cantidad de paquetes:  "))
        repartidores[nombre]["zona"] = input("Ingrese la Zona: ")

lista = list(repartidores.values())
resultado = quick_sort(lista)
for nombre, valor in resultado:
    print(f"{nombre}: {valor}")

else:
    print("Ha ingresado un valor incorrecto, adiós")
