#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es

def es_palindromo(palabra):
    if len(palabra) == 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            reduccion = palabra[1:-1]
            return es_palindromo(reduccion)
        else:
            return False
        
palabra = input("Dame una palabra y te dire si es un palindromo: ").strip().lower()
print(es_palindromo(palabra.replace(" ","")))