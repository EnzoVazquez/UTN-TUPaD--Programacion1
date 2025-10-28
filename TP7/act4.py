#Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad

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


print(productos)