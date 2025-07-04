def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def mostrar_factoriales():
    num = int(input("Hasta qué número deseas calcular los factoriales?: "))
    for i in range(1, num + 1):
        print(f"Factorial de {i} es {factorial(i)}")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def mostrar_fibonacci():
    pos = int(input("Hasta qué posición deseas ver la serie Fibonacci?: "))
    for i in range(pos + 1):
        print(fibonacci(i), end=" ")
    print()


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


def convertir_binario(n):
    if n == 0:
        return ""
    else:
        return convertir_binario(n // 2) + str(n % 2)


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)


def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


# Menú principal

opciones = {
    "1": mostrar_factoriales,
    "2": mostrar_fibonacci,
    "3": lambda: print(potencia(int(input("Base: ")), int(input("Exponente: ")))),
    "4": lambda: print(convertir_binario(int(input("Número decimal: "))) or "0"),
    "5": lambda: print(es_palindromo(input("Palabra: ").lower())),
    "6": lambda: print(suma_digitos(int(input("Número: ")))),
    "7": lambda: print(contar_bloques(int(input("Bloques nivel base: ")))),
    "8": lambda: print(contar_digito(int(input("Número: ")), int(input("Dígito a contar: "))))
}

while True:
    print("\nPráctico 11: Aplicación de la Recursividad")
    print("1. Factoriales")
    print("2. Serie Fibonacci")
    print("3. Potencia Recursiva")
    print("4. Decimal a Binario")
    print("5. Verificar Palíndromo")
    print("6. Sumar Dígitos")
    print("7. Contar Bloques de Pirámide")
    print("8. Contar Dígito en Número")
    print("0. Salir")

    eleccion = input("Elegí una opción: ")

    if eleccion == "0":
        break
    elif eleccion in opciones:
        opciones[eleccion]()
    else:
        print("Opción no válida")
