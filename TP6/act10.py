#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

paises = {"argentina":"buenos aires", "chile":"santiago", "brazil" : "brasilia", "ecuador":"quito"}
paises_invertido = {}

for i in paises:
    pais = i
    capital = paises[i]
    paises_invertido[capital] = i

print(paises)
print(paises_invertido)