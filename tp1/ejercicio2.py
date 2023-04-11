def solve(value):

    lista1 = value.split("+")
    values = "*".join(lista1).split("*")

    simbolos = []

    for i in range(len(values)):
        values[i] = int(values[i])

    for i in value:
        if i in "+*":
            simbolos.append(i)

    while "*" in simbolos:
        indice = simbolos.index("*") # Indice del primer simbolo de multiplicacion
        resultado = values[indice] * values[indice+1] # Realizar la multiplicacion
        values[indice] = resultado # Reemplazar el primer numero de la multiplicacion por el resultado
        values.pop(indice+1) # Eliminar el segundo numero de la multiplicacion
        simbolos.pop(indice) # Eliminar el simbolo de multiplicacion
    
    resultado = values[0]

    for i in range(len(simbolos)):
        resultado += values[i+1]

    return resultado
    

if __name__ == '__main__':
    string = input('Ingrese una expresion matematica: ')
    solve(str(string))