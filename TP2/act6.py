
#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

from statistics import mode, median, mean
import random

numero_aleatorios = [random.randint(1,100)for i in range(50)]

moda = mode(numero_aleatorios)
mediana = median(numero_aleatorios)
media = mean(numero_aleatorios)

print(f"moda: {moda}, mediana: {mediana}, media:{media}")

if (media > mediana) and (mediana > moda):
    print("Hay un sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Hay un sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("no hay coincidencias")