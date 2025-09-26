#Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_unicos = []
for num in datos :
    if num not in datos_unicos:
        datos_unicos.append(num)

print(datos)
print(datos_unicos)