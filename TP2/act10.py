#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano

print("Vamos a ver en que estacion estas ")
hemisferio = input("Dime en que hemisferio te encuentra(N o S) ")
mes = input("Dime en que mes estas ").lower()
dia = int(input("Dime el dia "))

if hemisferio == "n" or hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Invierno")
    elif(mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia <= 20):
        print("primavera")
    elif(mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("verano")
    elif(mes == "septiembre" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print("otoño")
    else:
        print("ha ocurrido un error")
elif hemisferio == "s" or hemisferio == "S":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Verano")
    elif(mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Otoño")
    elif(mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Invierno")
    elif(mes == "septiembre" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print("Primavera")
    else:
        print("ha ocurrido un error")
else:
    print("Seleccione una opcion valida")