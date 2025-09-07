#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene

num = int(input("dame un numero entero "))
digitos = len(str(num))
count = 0

for i in range(0,digitos, 1):
    count = count + 1

print(f"{num} Tiene {count} digitos")