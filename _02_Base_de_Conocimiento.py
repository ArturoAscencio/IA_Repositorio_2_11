base_de_conocimiento = {
    'personas': [
        {'nombre': 'Juan', 'edad': 30, 'profesion': 'Ingeniero'},
        {'nombre': 'Mar�a', 'edad': 25, 'profesion': 'Doctora'},
        {'nombre': 'Carlos', 'edad': 35, 'profesion': 'Profesor'}
    ],
    'ciudades': [
        {'nombre': 'Nueva York', 'poblacion': 8000000, 'pais': 'Estados Unidos'},
        {'nombre': 'Par�s', 'poblacion': 2200000, 'pais': 'Francia'},
        {'nombre': 'Londres', 'poblacion': 9000000, 'pais': 'Reino Unido'}
    ],
    'paises': [
        {'nombre': 'Estados Unidos', 'capital': 'Washington, D.C.'},
        {'nombre': 'Francia', 'capital': 'Par�s'},
        {'nombre': 'Reino Unido', 'capital': 'Londres'}
    ]
}

# Acceder a la base de conocimiento
print("Informaci�n sobre personas:")
for persona in base_de_conocimiento['personas']:
    print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Profesi�n: {persona['profesion']}")

print("\nInformaci�n sobre ciudades:")
for ciudad in base_de_conocimiento['ciudades']:
    print(f"Nombre: {ciudad['nombre']}, Poblaci�n: {ciudad['poblacion']}, Pa�s: {ciudad['pais']}")

print("\nInformaci�n sobre pa�ses:")
for pais in base_de_conocimiento['paises']:
    print(f"Nombre: {pais['nombre']}, Capital: {pais['capital']}")
