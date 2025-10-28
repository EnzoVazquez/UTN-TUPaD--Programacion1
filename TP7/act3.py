#Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        producto = linea.strip().split(",")
        print(f"Producto: {producto}")

print("Agreguemos un nuevo producto")
nombre = input("Que producto deseas agregar? ")
precio = int(input("que precio? "))
cantidad = int(input("cual es el stock? "))

producto_nuevo = f"{nombre},{precio},{cantidad}\n"

with open("productos.txt", "a") as archivo:
    archivo.write(producto_nuevo)
