import csv
import os

#funcion para crear el archivo csv
def crear():
    with open("catalogo.csv","w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=["titulo","cantidad"])
        escritor.writeheader()
        return

#funcion que trae el catalogo del archivo csv
def leer():
    catalogo = []
    with open("catalogo.csv", newline="",encoding="utf-8" ) as archivo:
        lineas = csv.DictReader(archivo)
        for linea in lineas:
            catalogo.append({"titulo":linea["titulo"],"cantidad":int(linea["cantidad"])})

        return catalogo

#Funcion que agrega el libro al archivo csv
def agregar(item):
    with open("catalogo.csv","a",newline="",encoding="utf-8") as catalogo:
        escritor = csv.DictWriter(catalogo, fieldnames=["titulo","cantidad"])
        escritor.writerow(item)
        print(f"{item["titulo"]} agregado correctamente!")

#funcion para agregar un solo libro
def agregar_uno():
    titulo = input("Titulo: ").strip().lower()
    stock = int(input("Cantidad: "))
    if validar_numero(stock):
        print("No se puede agregar cantidades negativas")
    else:
        if validar_repetido(titulo):
            print("El libro ya se encuentra en stock")
        else:
            agregar({"titulo":titulo,"cantidad":stock})

#Funcion para agregar varios libros
def agregar_varios():
    cantidad = int(input("Cuantos libros quieres ingresar? "))
    if validar_numero(cantidad):
            print("Cantidad no valida")
    else:
        for i in range(0,cantidad,1):
            titulo = input("Titulo: ").strip().lower()
            stock = int(input("Cantidad: "))
            if validar_numero(stock):
                print("No se puede agregar cantidades negativas")
                continue
            else:
                if validar_repetido(titulo):
                    print("El libro ya se encuentra en stock")
                else:
                    agregar({"titulo":titulo,"cantidad":stock})

#funcion para validar si el libro no esta en el catalogo
def validar_repetido(titulo):
    catalogo = leer()

    for libro in catalogo:
        if libro["titulo"] == titulo.strip().lower():
            return True
        
    return False

#Funcion que sobreescribe el catalogo actualizado
def guardar_catalogo(actualizado):
    with open("catalogo.csv","w",newline="",encoding="utf-8") as catalogo:
        escritor = csv.DictWriter(catalogo, fieldnames=["titulo","cantidad"])
        escritor.writeheader()
        escritor.writerows(actualizado)

#crear funcion que traiga todos los libros, actualize la cantidad de uno y vuelva a reescribir todo el archivo("w")
def actualizar_stock():
    catalogo = leer()
    libro = input("ingrese el titulo al que desea agregar ejemplares ").strip().lower()
    encontrado = False

    for item in catalogo:
        if libro == item["titulo"]:
            cantidad = int(input("Que cantidad quieres agregar? "))
            if validar_numero(cantidad):
                print("No se permiten cantidades negativas")
                return
            else:
                item["cantidad"] += cantidad
                guardar_catalogo(catalogo)
                print(f"stock actualizado con exito! {item["titulo"]} ahora tiene {item["cantidad"]} ejemplares")
                encontrado = True
                continue

    if not encontrado:
            print("No tenemos ese titulo")      

#funcion para buscar un libro
def buscar_libro():
    catalogo = leer()
    libro = input("Que libro estas buscando? ").strip().lower()
    encontrado = False

    for item in catalogo:
        if libro == item["titulo"]:
            encontrado = True
            if item["cantidad"] == 0:
                print(f"Tenemos {item["titulo"]} en la biblioteca, pero no hay stock en este momento")
            else:
                print(f"{item["titulo"]} esta disponible! quedan {item["cantidad"]} ejemplares")
    if not encontrado:
            print("No tenemos ese titulo") 

#funcion que devuelve los libros con cantidad 0
def agotados():
    catalogo = leer()
    agotados = []
    for libro in catalogo:
        if libro["cantidad"] == 0:
            agotados.append(libro["titulo"])

    if len(agotados) == 0:
        print("No hay titulos agotados!")
    else:
        print("Libros agotados:")
        print(agotados)

#funcion para validar que los numeros sean mayores a 0
def validar_numero(numero):
    if numero < 0:
        return True
    else:
        return False

#funcion para el manejo de stock en caso de retiro   
def retirar():
    catalogo = leer()
    retiro = input("Que libro quieres retirar? ").strip().lower()
    encontrado = False

    for libro in catalogo:
        if libro["titulo"] == retiro:
            if libro["cantidad"] == 0:
                print("lo sentimos, no quedan ejemplares en stock")
                encontrado = True
            else:
                libro["cantidad"] -= 1
                guardar_catalogo(catalogo)
                print(f"{retiro} retirado con exito! quedan {libro["cantidad"]} unidades en stock")
                encontrado = True
    
    if not encontrado:
        print("No contamos con ese titulo en la biblioteca")

#funcion para el manejo de stock en caso de devolucion
def devolver():
    catalogo = leer()
    devolucion = input("Que libro quieres devolver? ").strip().lower()
    encontrado = False

    for libro in catalogo:
        if libro["titulo"] == devolucion:
            libro["cantidad"] += 1
            guardar_catalogo(catalogo)
            print(f"{devolucion} devuelto con exito! quedan {libro["cantidad"]} unidades en stock")
            encontrado = True
    
    if not encontrado:
        print("Ese libro no pertenece a la biblioteca")
    
#Menu y sus funcionalidades
while True:

    #Ve si existe la base de datos, y si no, la crea
    if os.path.exists("catalogo.csv"):
        pass
    else:
        crear()

    menu = int(input("MENU\n1.Ingresar titulos\n2.Ingresar ejemplares de un libro\n3.Mostrar catalogo\n4.Buscar libro\n5.Titulos agotados\n6.Agregar un libro\n7.Prestamos/Devoluciones\n8.Salir\n"))
    if 1<= menu <=8:
        match menu:
            case 1:
                agregar_varios()
            case 2:
                actualizar_stock()
            case 3:
                catalogo = leer()
                print("****CATALOGO DE LIBROS****")
                print(catalogo)
            case 4:
                buscar_libro()
            case 5:
                agotados()
            case 6:
                agregar_uno()
            case 7:
                submenu = int(input("1.Retirar un libro\n2.Devolver un libro\n"))
                if 1<=submenu<=2:
                    match submenu:
                        case 1:
                            retirar()
                        case 2:
                            devolver()
                else:
                    print("Opcion invalida")
            case 8:
                print("adios!")
                break

    else:
        print("Valor incorrecto")