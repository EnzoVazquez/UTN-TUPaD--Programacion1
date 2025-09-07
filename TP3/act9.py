#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

print("dime 10 numeros y te calculare la media")

vueltas = 10
acum = 0
media = 0

for i in range (0,vueltas,1):
    num = int(input("ingrese un numero "))
    acum = acum + num

media = acum / vueltas
print(f"La media es: {media}")