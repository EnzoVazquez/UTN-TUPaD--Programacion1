#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745
import math

num = int(input("ingrese un numero y se lo devolvere invertido "))

vueltas = len( str(num))
exp = vueltas - 1
acum = 0
ultimo = 0

for i in range(0, vueltas, 1):
    ultimo = num % 10
    num = math.trunc(num/10)
    acum = acum + (ultimo * 10**exp)
    exp = exp-1

print(f"Al reves es {acum}")