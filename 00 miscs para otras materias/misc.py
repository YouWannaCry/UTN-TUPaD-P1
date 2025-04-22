import random

class tpController:
    def decimalToBinary(self):
        decimal = int(input("Ingresa un número decimal: "))
        numero_original = decimal
        resultado = ""
        pasos = []
        
        while decimal > 0:
            residuo = decimal % 2
            cociente = decimal // 2
            pasos.append((decimal, cociente, residuo))
            resultado = str(residuo) + resultado
            decimal = cociente
        
        print(f"Conversión de {numero_original} a binario:")
        for paso in pasos:
            print(f"{paso[0]}/2 = {paso[1]} -> {paso[2]}")
        
        print(f"\nEl número {numero_original} en binario es: {resultado}")

    def printWhile(self):
        i = 0
        while (i < 9):
            if(i == 7):
                i += 1
                continue
            print(i)
            i += 1

    def adivinar(self):
        numero = random.randint(0, 9)
        guess = int(input("Dame un numero y te dire si es el que estoy pensando: "))
        while numero != guess:
            guess = int(input("Ese numero es incorrecto, intenta de nuevo! "))
        print(f"Correcto! El numero era: {numero}")

def main():
    ctrl = tpController()
    opciones = {
        "1": ctrl.adivinar,
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