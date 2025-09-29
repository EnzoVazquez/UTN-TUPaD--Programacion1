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