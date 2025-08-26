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