pip install pycosat

import pycosat

# Funci�n para verificar la satisfacibilidad de una expresi�n l�gica
def verificar_satisfacibilidad(expresion):
    cnf = []  # Forma normal conjuntiva (CNF) de la expresi�n

    # Supongamos que la expresi�n est� en forma de una cadena
    # Ejemplo: (A or B) and (not A or C)
    clausulas = expresion.split("and")
    
    for clausula in clausulas:
        variables = clausula.split("or")
        clausula_cnf = [int(v) for v in variables]
        cnf.append(clausula_cnf)
    
    try:
        resultado = pycosat.solve(cnf)
        if resultado is not None:
            return True, resultado
        else:
            return False, None
    except pycosat.SolveFailed:
        return False, None

# Ejemplo de expresi�n l�gica para verificar satisfacibilidad
expresion = "(A or B) and (not A or C)"

satisfacible, asignacion = verificar_satisfacibilidad(expresion)

if satisfacible:
    print(f"La expresi�n es satisfacible. Asignaci�n de valores de verdad:")
    print(asignacion)
else:
    print("La expresi�n no es satisfacible.")
