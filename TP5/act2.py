#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return(f"hola {nombre}!")

nombre = input("Dime tu nombre ")
print(saludar_usuario(nombre))