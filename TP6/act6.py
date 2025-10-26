#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos = {}

while len(alumnos) < 3:
    alumno = input("Dime el nombre del alumno ")
    if alumno in alumnos:
        print("Alumno ya ingresado ")
        continue
    else:
        nota1 = int(input("Dame la primera nota "))
        nota2 = int(input("Dame la primera nota "))
        nota3 = int(input("Dame la primera nota "))
        if 0 > nota1 or nota1 > 10 or 0 > nota2 or nota2 > 10 or 0 > nota3 or nota3> 10:
            print("alguna de las notas ingresadas no es correcta")
            continue
        else: 
            notas = (nota1, nota2, nota3)
            alumnos[alumno] = notas

print(f"Las notas son: {alumnos}")

for i in alumnos:
    notas = alumnos[i]
    promedio = sum(notas) / 3
    print(f"El promedio de {i} es {promedio}")

            