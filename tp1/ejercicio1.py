def validate_string(value):
    
    # Definimos las variables que la cadena debe cumplir
    has_upper = False
    has_lower = False
    has_alnum = False
    has_alpha = False
    has_digit = False
    is_long_enough = len(value) > 8

    # Recorremos la cadena y verificamos si cumple con las condiciones
    for c in value: # c es cada caracter de la cadena
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isalnum():
            has_alnum = True
        if c.isalpha():
            has_alpha = True
        if c.isdigit():
            has_digit = True

    # Imprimimos los resultados
    print(has_alnum) # Contiene caracteres alfanumericos
    print(has_alpha) # Contiene caracteres alfabéticos
    print(has_upper) # Contiene mayúsculas
    print(has_lower) # Contiene minúsculas
    print(has_digit) # Contiene dígitos
    print(is_long_enough) # Es lo suficientemente larga

if __name__ == '__main__':
    value = input("Ingrese una cadena: ")
    validate_string(value)
