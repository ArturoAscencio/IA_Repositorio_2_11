import itertools

# Funci�n para evaluar una expresi�n l�gica y construir su tabla de verdad
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

# Funci�n para verificar la validez de una expresi�n l�gica
def es_validez(expresion):
    tabla = tabla_de_verdad(expresion)
    return all(fila['Resultado'] for fila in tabla)

# Expresi�n l�gica a verificar
expresion = "(A or B) and (not A or B) and (A or not B)"

# Verificar si la expresi�n es v�lida
if es_validez(expresion):
    print(f"La expresi�n es v�lida (siempre verdadera).")
else:
    print(f"La expresi�n no es v�lida (puede ser falsa en alguna asignaci�n de valores).")
