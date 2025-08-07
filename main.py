def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

nombres = []
total= int(input("¿Cuántos Nombres desea agregar?: "))
for i in range(total):
    n = input("Ingrese los nombres: \n")
    nombres.append(n)

resultado = quick_sort(nombres)
print(resultado)