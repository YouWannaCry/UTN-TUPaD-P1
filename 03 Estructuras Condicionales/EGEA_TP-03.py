import random
from statistics import mode, median, mean

class tpController:
    def mayoriaDeEdad(self):
        edad = int(input("Cual es tu edad? "))
        if edad >= 18:
            print("Es mayor de edad")
    
    def aprueba(self):
        nota = int(input("Que nota te sacaste? "))
        if nota >= 6:
            print("Desaprobado")
        else:
            print("Desaprobado")

    def esPar(self):
        numero = int(input("Escribe un numero par: "))
        if(numero % 2 == 0):
            print("Ese numero es par")
        else:
            print("Por favor, ingrese un numero par")

    def clasificacionEdad(self):
        edad = int(input("Cual es tu edad? "))
        if(edad < 12 and edad >= 0):
            print("Eres un niño/a")
        elif(edad >= 12 and edad< 18):
            print("Eres un adolescente")
        elif(edad >= 18 and edad < 30):
            print("Eres un adulto/a joven")
        elif(edad >= 30):
            print("Eres un adulto")
        else:
            print("Eres el increible caso de una persona que aun no ha nacido!")

    def checkContraseña(self):
        contraseña = input("Ingresa tu contraseña, pon algo secreto y seguro!: \n")
        if(len(contraseña) < 8 or len(contraseña) > 14):
            print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
        else:
            print("Ha ingresado una contraseña correcta")

    def calcularSesgo(self):
        print("Vamos a calcular la moda, mediana y media de 100 numeros en un rango al azar entre 1 y 100")
        numerosAleatorios = [random.randint(1, 100) for i in range(100)]
        moda = mode(numerosAleatorios)
        mediana = median(numerosAleatorios)
        media = mean(numerosAleatorios)
        print(f"La moda calculada es {moda}, la mediana calculada es {mediana}, y la media calculada es {media}")
        if(media > mediana and mediana > moda):
            print("Hay un sesgo positivo")
        if(media < mediana and mediana < moda):
            print("Hay un sesgo negativo")
        if(media == mediana and mediana == moda):
            print("No hay sesgo")

    def exclamar(self):
        phrase = input("Dime una frase, o una palabra: ")
        if(phrase[-1].lower() in "aeiou"):
            phrase += "!"
            
        print(f"{phrase}")

    def parseName(self):
        nombre = input("Dime tu nombre: ")
        modo = int(input(
        "¿Qué modo quieres?\n"
        "1 - Nombre todo en mayúscula\n"
        "2 - Nombre todo en minúscula\n"
        "3 - Nombre con la primera letra mayúscula\n"
        "Opción: "
    ))
    
        if (modo == 1):
            print(nombre.upper())
        elif (modo == 2):
            print(nombre.lower())
        elif (modo == 3):
            print(nombre.capitalize())
        else:
            print("Modo inválido.")

    def clasificaTerremoto(self):
        magnitud = float(input("Dime la magnitud de un terremoto y te dire en que parte de la escala de Richter se encuentra: "))
        if(magnitud < 3):
            print("Muy leve (casi imperceptible)")

        elif(magnitud >= 3 and magnitud < 4):
            print("Leve (ligeramente imperceptible)")

        elif(magnitud >= 4 and magnitud < 5):
            print("Moderado (sentido por personas, normalmente no peligroso)")

        elif(magnitud >= 5 and magnitud < 6):
            print("Fuerte (puede causar algun daño)")

        elif(magnitud >= 6 and magnitud < 7):
            print("Muy fuerte (puede causar daños significativos)")

        elif(magnitud > 7):
            print("Extremo (puede causar graves daños a gran escala)")

    def estacionAño(self):
        hemisferio = input("¿En qué hemisferio estás? (N/S): ")
        mes = int(input("¿Mes del año? (1-12): "))
        dia = int(input("¿Día del mes?: "))
        #Defino un diccionario que tiene, dia y mes de inicio de estacion, dia y mes de fin de estacion
        #y el hemisferio con la estacion correspondiente
        estaciones = [
                ((21, 12), (20, 3), {"N": "Invierno", "S": "Verano"}),
                ((21, 3),  (20, 6), {"N": "Primavera", "S": "Otoño"}),
                ((21, 6),  (20, 9), {"N": "Verano", "S": "Invierno"}),
                ((21, 9),  (20, 12),{"N": "Otoño", "S": "Primavera"})
            ]

        for inicio, fin, nombres in estaciones:
            if (mes == inicio[1] and dia >= inicio[0]) or \
               (mes == fin[1] and dia <= fin[0]) or \
               (mes > inicio[1] and mes < fin[1]) or \
               (inicio[1] > fin[1] and (mes > inicio[1] or mes < fin[1])):
                print(nombres[hemisferio.upper()])
                return

        print("Fecha inválida")

    def validoParaEntrada(self): #Ejercicio realizado en consulta
        edad = int(input("Cual es tu edad? "))
        altura = int(input("Cual es tu altura (En cm)? "))
        if(altura >= 150 and edad >= 15):
            print("Eres apto para subirte")
        else:
            print("No eres apto")

def main():
    ctrl = tpController()
    opciones = {
        "1": ctrl.mayoriaDeEdad,
        "2": ctrl.aprueba,
        "3": ctrl.esPar,
        "4": ctrl.clasificacionEdad,
        "5": ctrl.checkContraseña,
        "6": ctrl.calcularSesgo,
        "7": ctrl.exclamar,
        "8": ctrl.parseName,
        "9": ctrl.clasificacionEdad,
        "10": ctrl.estacionAño,
        "11": ctrl.validoParaEntrada
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