variables = {
    'A': True,
    'B': False,
    'C': True
}

# Definir una expresión lógica para evaluar (por ejemplo, A and B or C)
expresion_logica = "(A and B) or C"

# Función para evaluar una expresión lógica
def evaluar_expresion(expresion, variables):
    try:
        resultado = eval(expresion, variables)
        return resultado
    except:
        return False

# Evaluar la expresión lógica
resultado = evaluar_expresion(expresion_logica, variables)

# Imprimir el resultado
print(f"La expresión lógica ({expresion_logica}) es {resultado}")
