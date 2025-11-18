#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num
    
def factorial_multiple(num):
    if num >= 1:
        print(factorial(num))
        factorial_multiple(num-1)
    
    
entrada = int(input("Dame un numero entero y te mostrare el factorial de todos los numeros entre el y 1: "))

factorial_multiple(entrada)