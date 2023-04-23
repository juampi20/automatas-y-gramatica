import re

texto = """
Extensión a cadenas de la función de transición
Hemos explicado informalmente que el AFD define un lenguaje: el conjunto de todas las cadenas que dan lugar a una secuencia de transiciones desde el estado inicial hasta un estado de aceptación. En términos del diagrama de transiciones, el lenguaje de un AFD es el conjunto de etiquetas ubicadas a lo largo de todos los caminos que van desde el estado inicial hasta cualquier estado de aceptación.
Ahora es necesario precisar la notación del lenguaje de un AFD. Para ello, definimos una función de transición extendida que describirá lo que ocurre cuando se parte de cualquier estado y se sigue cualquier secuencia de entradas. Si δ es la función de transición, entonces la función de transición extendida construida a partir de δ será _ δ . La función de transición extendida es una función que toma un estado q y una cadena w y devuelve un estado p (el estado al que el autómata llega partiendo del estado q y procesando la secuencia de entradas w). Definimos_δ por inducción sobre la longitud de la cadena de entrada como sigue:

BASE._ δ (q,ε) = q. Es decir, si nos encontramos en el estado q y no leemos ninguna entrada, entonces permaneceremos en el estado q.

PASO INDUCTIVO. Supongamos que w es una cadena de la forma xa; es decir, a es el último símbolo de w y x es la cadena formada por todos los símbolos excepto el último. 3 Por ejemplo, w = 1101 se divide en x = 110 y a = 1. Luego_ δ (q,w) = δ__ δ (q,x),a

La Ecuación (2.1) puede parecer complicada, pero la idea es simple. Para calcular _ δ (q,w), en primer lugar se calcula _ δ (q,x), el estado en el que el autómata se encuentra después de procesar todos los símbolos excepto el último de la cadena w. Supongamos que este estado es p; es decir, _ δ (q,x) = p. Entonces _ δ (q,w) es lo que obtenemos al hacer la transición desde el estado p con la entrada a, el último símbolo de w. Es decir, _δ (q,w) =δ (p,a).
"""

palabras = re.findall(r'\b\w+\b', texto.lower())

frecuencias = {}
for palabra in palabras:
    if palabra not in frecuencias:
        frecuencias[palabra] = 0
    frecuencias[palabra] += 1

palabra_mas_repetida = ""
frecuencia_palabra_mas_repetida = 0
for palabra, frecuencia in frecuencias.items():
    if frecuencia > frecuencia_palabra_mas_repetida:
        palabra_mas_repetida = palabra
        frecuencia_palabra_mas_repetida = frecuencia

print(f"La palabra más repetida es '{palabra_mas_repetida}' con una frecuencia de {frecuencia_palabra_mas_repetida} veces.")
