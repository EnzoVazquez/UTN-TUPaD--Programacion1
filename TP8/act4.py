#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto
import math


def pasaje_binario(num):
    if num == 0:
        return ""
    else:
        return pasaje_binario(num // 2) + str(num % 2)
    
numero = int(input("Dame un numero y lo convertire a binario: "))
print(pasaje_binario(numero))