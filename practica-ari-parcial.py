# Número de ciclistas y etapas
num_ciclistas = 10
num_etapas = 2

# Inicializar variables para calcular las estadísticas
velocidad_promedio_mas_alta = 0
velocidad_promedio_mas_baja = float('inf')
velocidad_promedio_general = 0
ciclistas_velocidad_superior_30 = 0
ciclistas_velocidad_superior_25_todas_etapas = 0
velocidad_etapa_mas_rapida = float('inf')
velocidad_etapa_mas_lenta = 0

# Loop para registrar las velocidades de los ciclistas y calcular estadísticas
for ciclista in range(1, num_ciclistas + 1):
    velocidad_total = 0
    velocidad_etapa_mas_rapida_ciclista = float('inf')
    velocidad_etapa_mas_lenta_ciclista = 0

    print(f"Ingrese las velocidades del ciclista {ciclista} (en km/h) para cada etapa:")
    for etapa in range(1, num_etapas + 1):
        velocidad = float(input(f"Etapa {etapa}: "))
        velocidad_total += velocidad

        # Actualizar velocidad de etapa más rápida y más lenta
        if velocidad < velocidad_etapa_mas_rapida_ciclista:
            velocidad_etapa_mas_rapida_ciclista = velocidad
        if velocidad > velocidad_etapa_mas_lenta_ciclista:
            velocidad_etapa_mas_lenta_ciclista = velocidad

    # Calcular velocidad promedio del ciclista
    velocidad_promedio_ciclista = velocidad_total / num_etapas

    # Actualizar estadísticas generales
    velocidad_promedio_general += velocidad_promedio_ciclista
    if velocidad_promedio_ciclista > 30:
        ciclistas_velocidad_superior_30 += 1
    if velocidad_promedio_ciclista > 25:
        ciclistas_velocidad_superior_25_todas_etapas += 1
    if velocidad_promedio_ciclista > velocidad_promedio_mas_alta:
        velocidad_promedio_mas_alta = velocidad_promedio_ciclista
    if velocidad_promedio_ciclista < velocidad_promedio_mas_baja:
        velocidad_promedio_mas_baja = velocidad_promedio_ciclista
    if velocidad_etapa_mas_rapida_ciclista < velocidad_etapa_mas_rapida:
        velocidad_etapa_mas_rapida = velocidad_etapa_mas_rapida_ciclista
    if velocidad_etapa_mas_lenta_ciclista > velocidad_etapa_mas_lenta:
        velocidad_etapa_mas_lenta = velocidad_etapa_mas_lenta_ciclista

# Calcular velocidad promedio general
velocidad_promedio_general /= num_ciclistas

# Mostrar resultados
print("\nResultados:")
print(f"Velocidad promedio más alta: {velocidad_promedio_mas_alta} km/h")
print(f"Velocidad promedio más baja: {velocidad_promedio_mas_baja} km/h")
print(f"Velocidad promedio general: {velocidad_promedio_general} km/h")
print(f"Ciclistas con velocidad promedio superior a 30 km/h en al menos una etapa: {ciclistas_velocidad_superior_30}")
print(f"Ciclistas con velocidad promedio superior a 25 km/h en todas las etapas: {ciclistas_velocidad_superior_25_todas_etapas}")
print(f"Velocidad de la etapa más rápida en la carrera: {velocidad_etapa_mas_rapida} km/h")
print(f"Velocidad de la etapa más lenta en la carrera: {velocidad_etapa_mas_lenta} km/h")
