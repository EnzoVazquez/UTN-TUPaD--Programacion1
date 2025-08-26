#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

ES_MAYOR = 18

edad = int(input("Dime tu edad "))

if edad >= ES_MAYOR:
    print("Usted es mayor de edad")
else:
    print("Lo siento, tu no eres mayor de edad")