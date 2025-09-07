#ACT1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

ES_MAYOR = 18

edad = int(input("Dime tu edad "))

if edad >= ES_MAYOR:
    print("Usted es mayor de edad")
else:
    print("Lo siento, tu no eres mayor de edad")


#ACT2
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

NOTA_APROBADO = 6

nota = int(input("Dime tu nota y te dire si aprobaste "))

if nota >= NOTA_APROBADO:
    print("Aprobado")
else:
    print("Lo siento, desaprobado")


#ACT3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar

numero = int(input("Dame un numero y te dire si es par "))

if numero % 2 == 0:
    print(f"el numero {numero} es par")
else:
    print(f"el numero {numero} es impar")


#ACT4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Dime tu edad "))

if edad <= 0:
    print("Introduzca una edad valida")
elif edad <= 12:
    print("usted es un niño/a")
elif edad > 12 and edad <= 18:
    print("Usted es un adolescente")
elif edad > 18 and edad <= 30:
    print("usted es un adulto/a joven")
else:
    print("usted es un adulto/a")


#ACT5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string

LONG_MIN = 8
LONG_MAX = 14

contraseña = input("Ingrese una contraseña ")

long = len(contraseña)

if long >= 8 and long <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#ACT6
#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

from statistics import mode, median, mean
import random

numero_aleatorios = [random.randint(1,100)for i in range(50)]

moda = mode(numero_aleatorios)
mediana = median(numero_aleatorios)
media = mean(numero_aleatorios)

print(f"moda: {moda}, mediana: {mediana}, media:{media}")

if (media > mediana) and (mediana > moda):
    print("Hay un sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Hay un sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("no hay coincidencias")

#ACT7
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

palabra = input("Dime una palabra o frase y si termina en vocal le añadire '!' ")

ultima = palabra[-1].lower()

if ultima == "a" or ultima == "e" or ultima == "i" or ultima == "o" or ultima == "u":
    print(f"{palabra} !")
else:
    print("No termina en vocal")


#ACT8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro

nombre = input("Decime tu nombre ")

print("Dime como quieres que devuelva tu nombre")
print("1. Tu nombre en mayúsculas. Por ejemplo: PEDRO")
print("2. Tu nombre en minúsculas. Por ejemplo: pedro")
print("3. Tu nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

num = int(input())

if num == 1:
    mayus = nombre.upper()
    print(mayus)
elif num == 2:
    minus = nombre.lower()
    print(minus)
elif num == 3:
    p_mayus = nombre.title()
    print(p_mayus)
else:
    print("opcion inexistente")

#ACT9
#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

magnitud = float(input("Dime la magnitud del terremoto "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")


#ACT10
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano

print("Vamos a ver en que estacion estas ")
hemisferio = input("Dime en que hemisferio te encuentra(N o S) ")
mes = input("Dime en que mes estas ").lower()
dia = int(input("Dime el dia "))

if hemisferio == "n" or hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Invierno")
    elif(mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia <= 20):
        print("primavera")
    elif(mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("verano")
    elif(mes == "septiembre" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print("otoño")
    else:
        print("ha ocurrido un error")
elif hemisferio == "s" or hemisferio == "S":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia <= 20):
        print("Verano")
    elif(mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia <= 20):
        print("Otoño")
    elif(mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print("Invierno")
    elif(mes == "septiembre" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print("Primavera")
    else:
        print("ha ocurrido un error")
else:
    print("Seleccione una opcion valida")