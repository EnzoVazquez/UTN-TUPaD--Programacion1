#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

def freno(limite, vuelta = 0):
    if vuelta > limite:
        return
    
    print(f"f fibonacci({vuelta}) = {fibonacci(vuelta)}" )

    freno(limite, vuelta + 1)
    
limite = int(input("Hasta que vuelta quieres que te muestre la serie de fibonacci: "))
freno(limite)

    