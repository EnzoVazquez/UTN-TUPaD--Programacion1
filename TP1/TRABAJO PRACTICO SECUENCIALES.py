#TRABAJO PRACTICO SECUENCIALES

#ACTIVIDAD 1

print("hola mundo!")


#ACTIVIDAD 2

nombre = input('dime tu nombre y te saludare ')
print(f'hola! {nombre}')


#ACTIVIDAD 3

print('dame unos datos y te devolvere una oracion con los mismo')
nombre = input('decime tu nombre ')
apellido = input('decime tu apellido ')
edad = int(input('decime tu edad '))
nacionalidad = input('decime tu nacionalidad ')

print(f'Soy {nombre} {apellido}, soy {nacionalidad} y tengo {edad} años')


#ACTIVIDAD 4

radio = float(input('dime el radio de un circulo y te dire su area y perimetro'))
pi = 3.14159265359

area = pi * (radio**2)
perimetro = 2 * pi * radio

print(f'el area es {area} y el perimetro {perimetro}')


#ACTIVIDAD 5

segundos = int(input('dame una cantidad de seundo y te dire a cuantas hora equivale '))

horas = float(segundos / 3600)

print(f'{segundos} equivalen a {horas} horas')


#ACTIVIDAD 6

numero = int(input('decime un numero y te devolvere su tabla'))

uno = numero * 1
dos = numero * 2
tres = numero * 3
cuatro = numero * 4
cinco = numero * 5
seis = numero * 6
siete = numero * 7
ocho = numero * 8
nueve = numero * 9
diez = numero * 10

print(f'{numero} x 1 {uno}')
print(f'{numero} x 2 {dos}')
print(f'{numero} x 3 {tres}')
print(f'{numero} x 4 {cuatro}')
print(f'{numero} x 5 {cinco}')
print(f'{numero} x 6 {seis}')
print(f'{numero} x 7 {siete}')
print(f'{numero} x 8 {ocho}')
print(f'{numero} x 9 {nueve}')
print(f'{numero} x 10 {diez}')



#ACTIVIDAD 7

print('dame dos numeros por favor')
num1 = int(input('el primero '))
num2 = int(input('el segundo '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print('resultados:')
print(f'suma {suma}')
print(f'resta {resta}')
print(f'multiplicacion {multiplicacion}')
print(f'division {division}')


#ACTIVIDAD 8

print('vamos a sacar tu indice de masa corporal')
altura = float(input('decime tu altura '))
peso = float(input('decime tu peso '))

imc = float(peso/(altura**2))

print(f'Tu IMC es {imc}')


#ACTIVIDAD 9

celsius = int(input('decime una temperatura en celsius y la pasare a fahrenheit'))

fahrenheit = (9/5 * celsius + 32)

print(f'{celsius} celsius equivalen a {fahrenheit} fahrenheit')


#ACTIVIDAD 10

print('dame 3 numeros y te dire el promedio entre ellos')
num1 = int(input('decime el primero '))
num2 = int(input('decime el segundo '))
num3 = int(input('decime el tercero '))

promedio = (num1 + num2 + num3) / 3

print(f'el promedio es {promedio}')