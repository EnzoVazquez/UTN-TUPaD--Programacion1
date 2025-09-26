#Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja

notas = [9.5, 6.8, 7.3, 4.2, 7.2, 8.0, 7.8, 8.2, 6.3, 8.5]
cantidad = len(notas)
acum = 0
max = float("-inf")
min = float("inf")
#mostar listar completas
print(notas)
#calcular el promedio 
for i in range (0,cantidad,1):
    num = notas[i]
    acum += num

prom = acum / cantidad
print(f"El promedio de las notas es {prom}")
#calcular la nota mas alta y mas baja
for i in range (0,cantidad,1):
    num = notas[i]
    if num > max :
        max = num
    elif num < min :
        min = num
    else :
        pass

print(f"la nota mas alta fue {max}, y la mas baja {min}")