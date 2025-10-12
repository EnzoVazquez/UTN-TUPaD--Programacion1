#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun-
#ción

def tabla_multiplicar(numero):
    for i in range (1,11,1):
        print(f"{i} x {numero} = {i*numero}")
pass

numero = int(input("Dame un numero y te devolvere su tabla de multiplicar "))
tabla_multiplicar(numero)