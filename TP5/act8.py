#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
#ción para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    return round((peso/(altura**2)), 2)

print("Vamos a calcular tu Indice de Masa Corporal")
peso = float(input("Peso: "))
altura = float(input("Altura(en metros): "))
print(f"Tu IMC es {calcular_imc(peso, altura)}")
    