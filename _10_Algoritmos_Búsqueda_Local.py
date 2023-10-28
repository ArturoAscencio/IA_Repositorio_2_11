import random
import math

# Funci�n de costo de ejemplo (puede ser reemplazada por tu funci�n de costo)
def costo(solucion):
    return sum(x ** 2 for x in solucion)

# Algoritmo de recocido simulado
def recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones):
    solucion_actual = solucion_inicial
    costo_actual = costo(solucion_actual)
    mejor_solucion = solucion_actual
    mejor_costo = costo_actual

    for i in range(iteraciones):
        # Generar una soluci�n vecina
        indice = random.randint(0, len(solucion_actual) - 1)
        solucion_vecina = solucion_actual[:]
        solucion_vecina[indice] += random.uniform(-0.1, 0.1)

        # Calcular el costo de la soluci�n vecina
        costo_vecina = costo(solucion_vecina)

        # Calcular la diferencia de costos
        diferencia_costos = costo_vecina - costo_actual

        # Si la soluci�n vecina es mejor o se acepta con una probabilidad, actual�zala
        if diferencia_costos < 0 or random.random() < math.exp(-diferencia_costos / temperatura_inicial):
            solucion_actual = solucion_vecina
            costo_actual = costo_vecina

        # Actualizar la mejor soluci�n si es necesario
        if costo_actual < mejor_costo:
            mejor_solucion = solucion_actual
            mejor_costo = costo_actual

        # Enfriar la temperatura
        temperatura_inicial *= factor_enfriamiento

    return mejor_solucion, mejor_costo

# Par�metros del algoritmo
solucion_inicial = [random.uniform(-5, 5) for _ in range(10)]
temperatura_inicial = 1.0
factor_enfriamiento = 0.95
iteraciones = 10000

# Ejecutar el algoritmo de recocido simulado
mejor_solucion, mejor_costo = recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones)

print("Mejor soluci�n encontrada:", mejor_solucion)
print("Mejor costo:", mejor_costo)
