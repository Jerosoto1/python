# Crea un diccionario de estudiantes donde las claves sean los nombres y los valores sus notas finales.
# Después imprime los nombres de los estudiantes que aprobaron (nota mayor o igual a 6)

estudiante = {
    "cristian": 11,
    "juan": 6,
    "jero": 13,
    "almamaria": 9,
    "isaac": 8
}

print(estudiante)

for nombre, nota in estudiante.items():
    if nota >= 6 and nota <= 10:
        print(f"MAQUINAAA {nombre}")

        