#ACT 1
#Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#ACT 2
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#ACT 3
#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios

precios_frutas = {'Banana': 1300, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

keys = precios_frutas.keys()

frutas = list(keys)

print(frutas)

#ACT 4
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
    print(f"El numero de {consulta} es {guia[consulta]}")
else:
    print("No tenemos el numero en la lista")

#ACT 5
#Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Dime una frase ")

frase_desc = frase.split()
palabras_unicas = set()
repeticiones = {}

for i in frase_desc:
    if i not in palabras_unicas:
        repeticiones[i] = 1
        palabras_unicas.add(i)
    else:
        repeticiones[i] += 1


print(f"Las palabras unicas son: {palabras_unicas}")
print(f"Cantidad de veces que aparece cada palabra: {repeticiones}")

#ACT 6
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

#ACT 7
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


#ACT 8
#Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

productos = {"remeras": 3, "pantalones": 7, "bermudas": 6, "buzos": 5}

while True:
    menu = int(input("1. consultar stock\n2. agregar unidades a un producto\n3. agregar un producto\n4. salir "))
    if 1 <= menu <= 4:
        match menu:
            case 1:
                print(productos)

            case 2:
                entrada = input("A que producto le quieres agregar unidades? ")
                item = entrada.lower()
                if item not in productos:
                   print("No contamos con el producto")
                   continue

                else:
                    cant = int(input("Que cantidad quieres añadir? "))
                    productos[item] += cant
                    print(f"Stock actualizado! hay {productos[item]} {item} en existencia")
            
            case 3:
                entrada = input("Que producto quieres agregar? ")
                item = entrada.lower()
                if item in productos:
                    print("Ya contamos con ese producto en nuestro stock")
                    continue
                else:
                    stock = int(input("Que cantidad? "))
                    productos[item] = stock
                    print(f"{item} agregado con exito!")
            case 4:
                print("Adios!")
                break
    else:
        print("valor incorrecto")

#ACT 9
#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00"): "Medico",
    ("martes","12:00") : "almuerzo afuera",
    ("miercoles", "16:00") : "futbol",
    ("jueves", "20:00") : "parcial",
    ("viernes", "15:00") : "estudiar"
}

entrada_dia = input("Que dia de la semana quieres consultar? ")
dia = entrada_dia.lower()
hora = input("A que horario? ")

consulta = (dia, hora)

if consulta in agenda:
    print(f"tienes {agenda[consulta]}")
else:
    print("No tienes planes")

#ACT 10
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