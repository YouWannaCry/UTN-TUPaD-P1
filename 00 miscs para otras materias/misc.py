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


def main():
    ctrl = tpController()
    opciones = {
        "1": ctrl.decimalToBinary,
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