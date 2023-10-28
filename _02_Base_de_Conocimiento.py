base_de_conocimiento = {
    'personas': [
        {'nombre': 'Juan', 'edad': 30, 'profesion': 'Ingeniero'},
        {'nombre': 'María', 'edad': 25, 'profesion': 'Doctora'},
        {'nombre': 'Carlos', 'edad': 35, 'profesion': 'Profesor'}
    ],
    'ciudades': [
        {'nombre': 'Nueva York', 'poblacion': 8000000, 'pais': 'Estados Unidos'},
        {'nombre': 'París', 'poblacion': 2200000, 'pais': 'Francia'},
        {'nombre': 'Londres', 'poblacion': 9000000, 'pais': 'Reino Unido'}
    ],
    'paises': [
        {'nombre': 'Estados Unidos', 'capital': 'Washington, D.C.'},
        {'nombre': 'Francia', 'capital': 'París'},
        {'nombre': 'Reino Unido', 'capital': 'Londres'}
    ]
}

# Acceder a la base de conocimiento
print("Información sobre personas:")
for persona in base_de_conocimiento['personas']:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Profesión: {persona['profesion']}")

print("\nInformación sobre ciudades:")
for ciudad in base_de_conocimiento['ciudades']:
    print(f"Nombre: {ciudad['nombre']}, Población: {ciudad['poblacion']}, País: {ciudad['pais']}")

print("\nInformación sobre países:")
for pais in base_de_conocimiento['paises']:
    print(f"Nombre: {pais['nombre']}, Capital: {pais['capital']}")
