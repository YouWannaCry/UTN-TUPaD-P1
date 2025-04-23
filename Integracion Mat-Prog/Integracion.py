import random

class aux:
    def decimalToBinary(decimal):
        resultado = ""
        while decimal > 0:
            residuo = decimal % 2
            decimal //= 2
            resultado = str(residuo) + resultado
        return resultado if resultado else "0"
    
    def falseOption(resultado, cantidad=4):
        correctOption = aux.decimalToBinary(resultado)
        options = {correctOption}
        while len(options) < cantidad + 1:
            alter = resultado + random.choice([-3, -2, -1, 1, 2, 3])
            if alter >= 0:
                options.add(aux.decimalToBinary(alter))
        return list(options)
    
    def getValidIntInput(prompt, minVal, maxVal):
        while True:
            entrada = input(prompt)
            if entrada.isdigit():
                guess = int(entrada)
                if minVal <= guess <= maxVal:
                    return guess
                else:
                    print(f"Ingresa un numero entre {minVal} y {maxVal}.")
            else:
                print("Eso no es un numero valido.")


class controller:
    def logicQuiz(self):
        hardness = aux.getValidIntInput(f"¿Que dificultad quieres?\n(Debes colocar entre 1 y 6): ", 1, 6)
        totalQuestion = hardness + 2
        answered = 0
        totalTries = 0
        while totalQuestion > answered:
            op = random.choice(["+", "-", "*", "//"])
            dec1 = random.randint(10, 100)
            dec2 = random.randint(2, dec1)
            bin1 = aux.decimalToBinary(dec1)
            bin2 = aux.decimalToBinary(dec2)
            result = eval(f"{dec1} {op} {dec2}")
            binary = aux.decimalToBinary(result)
            options = aux.falseOption(result, hardness)
            print(binary)
            print(f"""
Pregunta {answered + 1}
¿Que resultado dara la operacion {bin1} {op} {bin2}?
Opciones:""")
            for i, op in enumerate(options, start=1):
                print(f"{i}) {op}")
            guess = aux.getValidIntInput("¿Cual es la opcion correcta? ", 1, len(options))
            tries = 0
            while True:
                tries += 1
                totalTries += 1
                if(options[guess-1] != binary):
                    for i, op in enumerate(options, start=1):
                        print(f"{i}) {op}")
                    guess = aux.getValidIntInput("Ups, ese no es el resultado, intenta de nuevo: ", 1, len(options))
                    continue
                else:
                    print(f"Usaste {tries} intento/s en esta pregunta")
                    break
            answered += 1
        print(f"Felicidades, respondiste todas las preguntas! Te tomo tan solo {totalTries} intentos, eso es una precision del {(totalQuestion/totalTries)*100}%")



if __name__ == "__main__":
    controller().logicQuiz()