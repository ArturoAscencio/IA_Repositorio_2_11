reglas = {
    'Regla1': {'antecedente': ['A'], 'consecuente': 'B'},
    'Regla2': {'antecedente': ['B', 'C'], 'consecuente': 'D'},
    'Regla3': {'antecedente': ['E'], 'consecuente': 'C'}
}

# Hechos iniciales
hechos = ['A', 'E']

def encadenamiento_hacia_adelante(reglas, hechos):
    nuevos_hechos = set(hechos)
    while True:
        cambios = False
        for regla, datos in reglas.items():
            antecedente = datos['antecedente']
            consecuente = datos['consecuente']
            if all(antecedente_h in nuevos_hechos for antecedente_h in antecedente) and consecuente not in nuevos_hechos:
                nuevos_hechos.add(consecuente)
                cambios = True
                print(f"Aplicando {regla}: {', '.join(antecedente)} -> {consecuente}")
        if not cambios:
            break
    return nuevos_hechos

nuevos_hechos = encadenamiento_hacia_adelante(reglas, hechos)
print("Hechos deducidos:", nuevos_hechos)

# Encadenamiento hacia atrás (backward chaining):

def encadenamiento_hacia_atras(reglas, meta):
    if meta in hechos:
        return True
    for regla, datos in reglas.items():
        consecuente = datos['consecuente']
        antecedente = datos['antecedente']
        if consecuente == meta:
            print(f"Meta alcanzada: {meta}")
            for antecedente_h in antecedente:
                if not encadenamiento_hacia_atras(reglas, antecedente_h):
                    return False
            return True
    return False

meta = 'D'
resultado = encadenamiento_hacia_atras(reglas, meta)

if resultado:
    print(f"Se pudo demostrar la meta: {meta}")
else:
    print(f"No se pudo demostrar la meta: {meta}")
