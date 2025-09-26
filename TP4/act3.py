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