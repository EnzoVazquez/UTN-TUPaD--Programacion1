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