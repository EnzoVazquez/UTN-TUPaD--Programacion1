#Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
guia = {}

while len(guia) < 5:

    nombre = input("Decime el nombre a agendar ")
    if nombre in guia:
        numero_contacto = guia[nombre]
        print(f"El contacto ya existe en la lista! con el numero {numero_contacto}")
        continue
    else:
        numero = int(input("Decime su numero de telefono "))   
        if numero in guia.values():
            print(f"El numero ya se encuentra asociado en la guia")
            continue
        else:
            guia[nombre] = numero
            print(f"{nombre} agregado correctamente!")
            print(guia)

consulta = input("De quien quieres saber el numero?")

if consulta in guia:
    print(f"El numero de consulta es {guia[consulta]}")
else:
    print("No tenemos el numero en la lista")