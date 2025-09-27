#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica
temperaturas = [[7.5, 15.6], [6.2, 14.8], [8.0, 18.2], [7.5, 17.3], [6.8, 16.4], [7.2, 18.4], [8.3, 19.5]]
maximas = 0
minimas = 0
indice = len(temperaturas)
prom_maximas = 0
prom_minimas = 0
amplitud = 0
max_amplitud = float("-inf")
dia_amplitud = 0
#calcular promedios
for temperatura in temperaturas:
    minimas += temperatura[0]
    maximas += temperatura[1]

prom_maximas = maximas/indice
prom_minimas = minimas/indice
print(f"El promedio de las temperaturas minimas es {prom_minimas:.2f}\nEl promedio de las temperaturas maximas es {prom_maximas:.2f}")

#mostrar dia con mayor amplitud termica
for temperatura in temperaturas:
    amplitud = temperatura[1] - temperatura[0]
    if amplitud > max_amplitud:
        dia_amplitud = temperatura
        max_amplitud = amplitud
    else:
        pass
print(f"La mayor amplitud termica fue el dia que se registro {dia_amplitud}, con una amplitud de {max_amplitud}")