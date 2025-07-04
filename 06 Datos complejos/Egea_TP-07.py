def punto1(precios_frutas):
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    print(precios_frutas)


def punto2(precios_frutas):
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    print(precios_frutas)


def punto3(precios_frutas):
    frutas = list(precios_frutas.keys())
    print(frutas)


def punto4():
    contactos = {}
    for _ in range(5):
        nombre = input("Nombre del contacto: ")
        numero = input("Número de teléfono: ")
        contactos[nombre] = numero

    consulta = input("¿De quién querés el número?: ")
    print(contactos.get(consulta, "No existe ese contacto"))


def punto5():
    frase = input("Ingresá una frase: ").lower()
    palabras = frase.split()
    palabras_unicas = set(palabras)
    print("Palabras únicas:", palabras_unicas)

    conteo_palabras = {}
    for palabra in palabras:
        conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
    print("Conteo de palabras:", conteo_palabras)


def punto6():
    alumnos = {}
    for _ in range(3):
        nombre = input("Nombre del alumno: ")
        notas = tuple(float(input(f"Nota {i+1} para {nombre}: ")) for i in range(3))
        alumnos[nombre] = notas

    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: promedio {promedio:.2f}")


def punto7():
    parcial1 = {int(x) for x in input("Aprobados Parcial 1 (separados por espacio): ").split()}
    parcial2 = {int(x) for x in input("Aprobados Parcial 2 (separados por espacio): ").split()}

    print("Aprobaron ambos:", parcial1 & parcial2)
    print("Aprobaron solo uno:", parcial1 ^ parcial2)
    print("Aprobaron al menos uno:", parcial1 | parcial2)


def punto8():
    stock = {}
    while True:
        producto = input("Producto a consultar (0 para salir): ")
        if producto == "0":
            break
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]}")
            agregar = int(input("Cuántas unidades querés agregar?: "))
            stock[producto] += agregar
        else:
            nuevo_stock = int(input("Producto no existe. Ingresá stock inicial: "))
            stock[producto] = nuevo_stock
        print(stock)


def punto9():
    agenda = {}
    while True:
        accion = input("1. Agregar evento 2. Consultar evento 0. Salir: ")
        if accion == "1":
            dia = input("Día: ")
            hora = input("Hora: ")
            evento = input("Evento: ")
            agenda[(dia, hora)] = evento
        elif accion == "2":
            dia = input("Consultar día: ")
            hora = input("Consultar hora: ")
            print(agenda.get((dia, hora), "Sin actividad"))
        elif accion == "0":
            break


def punto10():
    paises = {'Argentina': 'Buenos Aires', 'Francia': 'París', 'Japón': 'Tokio'}
    capitales = {capital: pais for pais, capital in paises.items()}
    print(capitales)


# Menú Principal
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

opciones = {
    "1": lambda: punto1(precios_frutas),
    "2": lambda: punto2(precios_frutas),
    "3": lambda: punto3(precios_frutas),
    "4": punto4,
    "5": punto5,
    "6": punto6,
    "7": punto7,
    "8": punto8,
    "9": punto9,
    "10": punto10
}

while True:
    print("\nPráctico 6: Estructuras de Datos Complejas")
    print("1. Agregar frutas y precios")
    print("2. Actualizar precios")
    print("3. Listar frutas")
    print("4. Agenda telefónica")
    print("5. Palabras únicas y conteo")
    print("6. Notas de alumnos y promedio")
    print("7. Análisis de aprobados")
    print("8. Control de stock")
    print("9. Agenda de eventos")
    print("10. Invertir diccionario de países")
    print("0. Salir")

    eleccion = input("Elegí una opción: ")

    if eleccion == "0":
        break
    elif eleccion in opciones:
        opciones[eleccion]()
    else:
        print("Opción no válida")
