#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00"): "Medico",
    ("martes","12:00") : "almuerzo afuera",
    ("miercoles", "16:00") : "futbol",
    ("jueves", "20:00") : "parcial",
    ("viernes", "15:00") : "estudiar"
}

entrada_dia = input("Que dia de la semana quieres consultar? ")
dia = entrada_dia.lower()
hora = input("A que horario? ")

consulta = (dia, hora)

if consulta in agenda:
    print(f"tienes {agenda[consulta]}")
else:
    print("No tienes planes")