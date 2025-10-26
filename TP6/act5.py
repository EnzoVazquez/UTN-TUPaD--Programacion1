#Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Dime una frase ")

frase_desc = frase.split()
palabras_unicas = set()
repeticiones = {}

for i in frase_desc:
    if i not in palabras_unicas:
        repeticiones[i] = 1
        palabras_unicas.add(i)
    else:
        repeticiones[i] += 1


print(f"Las palabras unicas son: {palabras_unicas}")
print(f"Cantidad de veces que aparece cada palabra: {repeticiones}")