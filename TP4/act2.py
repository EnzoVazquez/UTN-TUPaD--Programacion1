#Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#pedir al usuario que cargue 5 productos
productos = []
cont = 0
control = False

while cont < 5 :
    item = input("Ingrese un producto: ")
    productos.append(item.lower())
    cont += 1

#mostrar la lista ordenada alfabeticamente
print(sorted(productos))

#preguntar al usuario que producto desea eliminar
while control == False:

    deleted = input("Dime que producto quiere eliminar: ")
    if deleted in productos :
        productos.remove(deleted.lower())
        print (f"{deleted} eliminado/a con exito!")
        control = True
    else :
        print(f"{deleted} no esta entre tus productos")
