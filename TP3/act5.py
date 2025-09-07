#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

print("adivina en que numero estoy pensando!")
print("solo valen numeros del 1 a 9")

acum = 0
aleatorio = random.randint(1,9)

while True:
    num = int(input("que numero es? "))
    acum = acum + 1
    if num == aleatorio:
        break

print(f"el numero era {aleatorio}! solo tardaste {acum} intentos!")