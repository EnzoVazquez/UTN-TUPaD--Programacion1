#Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista

def leer_stock():
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            producto = linea.strip().split(",")
            print(f"Producto: {producto}")

def buscar_producto(busqueda):
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
        productos = []
        for linea in lineas:
            producto = linea.strip().split(",")
            item = {}
            item["nombre"] = producto[0]
            item["precio"] = producto[1]
            item["cantidad"] = producto[2]
            productos.append(item)

        for producto in productos:
            if producto["nombre"] == busqueda:
                print(f"{producto}")
                break
        else:
            print("No contamos con ese producto")

def subir_productos(productos_agregar):
    with open("productos.txt", "a") as archivo:
        archivo.writelines(productos_agregar)

productos_agregar = []

while True:
    print("MENU\n1. ver stock\n2. buscar producto\n3. agregar producto\n4. guardar y salir")
    menu = int(input("Que operacion quieres realizar?"))

    if 1 <= menu <= 4:
        match menu:
            case 1:
                leer_stock()
            case 2:
                busqueda = input("que producto estas buscando? ")
                buscar_producto(busqueda)
            case 3:
                nombre = input("Que producto deseas agregar? ")
                precio = int(input("que precio? "))
                cantidad = int(input("cual es el stock? "))
                producto_nuevo = f"{nombre},{precio},{cantidad}\n"
                productos_agregar.append(producto_nuevo)
            case 4:
                print(f"Los productos nuevos son:\n{productos_agregar}")
                subir_productos(productos_agregar)
                print("Productos cargados con exito! Adios")
                break
    
    else:
        print("valor incorrecto")
