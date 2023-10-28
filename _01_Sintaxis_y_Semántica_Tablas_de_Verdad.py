import itertools

# Variables lógicas y operadores
variables = ['A', 'B']
operadores = ['and', 'or', 'not']

# Generar todas las combinaciones posibles de valores de verdad para las variables
combinaciones = list(itertools.product([True, False], repeat=len(variables)))

# Imprimir encabezado de la tabla de verdad
encabezado = " | ".join(variables + [f"{op}()" for op in operadores])
print(encabezado)
print("-" * len(encabezado))

# Generar y mostrar la tabla de verdad
for combinacion in combinaciones:
    valores = dict(zip(variables, combinacion))
    resultados = []
    for op in operadores:
        if op == 'and':
            resultados.append(valores['A'] and valores['B'])
        elif op == 'or':
            resultados.append(valores['A'] or valores['B'])
        elif op == 'not':
            resultados.append(not valores['A'])
    fila = " | ".join([str(valores[var]) for var in variables] + [str(res) for res in resultados])
    print(fila)
