#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

aprobados_parcial1 = {113, 115, 120, 121, 137, 140}
aprobados_parcial2 = {112, 115, 117, 121, 137, 143, 150}



interseccion = aprobados_parcial1.intersection(aprobados_parcial2)
dif_simetrica = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
union = aprobados_parcial1.union(aprobados_parcial2)

print(f"Los alumnos que que aprobaron ambos son: {interseccion}")
print(f"Los alumnos que aprobaron solo uno son {dif_simetrica}")
print(f"lista total de estudiantes que aprobaron al menos uno {union}")
