import math

# Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Ejercicio 2

def saludar_usuario():
    nombre = input("Dime tu nombre: ")
    print(f"Hola {nombre}!")

# Ejercicio 3

def informacion_personal():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4

def calcular_area_perimetro_circulo():
    radio = float(input("Dime el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")

# Ejercicio 5

def segundos_a_horas():
    segundos = int(input("Dime una cantidad de segundos: "))
    horas = segundos / 3600
    print(f"Equivalente en horas: {horas:.2f}")

# Ejercicio 6

def tabla_multiplicar():
    numero = int(input("Dime un número para ver su tabla de multiplicar: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7

def operaciones_basicas():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division if division is not None else 'Indefinida'}")

# Ejercicio 8

def calcular_imc():
    peso = float(input("Dime tu peso en kg: "))
    altura = float(input("Dime tu altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")

# Ejercicio 9

def celsius_a_fahrenheit():
    celsius = float(input("Temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Equivalente en Fahrenheit: {fahrenheit:.2f}")

# Ejercicio 10

def calcular_promedio():
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Tercer número: "))
    promedio = (n1 + n2 + n3) / 3
    print(f"El promedio es: {promedio:.2f}")

# Menú Principal

def main():
    opciones = {
        "1": imprimir_hola_mundo,
        "2": saludar_usuario,
        "3": informacion_personal,
        "4": calcular_area_perimetro_circulo,
        "5": segundos_a_horas,
        "6": tabla_multiplicar,
        "7": operaciones_basicas,
        "8": calcular_imc,
        "9": celsius_a_fahrenheit,
        "10": calcular_promedio
    }

    eleccion = "1"
    while eleccion != "0":
        print("\nOpciones disponibles:")
        print("1. Imprimir 'Hola Mundo!'")
        print("2. Saludar Usuario")
        print("3. Información Personal")
        print("4. Calcular Área y Perímetro de un Círculo")
        print("5. Convertir Segundos a Horas")
        print("6. Tabla de Multiplicar")
        print("7. Operaciones Básicas")
        print("8. Calcular IMC")
        print("9. Convertir Celsius a Fahrenheit")
        print("10. Calcular Promedio")
        print("0. Salir")

        eleccion = input("Elegí un número de opción: ")

        if eleccion in opciones:
            opciones[eleccion]()
        elif eleccion != "0":
            print("Opción no válida.")

if __name__ == "__main__":
    main()
