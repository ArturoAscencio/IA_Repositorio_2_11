import itertools

# Función para evaluar una expresión lógica y construir su tabla de verdad
def tabla_de_verdad(expresion):
    variables = set([c for c in expresion if c.isalpha()])
    combinaciones = list(itertools.product([False, True], repeat=len(variables)))
    tabla = []

    for combinacion in combinaciones:
        valores = dict(zip(variables, combinacion))
        resultado = eval(expresion, valores)
        fila = {**valores, 'Resultado': resultado}
        tabla.append(fila)

    return tabla

# Función para verificar la validez de una expresión lógica
def es_validez(expresion):
    tabla = tabla_de_verdad(expresion)
    return all(fila['Resultado'] for fila in tabla)

# Expresión lógica a verificar
expresion = "(A or B) and (not A or B) and (A or not B)"

# Verificar si la expresión es válida
if es_validez(expresion):
    print(f"La expresión es válida (siempre verdadera).")
else:
    print(f"La expresión no es válida (puede ser falsa en alguna asignación de valores).")
