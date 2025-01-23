import matplotlib.pyplot as plt
import networkx as nx
import heapq
from estaciones import estaciones, pos
from conexiones import conexiones
from rutas_usuario import RutasUsuario

G = nx.Graph()

# Añadir estaciones (nodos) desde estaciones.py
for estacion in estaciones:
    G.add_node(estacion)

# Añadir conexiones, usando el valor booleano para saber si agregar la conexión
# Desde conexiones.py
for conexion in conexiones:
    if conexion[2]:  # Solo agregar la conexión si existe (True)
        G.add_edge(conexion[0], conexion[1], line=conexion[3], tiempo=conexion[4])

# Inicializar la clase RutasUsuario para manejar las rutas trazadas por el usuario
rutas_usuario = RutasUsuario('rutas_usuario.txt')

def mostrar_menu():
    print("\nOpciones:")
    print("1. Ver rutas guardadas")
    print("2. Editar ruta guardada")
    print("3. Salir")

def ver_rutas_guardadas():
    rutas = rutas_usuario.ver_rutas()
    if rutas:
        print("Rutas guardadas:")
        for ruta in rutas:
            print(f"  - {ruta}")
    else:
        print("No hay rutas guardadas.")

def editar_ruta_guardada():
    rutas = rutas_usuario.ver_rutas()
    if rutas:
        print("Rutas guardadas:")
        for i, ruta in enumerate(rutas):
            print(f"{i + 1}. {ruta}")
        seleccion = int(input("Selecciona el número de la ruta que deseas editar: ")) - 1
        if 0 <= seleccion < len(rutas):
            estacion_origen = input("Introduce la nueva estación de origen: ")
            estacion_destino = input("Introduce la nueva estación de destino: ")
            
            # Normalizar las estaciones
            origen_normalizado = normalizar_cadena(estacion_origen)
            destino_normalizado = normalizar_cadena(estacion_destino)

            if origen_normalizado in estaciones_normalizadas and destino_normalizado in estaciones_normalizadas:
                estacion_origen = estaciones_normalizadas[origen_normalizado]
                estacion_destino = estaciones_normalizadas[destino_normalizado]

                ruta_optima, rutas_lineas = encontrar_ruta_optima(G, estacion_origen, estacion_destino)
                if ruta_optima and rutas_lineas:
                    instrucciones, tiempo_viaje = generar_instrucciones(ruta_optima, rutas_lineas, G)
                    transbordos = len(set(rutas_lineas)) - 1
                    rutas_usuario.editar_ruta(seleccion, estacion_origen, estacion_destino, transbordos, tiempo_viaje)
                    print("Ruta editada y guardada con éxito.")
                else:
                    print("No se pudo encontrar una ruta válida.")
            else:
                print("Una o ambas estaciones no son válidas. Por favor, inténtelo de nuevo.")
        else:
            print("Selección no válida.")
    else:
        print("No hay rutas guardadas.")

def eliminar_ruta_guardada():
    rutas = rutas_usuario.ver_rutas()
    if rutas:
        print("Rutas guardadas:")
        for i, ruta in enumerate(rutas):
            print(f"{i + 1}. {ruta}")
        try:
            seleccion = int(input("Selecciona el número de la ruta que deseas eliminar: ")) - 1
            if 0 <= seleccion < len(rutas):
                rutas_usuario.eliminar_ruta(seleccion)
                print("Ruta eliminada con éxito.")
            else:
                print("Selección no válida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
    else:
        print("No hay rutas guardadas.")

# Función para encontrar la ruta óptima utilizando Dijkstra, considerando transbordos
def encontrar_ruta_optima(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    previos = {nodo: None for nodo in grafo}
    lineas = {nodo: None for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == destino:
            # Construir la ruta y las líneas utilizadas
            ruta = []
            rutas_lineas = []
            while nodo_actual:
                ruta.append(nodo_actual)
                rutas_lineas.append(lineas[nodo_actual])
                nodo_actual = previos[nodo_actual]
            ruta.reverse()
            rutas_lineas.reverse()
            return ruta, rutas_lineas

        for vecino in grafo[nodo_actual]:
            conexion = grafo[nodo_actual][vecino]
            peso = conexion['tiempo']
            linea_actual = conexion['line']

            # Si cambiamos de línea, agregar tiempo por transbordo
            if lineas[nodo_actual] and lineas[nodo_actual] != linea_actual:
                peso += 3  # Tiempo por transbordo

            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                previos[vecino] = nodo_actual
                lineas[vecino] = linea_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    print("No hay ruta disponible de "+str(inicio)+" a "+str(destino))
    return None, None

def generar_instrucciones(ruta_optima, rutas_lineas, grafo):
    instrucciones = []
    tiempo_viaje = 0
    linea_actual = rutas_lineas[0]  # Primera línea de la ruta
    segmento_inicio = ruta_optima[0]  # Inicio del segmento actual

    for i in range(1, len(ruta_optima)):
        estacion_actual = ruta_optima[i - 1]
        estacion_siguiente = ruta_optima[i]
        nueva_linea = rutas_lineas[i]

        # Sumar tiempo de viaje
        tiempo_viaje += grafo[estacion_actual][estacion_siguiente]['tiempo']

        # Detectar cambio de línea o fin de la ruta
        if nueva_linea != linea_actual:
            if estacion_actual != segmento_inicio:  # Evitar imprimir si es la misma estación
                instrucciones.append(
                    "Toma la línea "+str(linea_actual)+" desde "+str(segmento_inicio)+" hasta "+str(estacion_actual)+"."
                )
            segmento_inicio = estacion_actual
            linea_actual = nueva_linea

    # Añadir la última instrucción para llegar al destino
    if ruta_optima:
        instrucciones.append("Toma la línea " + str(linea_actual) + " para llegar a " + str(ruta_optima[-1]))

    return instrucciones, tiempo_viaje

# Normalizar nombres de estaciones
def normalizar_cadena(cadena):
    equivalencias = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u', 'Ñ': 'n'
    }
    return ''.join(equivalencias.get(c, c) for c in cadena).lower()

# Crear un diccionario normalizado de estaciones
estaciones_normalizadas = {normalizar_cadena(estacion): estacion for estacion in G.nodes}

# Solicitar estación de inicio y destino
entrada_inicio = input("Ingrese la estación de inicio: ")
inicio_normalizado = normalizar_cadena(entrada_inicio)
if inicio_normalizado in estaciones_normalizadas:
    inicio = estaciones_normalizadas[inicio_normalizado]
else:
    print("Estación de inicio no válida. Por favor, inténtelo de nuevo.")
    exit()

entrada_destino = input("Ingrese la estación de destino: ")
destino_normalizado = normalizar_cadena(entrada_destino)
if destino_normalizado in estaciones_normalizadas:
    destino = estaciones_normalizadas[destino_normalizado]
else:
    print("Estación de destino no válida. Por favor, inténtelo de nuevo.")
    exit()

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
print("El viajero va de "+str(inicio)+" a "+str(destino))

ruta_optima, rutas_lineas = encontrar_ruta_optima(G, inicio, destino)

# Si la ruta es válida, mostrar instrucciones y tiempo de viaje
if ruta_optima and rutas_lineas:
    instrucciones, tiempo_viaje = generar_instrucciones(ruta_optima, rutas_lineas, G)
    print("Instrucciones de viaje:")
    for instruccion in instrucciones:
        print("  - "+str(instruccion))
    print("\nTiempo total de viaje: "+str(tiempo_viaje)+" minutos.")
    
    # Guardar la ruta en el archivo
    tiempo_total, transbordos, tiempo_transbordos = calcular_tiempo_total(ruta_optima)
    rutas_usuario.guardar_ruta(inicio, destino, transbordos, tiempo_total)

else:
    print("No se pudo encontrar una ruta válida.")



line_colors = {
    "Línea 1": "#68c4dc",
    "Línea 2": "red",
    "Línea 3": "yellow",
    "Línea 4": "#d07404",
    "Línea 5": "#a0bc14",
    "Línea 6": "gray",
    "Línea 7": "#f89c0c",
    "Línea 8": "#eba6c9",
    "Línea 9": "#a02c8c",
    "Línea 10": "#085cac",
    "Línea 11": "#08943c",
    "Línea 12": "#b09c04",
    "Ramal": "steelblue",
}
def alternar_color(parpadeo):
    return "white" if parpadeo % 2 == 0 else "black"

# Mostrar el grafo
ver_grafo = input("¿Quieres ver el grafo con la ruta más corta con el algoritmo de Dijkstra? (si/no): ")
if ver_grafo in ['1', 'sí', 'si', 'yes', 'y', 's']:
    # Preguntar si mostrar todas las etiquetas de nodos o solo las de la ruta óptima
    mostrar_todas_etiquetas = input("¿Quieres ver todos los nombres de los nodos en el grafo? (si/no): ").lower()
    
    # Dibujar el grafo con las posiciones fijas
    edge_colors = [line_colors.get(G[u][v]['line'], 'black') for u, v in G.edges()]
    plt.ion()  # Activar modo interactivo
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # Bucle para parpadear las aristas de la ruta óptima
    for i in range(12):  # Número de parpadeos
        ax.clear()

        # Dibujar todo el grafo
        nx.draw(
            G, pos, node_color="lightgray", node_size=200, font_size=6,
            font_weight="bold", font_color="black", edge_color=edge_colors, width=2
        )

        # Resaltar la ruta óptima
        if ruta_optima:
            path_edges = list(zip(ruta_optima, ruta_optima[1:]))

            # Alternar color para el parpadeo
            color = alternar_color(i)
            nx.draw_networkx_edges(
                G, pos, edgelist=path_edges, edge_color=color, width=3, ax=ax
            )

            # Mostrar solo las etiquetas de los nodos de la ruta óptima
            if mostrar_todas_etiquetas in ['1', 'sí', 'si', 'yes', 'y', 's']:
                # Mostrar todas las etiquetas de nodos
                labels = {nodo: nodo for nodo in G.nodes}
            else:
                # Mostrar solo las etiquetas de los nodos de la ruta óptima
                labels = {nodo: nodo for nodo in ruta_optima}
            
            nx.draw_networkx_labels(
                G, pos, labels=labels, font_size=10, font_weight="bold", font_color="black", ax=ax
            )

        plt.draw()
        plt.pause(0.5)  # Pausa para simular el parpadeo
    plt.ioff()  # Desactivar modo interactivo
    plt.show()

# Mostrar el menú y gestionar las opciones del usuario
while True:
    print("\nOpciones:")
    print("1. Ver rutas guardadas")
    print("2. Editar ruta guardada")
    print("3. Eliminar ruta guardada")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        rutas = rutas_usuario.ver_rutas()
        if rutas:
            print("Rutas guardadas:")
            for i, ruta in enumerate(rutas):
                print(f"{i + 1}. {ruta}")
        else:
            print("No hay rutas guardadas.")
    elif opcion == "2":
        editar_ruta_guardada()
    elif opcion == "3":
        rutas = rutas_usuario.ver_rutas()
        if rutas:
            print("Rutas guardadas:")
            for i, ruta in enumerate(rutas):
                print(f"{i + 1}. {ruta}")
            try:
                seleccion = int(input("Selecciona el número de la ruta que deseas eliminar: ")) - 1
                rutas_usuario.eliminar_ruta(seleccion)
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")
        else:
            print("No hay rutas guardadas.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")