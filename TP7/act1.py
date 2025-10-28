#Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada linea debe tener: nombre,precio,cantidad

entrada = {"remera,25000,25\n",
           "jean,30000,30\n",
           "campera,35000,20\n"}

with open("productos.txt","w") as archivo:
    archivo.writelines(entrada)