import math

class tpController:
    def holaMundo(self):
        print("Hola mundo!")

    def saludarPersona(self):
        nombre = input("Ingrese su nombre: ")
        print(f"Hola {nombre}!")

    def presentarPersona(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = input("Ingrese su edad: ")
        home = input("Ingrese el pais donde vive: ")
        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {home}")

    def calcularDatoCirculo(rselfadio):
        radio = input("Ingrese el radio del circulo: ")
        print(f"El area del circulo es {float(radio) * float(radio) * 3.14} y el perimetro es {2 * float(radio) * 3.14}")

    def segundosAHoras(self):
        segundos = input("Ingrese la cantidad de segundos: ")
        print(f"{segundos} segundos son {int(segundos) // 3600} hora/s")

    def tablaMultiplicar(self):
        numero = input("Ingrese el numero para la tabla de multiplicar: ")
        print(f"Tabla del {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {int(numero) * i}")

    def operacionesNumericas(self):
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        if(numero1 == 0 or numero2 == 0):
            print("Ningun numero puede ser 0")
        else:
            print(f"La suma de {numero1} y {numero2} es {float(numero1) + float(numero2)}")
            print(f"La resta de {numero1} y {numero2} es {float(numero1) - float(numero2)}")
            print(f"La multiplicación de {numero1} y {numero2} es {float(numero1) * float(numero2)}")
            print(f"La división de {numero1} y {numero2} es {float(numero1) / float(numero2)}")

    def calculadoraImc(self):
        peso = input("Ingrese su peso: ")
        altura = input("Ingrese su altura en metros: ")
        imc = float(peso) / (float(altura) * float(altura))
        print(f"El IMC es {round(imc, 2)}") 

    def celsiusAFahrenheit(self):
        celsius = input("Ingrese la temperatura en grados celsius: ")
        print(f"{celsius} grados celsius son {float(celsius) * 1.8 + 32} grados fahrenheit")

    def calculadoraPromedio(self):
        nota1 = input("Ingrese la primera nota: ")
        nota2 = input("Ingrese la segunda nota: ")
        nota3 = input("Ingrese la tercera nota: ")
        print(f"El promedio de las notas es {(int(nota1) + int(nota2) + int(nota3)) / 3}")
    

def main():
    ctrl = tpController()
    opciones = {
        "1": ctrl.holaMundo,
        "2": ctrl.saludarPersona,
        "3": ctrl.presentarPersona,
        "4": ctrl.saludarPersona,
        "5": ctrl.calcularDatoCirculo,
        "6": ctrl.segundosAHoras,
        "7": ctrl.tablaMultiplicar,
        "8": ctrl.operacionesNumericas,
        "9": ctrl.calculadoraImc,
        "10": ctrl.celsiusAFahrenheit,
        "11": ctrl.calculadoraPromedio
    }

    eleccion = "1"
    while eleccion != "0":
        eleccion = input(f"Elegí un método (1-{len(opciones)}, 0 para salir): ")
        if eleccion in opciones:
            opciones[eleccion]()
        elif eleccion != "0":
            print("Método no encontrado")

if __name__ == "__main__":
    main()