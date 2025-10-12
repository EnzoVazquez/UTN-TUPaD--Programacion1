#Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
#dio como parámetro y devuelva el área del círculo. calcular_peri-
#metro_circulo(radio) que reciba el radio como parámetro y devuel-
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
#bas funciones para mostrar los resultados
import math

def calcular_area_circulo(radio):
    area = math.pi*(radio**2)
    return(area)

def metro_circulo(radio):
    perimetro = 2*(math.pi*radio)
    return(perimetro)

radio = float(input("Decime el radio de un circulo "))
print(f"radio: {radio} cm\narea: {calcular_area_circulo(radio)} cm\nperimetro: {metro_circulo(radio)} cm")