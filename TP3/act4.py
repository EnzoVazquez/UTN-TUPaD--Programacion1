#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

print("dame numeros enteros y los ire sumando, cuando ingreses 0 te dare el acumulativo")

num = 0
acum = 0

while True:
    num = int(input())
    acum = acum + num
    if num == 0:
        break

print(acum)