libros = ["1984", "cien años de soledad", "el señor de los anillos: la comunidad del anillo", "crimen y castigo", "rayuela", "fahrenheit 451", "orgullo y prejuicio"]
ejemplares = [7, 15, 12, 0, 11, 0, 3]

while True:

    print("Menu de la biblioteca")
    print("1. agregar un libro\n" \
    "2. agregar ejemplares\n" \
    "3. mostrar libros y ejemplares disponibles\n" \
    "4. buscar un titulo\n" \
    "5. titulos agotados\n" \
    "6. agregar libro con su stock \n" \
    "7. retirar/devolver un libro\n" \
    "8. salir")
    menu = int(input())

    if 1 <= menu <= 8:
        match menu:
            #Ingresar libros con stock 0
            case 1:
                entrada = input("dime el titulo: ")
                libro = entrada.lower()
                if libro in libros:
                    print("El libro ya esta en la biblioteca, puede devolverlo con la opcion 7")
                else :
                    libros.append(libro)
                    ejemplares.append(0)
                    indice = libros.index(libro)
                    print(f"¡{libro} ingresado correctamente! esta en el puesto {indice} de la lista")
            #actualizar ejemplares a libros de la biblioteca
            case 2:
                for i, titulo in enumerate(libros):
                        print(i, titulo)
                entrada = input("¿de que libro quieres actualizar stock? ")
                libro = entrada.lower()
                if not libro in libros :
                    print("No tenemos ese libro en la biblioteca, si quieres agregarlo usa la opcion 1")
                else:
                    stock = int(input("dime el stock actualizado "))
                    indice = libros.index(libro)
                    ejemplares[indice] = stock
                    print(f"stock actualizado a {stock}")
            #mostrar los libros
            case 3:
                stock = len(libros)
                for i in range(0,stock,1):
                    libro = libros[i]
                    unidades = ejemplares[i]
                    print(f"libro: {libro}\n stock: {unidades}\n")
            #buscar un libro
            case 4:
                entrada = input("¿que titulo buscas?")
                libro = entrada.lower()
                if libro in libros:
                    indice = libros.index(libro)
                    stock = ejemplares[indice]
                    if stock == 0 :
                        print(f"En este momento no quedan copias de {libro}")
                    else :
                        print(f"{libro} esta disponible en el indice {indice}, quedan {stock} ejemplares")
                else :
                    print(f"No tenemos {libro} en la biblioteca")
            #mostrar libros agotados
            case 5:
                indices =[]
                for i, valor in enumerate(ejemplares):
                    if valor == 0:
                        indices.append(i)
                for indice in indices:
                    libro = libros[indice]
                    print(f"{libro} esta agotado")
            #añadir un libro especificando ejemplares
            case 6:
                entrada = input("¿que titulo deseas añadir?")
                libro = entrada.lower()
                if libro in libros:
                    print("!ya tenemos ese titulo en la biblioteca¡")
                else:
                    stock = int(input("cuantas unidades?"))
                    libros.append(libro)
                    ejemplares.append(stock)
                    indice = libros.index(libro)
                    print(f"Libro añadido con exito! indice: {indice}")
            #retirar/devolver un libro
            case 7:
                operacion = int(input("1. Retirar\n2. Devolver\n"))
                if operacion == 1:
                    for i, titulo in enumerate(libros):
                        print(i, titulo)
                    pedido = int(input("Dime el indice del libro quieres retirar "))
                    libro = libros[pedido]
                    stock = ejemplares[pedido]
                    if stock == 0:
                        print(f"Lo siento, no quedan ejemplares de {libro}")
                    else :
                        ejemplares[pedido] = stock - 1
                        print(f"{libro} retirado con exito! quedan {stock} unidades aún")
                elif operacion == 2:
                    for i, titulo in enumerate(libros):
                        print(i, titulo)
                    pedido = int(input("Dime el indice del libro que quieres devolver "))
                    stock = ejemplares[pedido]
                    libro = libros[pedido]
                    ejemplares[pedido] = stock + 1
                    print(f"Gracias por su devolucion!{libro} devuelto con exito, hay {ejemplares[pedido]} disponibles!")
            #salir
            case 8:
                print("Hasta luego!")
                break
    else :
        print("valor incorrecto")