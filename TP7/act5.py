#Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error

busqueda = input("que producto estas buscando? ")

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
