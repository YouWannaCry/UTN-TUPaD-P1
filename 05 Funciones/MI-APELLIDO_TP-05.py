class tpController:
    def 

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