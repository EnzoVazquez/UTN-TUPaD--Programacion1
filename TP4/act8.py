#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia
#notas = [[nombre, matematicas, literatura, quimica]]

notas = [["juan", 8, 5, 9], ["micaela", 7, 8, 6], ["pedro", 6, 5, 7], ["gaston", 9, 8, 6], ["florencia", 9, 10, 8]]
materias = ["matematicas", "literatura", "quimica"]
promedio = 0
acum = 0
promedio_mat =0
#mostrar promedio
for estudiante in notas :
        for i in range(1,4,1):
                acum += estudiante[i]
                promedio = acum/3
        print(f"El promedio de {estudiante[0]} es {promedio}")
        acum = 0

# mostrar promedio de cada materia
for i in range (1,4,1):
        suma = 0
        for estudiante in notas:
                suma += estudiante[i]
        
        promedio_mat = suma / len(notas)
        print(f"El promedio de {materias[i-1]} es {promedio_mat}")