#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número

def contar_digito(numero, digito, acum = 0):
    if numero == 0:
        return acum
    else:
        item = numero % 10
        actualizacion = numero // 10
        if item == digito :
            acum += 1
            return contar_digito(actualizacion, digito, acum)
        else:
            return contar_digito(actualizacion, digito, acum)
        
print("Dame un numero y un digito y te dire cuantas veces aparece este en el numero")
numero = int(input("Dame el numero primero: "))
digito = int(input("Ahora dame el digito que deseas contar: "))

if 0<= digito <= 9:
    print(f"El numero {digito} aparece {contar_digito(numero, digito)} veces en {numero}")
else:
    print("El digito tiene que estar entre 0 y 9")