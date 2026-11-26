# Función que clasifica el nivel de compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# Matriz con los datos de las sesiones: [ID, Duración, Clics]
sesiones = [
    [101, 200, 10],
    [102, 45, 2],
    [103, 120, 5],
    [104, 250, 12],
    [105, 90, 4]
]

# Encabezado del informe
print("=" * 45)
print("INFORME DE COMPROMISO POR SESIÓN")
print("=" * 45)
print(f"{'ID Cliente':<12} {'Nivel de Compromiso':<20}")
print("-" * 45)

# Recorrer la matriz y mostrar resultados
for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    cantidad_clics = sesion[2]
    nivel = clasificar_compromiso(duracion, cantidad_clics)
    print(f"{id_cliente:<12} {nivel:<20}")

# Mensaje de cierre
print("=" * 45)
print(" Proceso finalizado correctamente")