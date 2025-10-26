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