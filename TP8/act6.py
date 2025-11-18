#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(num, acum = 0):
    if num == 0:
        return acum
    else:
        ultimo = num % 10
        actualizacion = num // 10
        acum += ultimo
        return suma_digitos(actualizacion, acum)

num = int(input("Dame un numero y sumare todos sus elementos: "))
print(suma_digitos(num))