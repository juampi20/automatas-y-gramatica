import os
import re

class RegexValidation:
    def __init__(self):
        self.regex1 = r"(a|b)*$"
        self.regex2 = r"(aa|b)*(a|bb)*?$"

    def clear_screen(self):
        os.system("cls")

    def validate_input(self, regex, input_string):
        current_state = 0
        print(f"Estado actual: {current_state}")
        for symbol in input_string:
            if re.match(regex, symbol):
                next_state = current_state + 1
                print(f"Símbolo '{symbol}' -> Estado siguiente: {next_state}")
                current_state = next_state
            else:
                print(f"Símbolo '{symbol}' no es válido en la posición {current_state}.")
                return
        if re.match(regex, ""):
            print(f"La cadena '{input_string}' es válida.")
        else:
            print(f"La cadena '{input_string}' no es válida.")

    def ej1(self):
        self.clear_screen()
        input_string = input("Inserte una cadena compatible con la siguiente expresión regular: (a|b)*\nCadena: ")
        self.validate_input(self.regex1, input_string)

    def ej2(self):
        self.clear_screen()
        input_string = input("Inserte una cadena compatible con la siguiente expresión regular: (aa|b)*(a|bb)*\nCadena: ")
        self.validate_input(self.regex2, input_string)

rv = RegexValidation()

while True:
    rv.clear_screen()
    print("""
    --------------------------------------------------------
    Selecione una opcion:

    opcion 1: (a|b)*
    opcion 2: (aa|b)*(a|bb)*
    --------------------------------------------------------
    """)
    opt = input("Respuesta: ")

    if opt == "1":
        rv.ej1()
    elif opt == "2":
        rv.ej2()
    else:
        print("Opción inválida. Intente de nuevo.")

    input("\n Presione una tecla... ")
