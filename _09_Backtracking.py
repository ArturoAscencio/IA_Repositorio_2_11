def es_seguro(tablero, fila, columna, N):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, N)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_queens(N):
    tablero = [[0] * N for _ in range(N)]

    if not resolver_n_queens_util(tablero, 0, N):
        print("No hay solución.")
    else:
        imprimir_tablero(tablero)

def resolver_n_queens_util(tablero, fila, N):
    if fila == N:
        return True

    for columna in range(N):
        if es_seguro(tablero, fila, columna, N):
            tablero[fila][columna] = 1

            if resolver_n_queens_util(tablero, fila + 1, N):
                return True

            tablero[fila][columna] = 0

    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(['Q' if c == 1 else '.' for c in fila]))

N = 8  # Número de reinas y tamaño del tablero
resolver_n_queens(N)
