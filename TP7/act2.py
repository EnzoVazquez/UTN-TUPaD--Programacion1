#Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        print(f"Producto: {producto}")