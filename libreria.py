import unicodedata
import time
import sys

def imprimir_con_retraso(texto, retraso=0.1):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(retraso)
    print()

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower())
        if unicodedata.category(c) != 'Mn'
    )

libros = [
    {"titulo": "Habitos Atomicos", "autor": "James Clear", "categoria": "Autoayuda", "disponible": True},
    {"titulo": "Los secretos de la mente millonaria", "autor": "T. Harv Eker", "categoria": "Finanzas", "disponible": True},
    {"titulo": "Padre Rico Padre Pobre", "autor": "Robert Kiyosaki", "categoria": "Educacion Financiera", "disponible": True},
    {"titulo": "El Elemento", "autor": "Ken Robinson", "categoria": "Desarrollo Personal", "disponible": True},
    {"titulo": "It", "autor": "Stephen King", "categoria": "Terror", "disponible": True}
]

prestamos_usuario = []

def mostrar_libros(lista):
    if not lista:
        print("No hay libros para mostrar.",)
        return
    for idx, libro in enumerate(lista, start=1):
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"{idx}. {libro['titulo']} - {libro['autor']} ({libro['categoria']}) - {estado}")

def buscar_titulo():
    termino = input("Ingresa el título a buscar: ")
    normal = normalizar(termino)
    resultados = [libro for libro in libros if normal in normalizar(libro["titulo"])]
    print("\nResultados de búsqueda:")
    mostrar_libros(resultados)

def buscar_categoria():
    termino = input("Ingresa la categoría: ")
    normal = normalizar(termino)
    resultados = [libro for libro in libros if normal in normalizar(libro["categoria"])]
    print("\nResultados por categoría:")
    mostrar_libros(resultados)

def prestar_libro():
    disponibles = [libro for libro in libros if libro["disponible"]]
    if len(prestamos_usuario) >= 3:
        print("Solo puedes prestar hasta 3 libros.")
        return
    if not disponibles:
        print("No hay libros disponibles.")
        return
    print("\nLibros disponibles:")
    mostrar_libros(disponibles)
    try:
        opcion = int(input("Elige el número del libro a prestar: ")) - 1
        if 0 <= opcion < len(disponibles):
            libro = disponibles[opcion]
            libro["disponible"] = False
            prestamos_usuario.append(libro)
            print(f"Has prestado: '{libro['titulo']}'")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada no válida.")

def devolver_libro():
    if not prestamos_usuario:
        print("No tienes libros para devolver.")
        return
    print("\nLibros que puedes devolver:")
    mostrar_libros(prestamos_usuario)
    try:
        opcion = int(input("Elige el número del libro que deseas devolver: ")) - 1
        if 0 <= opcion < len(prestamos_usuario):
            libro = prestamos_usuario.pop(opcion)
            libro["disponible"] = True
            print(f"Has devuelto: '{libro['titulo']}'")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada no válida.")

def ver_prestamos():
    print("\nTus libros prestados:")
    mostrar_libros(prestamos_usuario)

def agregar_libro():
    titulo = input("Ingresa el título del libro: ").strip()
    autor = input("Ingresa el autor: ").strip()
    categoria = input("Ingresa la categoría: ").strip()
    if titulo == "" or autor == "" or categoria == "":
        print("Todos los campos son obligatorios.")
        return
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "disponible": True
    }
    libros.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado correctamente y disponible para préstamo.")

def mostrar_menu():
    print("\n--- Biblioteca Virtual ---")
    print("1. Ver todos los libros")
    print("2. Buscar libro por título")
    print("3. Buscar libro por categoría")
    print("4. Prestar un libro")
    print("5. Ver libros prestados")
    print("6. Devolver un libro")
    print("7. Agregar un libro nuevo")
    print("8. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-8): ")

    if opcion == "1":
        imprimir_con_retraso("\nLista completa de libros:\n", 0.01)
        mostrar_libros(libros)
    elif opcion == "2":
        buscar_titulo()
    elif opcion == "3":
        buscar_categoria()
    elif opcion == "4":
        prestar_libro()
    elif opcion == "5":
        ver_prestamos()
    elif opcion == "6":
        devolver_libro()
    elif opcion == "7":
        agregar_libro()
    elif opcion == "8":
        imprimir_con_retraso("Saliendo de la biblioteca.......", 0.1)
        break
    else:
        print("Opción no válida.")
