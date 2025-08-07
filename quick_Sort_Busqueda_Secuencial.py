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
    menores = [x for x in lista[1:] if x[1]["cant_paquete"] < pivote[1]["cant_paquete"]]
    iguales = [x for x in lista if x[1]["cant_paquete"] == pivote[1]["cant_paquete"]]
    mayores = [x for x in lista[1:] if x[1]["cant_paquete"] > pivote[1]["cant_paquete"]]

    return quick_sort(menores) + iguales + quick_sort(mayores)

repartidores = {}
total_rep =int(input("¿Cuántos repartidores participaron hoy?: "))
if total_rep >= 1:
    for i in range(total_rep):
        print(f"\nRepartidor #{i + 1}")
        while True:
            nombre = input("Nombre: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.  Intente de nuvoe")
            elif nombre in repartidores:
                print("El nombre ya fue ingresado.  Ingrese otro nombre")
            else:
                break
        while True:
            try:
               cant_paquete = int(input("Ingrese la cantidad de paquetes:  "))
               if cant_paquete < 0:
                   print("No puede ingresar una cantidad menor a 1. Intente nuevamente.")
               else:
                   break
            except ValueError:
                print("Debe ingresar un número válido.  Intente de nuevo")

        while True:
            zona = input("Ingrese la zona: ").strip()
            if zona == "":
                print("La zona no puede quedar vacía.  Intente de nuevo.")
            else:
                break


        repartidores[nombre] = {
             "cant_paquete": cant_paquete,
             "zona": zona
    }



#       print("\n")

    lista = list(repartidores.items())
    print(" -- Datos ingresados: -- ")
    for nombre, valor in lista:
        print(f" - {nombre} entregó {valor['cant_paquete']} paquetes en zona: {valor['zona']} ")

    lista = list(repartidores.items())
    resultado = quick_sort(lista)
    print("\n ---- Ranking -----")
    for i, (nombre, valor) in enumerate(resultado, start=1):

        print(f" {i} - {nombre} entregó {valor['cant_paquete']} paquetes en la zona {valor['zona']}")

    lista = list(repartidores.items())

    print("\n ---- Buscador-----")
    buscado = input(f"Ingrese el nombre del repartidor: ")
    if buscado in repartidores:
        valor_a_buscar = repartidores[buscado]
        print(f"{nombre} entregó {valor_a_buscar['cant_paquete']} paquete en la zona {valor_a_buscar['zona']}")
    else:
        print("No hay ningún repartidor con ese nombre")

    print("\n ---- Estadísticas-----")
    total_entregas =0
    lista = list(repartidores.items())
    for nombre, valor in lista:
        total_entregas += valor['cant_paquete']
    prom = total_entregas / len(repartidores)
    mayor_nombre, mayor_valor = resultado[-1]
    menor_nombre, menor_valor = resultado[0]


    print(f"Total de paquetes entregados: {total_entregas}")
    print(f"El promedio de entregas es de: {round(prom,2)}")
    print(f"El de mayor entregas fue: {mayor_nombre} ({mayor_valor['cant_paquete']})")
    print(f"El de menor entregas fue: {menor_nombre} ({menor_valor['cant_paquete']})")



else:
    print("Ha ingresado un valor incorrecto, adiós")
