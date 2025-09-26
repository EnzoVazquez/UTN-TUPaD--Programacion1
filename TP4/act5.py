#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada

estudiantes = ["pedro", "maria", "santiago", "gonzalo", "mariela", "victor", "enzo"]
print(f"estudiantes: {estudiantes}")
print("Quieres: \n 1.Eliminar uno\n 2.Agregar uno")
num = int(input())
if num < 1 or num > 2 :
    print("seleccione una opcion valida")
    pass
elif num == 1 :
    borrado = input("dime que estudiante quieres eliminar: ")
    if borrado in estudiantes:
        estudiantes.remove(borrado)
        print(estudiantes)
    else:
        print(f"{borrado} no es un estudiante")
elif num == 2 :
    agregado = input("dime que estudiante quieres agregar: ")
    estudiantes.append(agregado)
    print(estudiantes)