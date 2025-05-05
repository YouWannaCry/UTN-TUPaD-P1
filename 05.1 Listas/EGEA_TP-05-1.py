class tpController:
    def listaMultiplo(self):
        """Crea una lista con los numeros del 1 al 100 que sean multiplos de 4"""
        multiplos = []
        for i in range(4,101,4):
            multiplos.append(i)
        print(multiplos)

    def printPenult(self):
        """Imprime el penultimo valor de una lista"""
        things = ["Ñoquis", 5, "Auto", 19, True]
        print(things[-2])

    def appendAndPrint(self):
        """Se crea una lista vacia y se le agregan 3 valores, luego se imprime"""
        words = []
        words.append("Cebra")
        words.append("Tiranosaurio")
        words.append("Texto")
        print(words)

    def replaceValues(self):
        """Reemplaza el segundo y ultimo valor de la lista"""
        animales = ["perro", "gato", "conejo", "pez"]
        print(animales)
        animales[-1] = "oso"
        animales[2] = "loro" ##No se si por "el segundo" se refieren a el segundo [2], o el segundo [1]. En cualquier caso lo deje asi, pero considere tambien la otra opcion
        print(animales)
    
    def explain(self):
        """Explica el codigo mediante prints"""
        numeros = [8, 15, 3, 22, 7]
        print("Primero se define una lista con ciertos valores")
        numeros.remove(max(numeros))
        print("Se hace un remove (max(numeros)) que obtiene el valor maximo de la lista(en este caso, 22)")
        print(numeros)
        print("Se imprime la lista ya modificada")

    def printNumbers(self):
        """Crea una lista del 10 al 30, con saltos de 5 en 5 e imprime los primeros 2"""
        numbers = []
        for i in range(10, 31, 5):
            numbers.append(i)
        print(numbers[0:2])
    
    def replaceCentral(self):
        """Reemplaza los dos valores centrales de una lista por dos valores al azar"""
        autos = ["sedan", "polo", "suran", "gol"]
        autos[1] = "sam"
        autos[2] = "porter"
        print(autos)

    def doubleIt(self):
        """Se doblan todos los valores de una lista"""
        list = [5, 10, 15]
        dobles = []
        for x in list[0:]:
            dobles.append(x * 2)
        print(dobles)

    def shoplist(self):
        """Se modifican las listas de compras de algunos clientes"""
        compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
        compras[2].append("jugo")
        compras[1][1] = "tallarines"
        compras[0].remove("pan")
        print(compras)

    def printList(self):
        """Se crea una lista y se imprimen los valores por pantalla"""
        lista_anidada = [
            15,               
            True,             
            [25.5, 57.9, 30.6],
            False
            ]
        print(lista_anidada)
 

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