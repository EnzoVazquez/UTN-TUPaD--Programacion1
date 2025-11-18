#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide

def contar_bloques(bloques, acum = 0):
    if bloques == 1:
        return acum + 1
    else:
        acum += bloques
        bloques = bloques-1
        return contar_bloques(bloques, acum)

bloques = int(input("Dime cuantos bloques tienes en el ultimo nivel y te devolvere la cantidad necesaria para armar la piramide: "))
print(f"Necesitas {contar_bloques(bloques)} bloques")