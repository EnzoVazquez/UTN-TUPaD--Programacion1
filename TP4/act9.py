#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada

tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

turno = True

print("TA-TE-TI")
print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}")

while turno == True :
    print("Turno de CRUZ")
    movimiento_1 = int(input("Dime la fila"))
    movimiento_2 = int(input("ingrese columna"))
    #comprobamos que este libre
    if tablero[(movimiento_1-1)][(movimiento_2-1)] == "-":
        ##si esta libre, le asignamos x
        tablero [(movimiento_1-1)][(movimiento_2-1)] = "x"
        print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}")
        #comprobamos si gano
        for fila in tablero:
            #validamos asi para que no se ejecute con -
            if len(set(fila)) == 1 and fila[0] != "-":
                print(f"Gano X en una fila")
                break
            else:
                pass
        turno = False
    else:
        print("Lugar Ocupado")
else :
    print("Turno de CIRCULO")
    movimiento_1 = int(input("Dime la fila"))
    movimiento_2 = int(input("ingrese columna"))
    #comprobamos que este libre
    if tablero[(movimiento_1-1)][(movimiento_2-1)] == "-":
        ##si esta libre, le asignamos x
        tablero [(movimiento_1-1)][(movimiento_2-1)] = "0"
        print(f"{tablero[0]}\n{tablero[1]}\n{tablero[2]}")
        #comprobamos si gano
        for fila in tablero:
            #validamos asi para que no se ejecute con -
            if len(set(fila)) == 1 and fila[0] != "-":
                print(f"Gano X en una fila")
                break
            else:
                pass
        turno = True
    else:
        print("Lugar Ocupado")