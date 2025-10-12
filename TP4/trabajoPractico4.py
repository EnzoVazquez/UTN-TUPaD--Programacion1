#EJERCICIO 1
#Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja

notas = [9.5, 6.8, 7.3, 4.2, 7.2, 8.0, 7.8, 8.2, 6.3, 8.5]
cantidad = len(notas)
acum = 0
max = float("-inf")
min = float("inf")
#mostar listar completas
print(notas)
#calcular el promedio 
for i in range (0,cantidad,1):
    num = notas[i]
    acum += num

prom = acum / cantidad
print(f"El promedio de las notas es {prom}")
#calcular la nota mas alta y mas baja
for i in range (0,cantidad,1):
    num = notas[i]
    if num > max :
        max = num
    elif num < min :
        min = num
    else :
        pass

print(f"la nota mas alta fue {max}, y la mas baja {min}")

#EJERCICIO2
#Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#pedir al usuario que cargue 5 productos
productos = []
cont = 0
control = False

while cont < 5 :
    item = input("Ingrese un producto: ")
    productos.append(item.lower())
    cont += 1

#mostrar la lista ordenada alfabeticamente
print(sorted(productos))

#preguntar al usuario que producto desea eliminar
while control == False:

    entrada = input("Dime que producto quiere eliminar: ")
    eliminado = entrada.lower()

    if eliminado in productos :
        productos.remove(eliminado)
        print (f"{eliminado} eliminado/a con exito!")
        control = True
    else :
        print(f"{eliminado} no esta entre tus productos")

#EJERCICIO 3
#Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista
import random
numeros = []
pares = []
impares = []
cont = 0
num = 0
cant_par = 0
cant_impar = 0
#lista de 15 numeros al azar
while cont < 15:
    num = random.randint(1,100)
    numeros.append(num)
    cont += 1
#crear lista de pares e impares
for i in range(0,len(numeros),1):
    item = numeros[i]
    if item % 2 == 0:
        pares.append(item)
    else :
        impares.append(item)
cant_par = len(pares)
cant_impar = len(impares)

print(f"{numeros}")
print(f"hubo {cant_par} pares, {pares}")
print(f"hubo {cant_impar} impares, {impares}")

#EJERCICIO 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_unicos = []
for num in datos :
    if num not in datos_unicos:
        datos_unicos.append(num)

print(datos)
print(datos_unicos)

#EJERCICIO 5
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada

estudiantes = ["pedro", "maria", "santiago", "gonzalo", "mariela", "victor", "enzo"]
print(f"estudiantes: {estudiantes}")
print("Quieres: \n 1.Eliminar uno\n 2.Agregar uno")
num = int(input())
if num < 1 or num > 2 :
    print("seleccione una opcion valida")
    pass
elif num == 1 :
    borrado = input("dime que estudiante quieres eliminar: ")
    if borrado in estudiantes:
        estudiantes.remove(borrado)
        print(estudiantes)
    else:
        print(f"{borrado} no es un estudiante")
elif num == 2 :
    agregado = input("dime que estudiante quieres agregar: ")
    estudiantes.append(agregado)
    print(estudiantes)

#EJERCICIO 6
#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero

numeros = [1, 2, 3, 4, 5, 6, 7]
ultimo = numeros.pop()
numeros.insert(0, ultimo)
print(numeros)

#EJERCICIO 7
#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica
temperaturas = [[7.5, 15.6], [6.2, 14.8], [8.0, 18.2], [7.5, 17.3], [6.8, 16.4], [7.2, 18.4], [8.3, 19.5]]
maximas = 0
minimas = 0
indice = len(temperaturas)
prom_maximas = 0
prom_minimas = 0
amplitud = 0
max_amplitud = float("-inf")
dia_amplitud = 0
#calcular promedios
for temperatura in temperaturas:
    minimas += temperatura[0]
    maximas += temperatura[1]

prom_maximas = maximas/indice
prom_minimas = minimas/indice
print(f"El promedio de las temperaturas minimas es {prom_minimas:.2f}\nEl promedio de las temperaturas maximas es {prom_maximas:.2f}")

#mostrar dia con mayor amplitud termica
for temperatura in temperaturas:
    amplitud = temperatura[1] - temperatura[0]
    if amplitud > max_amplitud:
        dia_amplitud = temperatura
        max_amplitud = amplitud
    else:
        pass
print(f"La mayor amplitud termica fue el dia que se registro {dia_amplitud}, con una amplitud de {max_amplitud}")

#EJERCICIO 8
#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia
#notas = [[nombre, matematicas, literatura, quimica]]

notas = [["juan", 8, 5, 9], ["micaela", 7, 8, 6], ["pedro", 6, 5, 7], ["gaston", 9, 8, 6], ["florencia", 9, 10, 8]]
materias = ["matematicas", "literatura", "quimica"]
promedio = 0
acum = 0
promedio_mat =0
#mostrar promedio
for estudiante in notas :
        for i in range(1,4,1):
                acum += estudiante[i]
                promedio = acum/3
        print(f"El promedio de {estudiante[0]} es {promedio}")
        acum = 0

# mostrar promedio de cada materia
for i in range (1,4,1):
        suma = 0
        for estudiante in notas:
                suma += estudiante[i]
        
        promedio_mat = suma / len(notas)
        print(f"El promedio de {materias[i-1]} es {promedio_mat}")

#EJERCICIO 9
#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada

tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

print("TA-TE-TI")
print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}")

turno = "X"
jugadas = 0

while jugadas < 9:
    print(f"Turno de {turno}")

    fila = int(input("Dime la fila (0-2)"))
    columna = int(input("Dime la columna (0-2)"))

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Valor fuera del rango, pon un valor valido")
        continue

    if tablero[fila][columna] != "-":
        print("casilla ocupada!")
        continue
    else:
        tablero[fila][columna] = turno

    print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}")

    if turno == "X" :
        turno = "O"
    else:
        turno = "X"

#EJERCICIO 10
#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.
ventas = [[8, 12, 2, 6], [10, 16, 7, 6], [11, 8, 9, 3], [11, 25, 4, 14], [14, 5, 6, 13], [12, 4, 8, 14], [13, 10, 11, 9]]
count = 0
acum = 0
record = 0
producto = 0
productos = ["manzana", "banana", "pera", "naranja"]
#mostrar el total vendido de cada producto y el mas vendido de la semana
for c in range (0,4,1):
    for i in range(0,7,1):
        venta_semana = ventas[i][c]
        acum += venta_semana
    match c: 
        case 0:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0
        case 1:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0
        case 2:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0
        case 3:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0

print(f"El producto mas vendido esta semana fue {productos[producto]} con {record} unidades")
#mostrar el dia con mayores ventas
for e in range (7):
    total_dia = 0
    record_ventas = 0
    dia_mayor = 0
    for i in range (4):
        total_dia += ventas[e][i]
    if total_dia > record_ventas:
        record_ventas = total_dia
        dia_mayor = e

print(f"El dia de mayor ventas el fue el dia {dia_mayor}, con un total de {record_ventas} ventas")


