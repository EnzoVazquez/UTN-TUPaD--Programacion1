#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("ingresa 10 numeros y te dire cuantos pares, cuantos impares, cuantos negativos y cuantos positivos ingresaste")

vueltas = 10
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range (0,vueltas,1):

    num = int(input("ingrese un valor "))

    if num >= 0:
        positivos = positivos + 1
        if num%2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    else:
        negativos = negativos + 1
        if num%2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1

print(f"pares: {pares}")
print(f"impares: {impares}")
print(f"positivos: {positivos}")
print(f"negativos: {negativos}")