#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores

print("dame 2 numeros y te devolvere la suma de todos los valores entre ellos")
num1 = int(input("el primero: "))
num2 = int(input("el segundo: "))
mayor = 0
menor = 0
acum = 0

if num1 > num2:
    mayor = num1
    menor = num2
elif num2 > num1:
    mayor = num2
    menor = num1
else:
    print("no ingrese 2 numeros iguales")


for i in range(menor + 1, mayor, 1):
    acum = acum + i

print(acum)