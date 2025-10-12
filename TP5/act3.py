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