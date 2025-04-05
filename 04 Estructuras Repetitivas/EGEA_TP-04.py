import random
from statistics import mode, median, mean

class tpController:
    #Ejercicio 1
    def printCentena(self):
        """Imprimir números del 0 al 100"""
        i = 0
        while i <= 100:
            print(i)
            i += 1

    #Ejercicio 2
    def digitosEnteros(self):
        """Cantidad de que contiene un entero"""
        numero = input("Dime un numero entero, y te dire cuantos digitos tiene: ")
        counter = 0
        for _ in numero:
            counter += 1
        print(f"El numero entero que me diste tiene {counter} digitos!")
        ##Tambien se puede hacer asi sin el for, 
        # print(f"El numero entero que me diste tiene {len(numero)} digitos!")

    #Ejercicio 3
    def sumatoria(self):
        """Suma todos los enteros entre dos valores"""
        num1, num2 = int(input("Dime dos valores, y te dare la sumatoria de todos los valores intermedios: "))
        sumatoria = 0
        for i in range(num1, num2):
            sumatoria += i
        print(sumatoria)

    #Ejercicio 4
    def sumaInfinita(self):
        """Suma hasta que se ingrese un 0"""
        numero = int(input("""Sumare todos los numeros que escribas, hasta que escribas 0 
                           Empieza con el primer intento: """))
        suma = 0
        while(numero != 0):
            suma += numero
            numero = int(input(f"La suma hasta ahora es {suma}, que quieres sumar ahora? 0 para terminar: "))
        print(f"La suma final es de {suma}")

    #Ejercicio 5
    def adivina(self):
        """Genera un numero aleatorio entre 0 y 9, y cuenta las veces que el usuario tarda en adivinar"""
        numero = random.randint(0, 9)
        guess = int(input("""Estoy pensando en un numero entre el 0 y el 9, podrias adivinarlo?
                          Dime tu primer intento: """))
        counter = 1
        tried = [guess]
        while numero != guess:
            guess = int(input(f"""Eso estuvo cerca, pero no es el número correcto.
                              Has probado con estos números: {", ".join(str(numero) for numero in tried)}
                              Prueba con otro: """))
            counter += 1
            tried.append(guess)
            
        print(f"""Lo lograste! El número era {numero}.
              Intentaste {counter} veces.
              Estos fueron tus intentos: {", ".join(str(numero) for numero in tried)}""")
        
    #Ejercicio 6
    def printParCentena(self):
        """Imprime todos los numeros pares desde el 100 hasta el 0"""
        for i in range(100, 0, -2):
            print(i)

    #Ejercicio 7
    def sumatoriaHastaX(self):
        """Suma todos los enteros entre 0 y un valor dado"""
        num1 = int(input("Dime un valor, y te dare la sumatoria de todos los numeros hasta ese: "))
        sumatoria = 0
        for i in range(0, num1):
            sumatoria += i
        print(sumatoria)

    #Ejercicio 8
    def datoCentenar(self):
        """Permite ingresar 100 numeros (o generarlos al azar) y calcula varios parametros"""
        ## lista = [random.randint(-1000, 1000) for _ in range(100)] ##Metodo para probar y generar la cantidad que se quieran de valores
        lista = []
        for i in range(100):
            numero = input("Con que número seguimos? ")

            while True:
                try:
                    numero = int(numero)
                    break
                except ValueError:
                    numero = input("Ups, eso no es un numero. Intenta de nuevo: ")

            lista.append(numero)
            print(f"Ya llevas {len(lista)} numero/s")


        positivos, negativos, pares, impares = [], [], [], []
        for i in lista:
            if(i > 0):
                positivos.append(i)
            else:
                negativos.append(i)
            
            if((i % 2) == 0 ):
                pares.append(i)
            else:
                impares.append(i)
            
        print(
            f"""Muy bien! A partir de los 100 numeros que me has dado, te dare los datos: 

            Primero empezamos con los numeros positivos! 
            Ingresaste {len(positivos)} numeros positivos, y son: {", ".join(str(numero) for numero in positivos)}

            Ahora, vamos con los negativos: 
            Ingresaste {len(negativos)} numeros negativos, y son: {", ".join(str(numero) for numero in negativos)}
            
            Veamos con los pares: 
            Ingresaste {len(pares)} numeros pares, y son: {", ".join(str(numero) for numero in pares)} 

            Y para terminar, los impares: 
            Ingresaste {len(impares)} numeros impares, y son: {", ".join(str(numero) for numero in impares)}

            Y ahora como datos curiosos, el {(len(positivos) * 100)/100}% de los numeros que escribiste eran positivos!
            El {100-((len(positivos) * 100)/100)}% restante eran negativos.

            Los ultimos datos, el {(len(pares) * 100)/100}% de los numeros que escribiste eran pares!
            El {100-((len(pares) * 100)/100)}% restante eran impares.
""")


    #Ejercicio 9
    def  mediaDeCentena(self):
        """Permite ingresar 100 numeros (o generarlos al azar) y calcula la media"""
        # lista = [random.randint(-1000, 1000) for _ in range(100)] ##Metodo para probar y generar la cantidad que se quieran de valores
        lista = []
        for i in range(100):
            numero = input("Con que número seguimos? ")

            while True:
                try:
                    numero = int(numero)
                    break
                except ValueError:
                    numero = input("Ups, eso no es un numero. Intenta de nuevo: ")

            lista.append(numero)
            print(f"Ya llevas {len(lista)} numero/s")

        media = sum(lista) / len(lista)
        print(f"""
              Ingresaste estos numeros: {", ".join(str(numero) for numero in lista)}
              Esta es su media: {media}
""")
        
    #Ejercicio 10
    def invertir(self):
        """Invierte los numeros ingresados por el usuario"""
        numero = input("Que numero quieres invertir? ")

        while True:
            try:
                numero = int(numero)
                break
            except ValueError:
                numero = input("Ups, eso no es un numero. Intenta de nuevo: ")
        
        #Seguro se puede hacer de otra forma, no se me ocurre como
        isNegative = numero < 0
        numero = abs(numero)
        digitos = list(str(numero))
        digitos.reverse()
        inverse = int("".join(digitos))
        if isNegative:
            inverse = -inverse
        print(f"El numero invertido es {inverse}")
    
        
def main():
    ctrl = tpController()

    metodos = [(nombre, getattr(ctrl, nombre)) for nombre in ctrl.__class__.__dict__ if callable(getattr(ctrl, nombre))]
    
    opciones = {str(index + 1): funcion for index, (nombre, funcion) in enumerate(metodos)}

    eleccion = "1"
    while eleccion != "0":
        print("\nOpciones disponibles:")
        for key, funcion in opciones.items():
            descripcion = funcion.__doc__ if funcion.__doc__ else funcion.__name__
            print(f"{key}. {descripcion}")

        eleccion = input(f"Elegí un método (1-{len(opciones)}, 0 para salir): ")
        if eleccion in opciones:
            opciones[eleccion]()
        elif eleccion != "0":
            print("Método no encontrado")


if __name__ == "__main__":
    main()