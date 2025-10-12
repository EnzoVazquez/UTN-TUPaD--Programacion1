#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos-
#trar el resultado usando esta función

def segundos_a_horas(segundos):
    return(segundos/3600)

segundos = int(input("Decime una cantidad de segundos y los convetire a horas "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")