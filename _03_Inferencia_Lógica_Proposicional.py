variables = {
    'A': True,
    'B': False,
    'C': True
}

# Definir una expresi�n l�gica para evaluar (por ejemplo, A and B or C)
expresion_logica = "(A and B) or C"

# Funci�n para evaluar una expresi�n l�gica
def evaluar_expresion(expresion, variables):
    try:
        resultado = eval(expresion, variables)
        return resultado
    except:
        return False

# Evaluar la expresi�n l�gica
resultado = evaluar_expresion(expresion_logica, variables)

# Imprimir el resultado
print(f"La expresi�n l�gica ({expresion_logica}) es {resultado}")
