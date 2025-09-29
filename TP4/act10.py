#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.
ventas = [[8, 12, 2, 6], [10, 16, 7, 6], [11, 8, 9, 3], [11, 25, 4, 14], [14, 5, 6, 13], [12, 4, 8, 14], [13, 10, 11, 9]]
count = 0
acum = 0
record = 0
producto = 0
productos = ["manzana", "banana", "pera", "naranja"]
#mostrar el total vendido de cada producto y el mas vendido de la semana
for c in range (0,4,1):
    for i in range(0,7,1):
        venta_semana = ventas[i][c]
        acum += venta_semana
    match c: 
        case 0:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0
        case 1:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0
        case 2:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0
        case 3:
            print(f"Esta semana vendimos {acum} {productos[c]}")
            if acum > record:
                record = acum
                producto = c
            acum = 0

print(f"El producto mas vendido esta semana fue {productos[producto]} con {record} unidades")
#mostrar el dia con mayores ventas
for e in range (7):
    total_dia = 0
    record_ventas = 0
    dia_mayor = 0
    for i in range (4):
        total_dia += ventas[e][i]
    if total_dia > record_ventas:
        record_ventas = total_dia
        dia_mayor = e

print(f"El dia de mayor ventas el fue el dia {dia_mayor}, con un total de {record_ventas} ventas")
        
    

