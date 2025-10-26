#ACT 1
#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal

def imprimir_hola_mundo():
    return("Hola mundo!")

print(imprimir_hola_mundo())

#ACT 2
#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return(f"hola {nombre}!")

nombre = input("Dime tu nombre ")
print(saludar_usuario(nombre))

#ACT 3
#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
#dir los datos al usuario y llamar a esta función con los valores in-
#gresados
def informacion_personal(nombre, apellido, edad, residencia):
    return(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Decime tu nombre ")
apellido = input("Decime tu apellido ")
edad = int(input("Decime tu edad "))
residencia = input("Decime tu residencia ")

print(informacion_personal(nombre, apellido, edad, residencia))

#ACT 4
#Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
#dio como parámetro y devuelva el área del círculo. calcular_peri-
#metro_circulo(radio) que reciba el radio como parámetro y devuel-
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
#bas funciones para mostrar los resultados
import math

def calcular_area_circulo(radio):
    area = math.pi*(radio**2)
    return(area)

def metro_circulo(radio):
    perimetro = 2*(math.pi*radio)
    return(perimetro)

radio = float(input("Decime el radio de un circulo "))
print(f"radio: {radio} cm\narea: {calcular_area_circulo(radio)} cm\nperimetro: {metro_circulo(radio)} cm")

#ACT 5
#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos-
#trar el resultado usando esta función

def segundos_a_horas(segundos):
    return(segundos/3600)

segundos = int(input("Decime una cantidad de segundos y los convetire a horas "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

#ACT 6
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

#ACT 7
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

#ACT 8
#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
#ción para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    return round((peso/(altura**2)), 2)

print("Vamos a calcular tu Indice de Masa Corporal")
peso = float(input("Peso: "))
altura = float(input("Altura(en metros): "))
print(f"Tu IMC es {calcular_imc(peso, altura)}")

#ACT 9
#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función

def celsius_a_fahrenheit(celsius):
    return((celsius*1.8)+32)

temp = float(input("Dime una temperatura en celsius y la convertire a fahrenheit "))
print(f"{temp} celsius equivalen a {celsius_a_fahrenheit(temp)} fahrenheit")

#ACT 10
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