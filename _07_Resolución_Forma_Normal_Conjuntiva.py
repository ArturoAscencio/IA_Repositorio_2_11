from sympy import symbols, Or, And, Not, Implies, to_cnf, satisfiable

# Definir variables
A, B, C = symbols('A B C')

# Definir una f�rmula l�gica
formula = And(Or(A, B), Or(Not(A), C), Implies(B, C))

# Convertir la f�rmula a su Forma Normal Conjuntiva (FNC)
fnc = to_cnf(formula, True)

# Imprimir la f�rmula en FNC
print("F�rmula en FNC:", fnc)

# Realizar resoluci�n
resolucion = satisfiable(fnc, algorithm="dpll")

if resolucion:
    print("La f�rmula es v�lida (satisfacible).")
else:
    print("La f�rmula no es v�lida (insatisfacible).")
