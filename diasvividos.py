from datetime import datetime
while True:
    try:
        # Solicitar la fecha de nacimiento al usuario
        nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
        # Convertir la cadena a un objeto datetime
        fecha_nacimiento = datetime.strptime(nacimiento, "%d/%m/%Y")
        break
    except ValueError:
        print("Formato incorrecto. Por favor, introduce la fecha en el formato dd/mm/aaaa.")
hoy = datetime.now()

dias = (hoy - fecha_nacimiento).days
print(dias)