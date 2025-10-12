#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función

def calcular_promedio(a, b, c):
    total = a + b + c
    return(total/3)

print("Calculemos el promedio de 3 numeros enteros")
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))
c = int(input("Tercer numero: "))

print(f"El promedio es {calcular_promedio(a,b,c)}")