#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta-
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
#sultados de forma clara

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return(suma, resta, multiplicacion, division)

print("Dame 2 numeros y hare las operaciones basicas con ellos ")
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))

resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicacion: {resultados[2]}\nDivision: {resultados[3]}")
