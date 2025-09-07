#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario

print("dime un numero y te devolvere la suma de todos los numeros entre 0 y el")
print("solo enteros positivos")

num = int(input())
acum = 0

if num < 0:
    print("solo numeros positivos")
else:
    for i in range (0,num,1):
        acum = acum + i

print(acum)