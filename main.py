import matplotlib.pyplot as plt
import networkx as nx
import heapq
from estaciones import estaciones
from conexiones import conexiones

G = nx.Graph()

# Añadir estaciones (nodos)
for estacion in estaciones:
    G.add_node(estacion)

# Añadir conexiones, usando el valor booleano para saber si agregar la conexión
for conexion in conexiones:
    if conexion[2]:  # Solo agregar la conexión si existe (True)
        G.add_edge(conexion[0], conexion[1], line=conexion[3], tiempo=conexion[4])

# Función para encontrar la ruta óptima utilizando Dijkstra
def encontrar_ruta_optima(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    previos = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == destino:
            ruta = []
            while nodo_actual is not None:
                ruta.insert(0, nodo_actual)
                nodo_actual = previos[nodo_actual]
            print(f"Ruta óptima de {inicio} a {destino}: {ruta}")
            return ruta

        for vecino in grafo[nodo_actual]:
            peso = grafo[nodo_actual][vecino]["tiempo"]
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                previos[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    print(f"No hay ruta disponible de {inicio} a {destino}.")
    return None

# Normalizar nombres de estaciones
def normalizar_cadena(cadena):
    equivalencias = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u', 'Ñ': 'n'
    }
    return ''.join(equivalencias.get(c, c) for c in cadena).lower()

# Crear un diccionario normalizado de estaciones
estaciones_normalizadas = {normalizar_cadena(estacion): estacion for estacion in G.nodes}

# Solicitar estación de inicio y destino
while True:
    entrada_inicio = input("Ingrese la estación de inicio: ")
    inicio_normalizado = normalizar_cadena(entrada_inicio)
    if inicio_normalizado in estaciones_normalizadas:
        inicio = estaciones_normalizadas[inicio_normalizado]
        break
    print("Estación de inicio no válida. Por favor, inténtelo de nuevo.")

while True:
    entrada_destino = input("Ingrese la estación de destino: ")
    destino_normalizado = normalizar_cadena(entrada_destino)
    if destino_normalizado in estaciones_normalizadas:
        destino = estaciones_normalizadas[destino_normalizado]
        break
    print("Estación de destino no válida. Por favor, inténtelo de nuevo.")

# Calcular el tiempo total del viaje, incluyendo transbordos
def calcular_tiempo_total(ruta_optima):
    tiempo_viaje = 0
    transbordos = 0
    tiempo_transbordos = 0
    linea_anterior = None

    for i in range(len(ruta_optima) - 1):
        estacion_actual = ruta_optima[i]
        estacion_siguiente = ruta_optima[i + 1]
        linea_actual = G[estacion_actual][estacion_siguiente]["line"]

        tiempo_viaje += G[estacion_actual][estacion_siguiente]["tiempo"]

        # Si se realiza un transbordo (la línea cambia), se añaden 3 minutos
        if linea_anterior and linea_anterior != linea_actual:
            transbordos += 1
            tiempo_transbordos += 3  # Añadir 3 minutos por transbordo

        linea_anterior = linea_actual

    return tiempo_viaje, transbordos, tiempo_transbordos

# Mostrar información sobre el viaje
print(f"El viajero va de {inicio} a {destino}")
ruta_optima = encontrar_ruta_optima(G, inicio, destino)

# Si hay ruta, calcular el tiempo total
if ruta_optima:
    tiempo_viaje, transbordos, tiempo_transbordos = calcular_tiempo_total(ruta_optima)
    tiempo_total = tiempo_viaje + tiempo_transbordos

print(f"Tiempo total de viaje: {tiempo_viaje} minutos.")
if transbordos > 0:
    if transbordos == 1:
        print(f"Se ha realizado {transbordos} transbordo, añadiendo {tiempo_transbordos} minutos al tiempo total.")
    else:
        print(f"Se han realizado {transbordos} transbordos, añadiendo {tiempo_transbordos} minutos al tiempo total.")
    print(f"Tiempo total (incluyendo transbordos): {tiempo_total} minutos.")
else:
    print(f"Tiempo total: {tiempo_total} minutos.")

# Posiciones de las estaciones
pos = {
    "Alonso Cano": (765, 510),
    "Alonso Martínez": (735, 585),
    "Argüelles": (535, 540),
    "Avenida de América": (830, 480),
    "Callao": (670, 660),
    "Chamartín": (735, 220),
    "Colombia": (820, 325),
    "Cuatro Caminos": (640, 415),
    "Diego de León": (870, 515),
    "Goya": (870, 600),
    "Manuel Becerra": (910, 560),
    "Moncloa": (500, 518),
    "Nuevos Ministerios": (735, 460),
    "Ópera": (640, 715),
    "Plaza de Castilla": (735, 300),
    "Plaza de España": (600, 575),
    "Príncipe Pío": (572, 632),
    "Sol": (700, 715),
    "Santiago Bernabéu": (735, 380),
    "Tribunal": (685, 585),
    "Velázquez": (830, 600),
}

line_colors = {
    "Línea 1": "lightblue",
    "Línea 2": "red",
    "Línea 3": "yellow",
    "Línea 4": "saddlebrown",
    "Línea 5": "green",
    "Línea 6": "gray",
    "Línea 7": "orange",
    "Línea 8": "pink",
    "Línea 9": "purple",
    "Línea 10": "darkblue",
    "Ramal": "black",
}

# Dibujar el grafo con las posiciones fijas
edge_colors = [line_colors.get(G[u][v]['line'], 'black') for u, v in G.edges()] 
plt.figure(figsize=(12, 12))

# Usar las posiciones fijas para los nodos
nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=3500, font_size=10, font_weight="bold", 
        font_color="black", edge_color=edge_colors, width=3)

# Resaltar la ruta óptima
if ruta_optima:
    path_edges = list(zip(ruta_optima, ruta_optima[1:]))
    # Dibujar los bordes de la ruta óptima con un color distinto
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="black", width=6)

plt.margins(0.1)
plt.show()