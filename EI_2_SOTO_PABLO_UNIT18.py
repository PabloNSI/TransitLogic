import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

                                                    # ESTACIONES
G.add_node("Alonso Cano")
G.add_node("Alonso Martínez")
G.add_node("Avenida de América")
G.add_node("Argüelles")
G.add_node("Callao")
G.add_node("Chamartín")
G.add_node("Colombia")
G.add_node("Cuatro Caminos")
G.add_node("Diego de León")
G.add_node("Goya")
G.add_node("Manuel Becerra")
G.add_node("Moncloa")
G.add_node("Nuevos Ministerios")
G.add_node("Ópera")
G.add_node("Plaza de Castilla")
G.add_node("Plaza de España")  # Con Noviciado para línea 2
G.add_node("Príncipe Pío")
G.add_node("Santiago Bernabéu")
G.add_node("Sol")
G.add_node("Tribunal")
G.add_node("Velázquez")


                                                    # CONEXIONES


# Alonso Cano
G.add_edge("Alonso Cano", "Avenida de América", line="Línea 7")

# Alonso Martínez
G.add_edge("Alonso Martínez", "Argüelles", line="Línea 4")
G.add_edge("Alonso Martínez", "Velázquez", line="Línea 4")
G.add_edge("Alonso Martínez", "Callao", line="Línea 5")
G.add_edge("Alonso Martínez", "Diego de León", line="Línea 5")
G.add_edge("Alonso Martínez", "Tribunal", line="Línea 10")
G.add_edge("Alonso Martínez", "Nuevos Ministerios", line="Línea 10")

# Avenida de América
G.add_edge("Avenida de América", "Diego de León", line="Línea 4")
G.add_edge("Avenida de América", "Alonso Cano", line="Línea 7")
G.add_edge("Avenida de América", "Colombia", line="Línea 9")

# Argüelles
G.add_edge("Argüelles", "Moncloa", line="Línea 3")
G.add_edge("Argüelles", "Plaza de España", line="Línea 3")
G.add_edge("Argüelles", "Alonso Martínez", line="Línea 4")
G.add_edge("Argüelles", "Príncipe Pío", line="Línea 6")
G.add_edge("Argüelles", "Moncloa", line="Línea 6")

# Callao
G.add_edge("Callao", "Sol", line="Línea 3")
G.add_edge("Callao", "Plaza de España", line="Línea 3")
G.add_edge("Callao", "Ópera", line="Línea 5")
G.add_edge("Callao", "Alonso Martínez", line="Línea 5")

# Chamartín
G.add_edge("Chamartín", "Plaza de Castilla", line="Línea 10")
G.add_edge("Chamartín", "Plaza de Castilla", line="Línea 1")

# Colombia
G.add_edge("Colombia", "Nuevos Ministerios", line="Línea 8")
G.add_edge("Colombia", "Avenida de América", line="Línea 9")
G.add_edge("Colombia", "Plaza de Castilla", line="Línea 9")

# Cuatro Caminos
G.add_edge("Cuatro Caminos", "Tribunal", line="Línea 1")
G.add_edge("Cuatro Caminos", "Plaza de Castilla", line="Línea 1")
G.add_edge("Cuatro Caminos", "Plaza de España", line="Línea 2")

# Diego de León
G.add_edge("Diego de León", "Avenida de América", line="Línea 4")
G.add_edge("Diego de León", "Goya", line="Línea 4")
G.add_edge("Diego de León", "Alonso Martínez", line="Línea 5")
G.add_edge("Diego de León", "Avenida de América", line="Línea 6")
G.add_edge("Diego de León", "Manuel Becerra", line="Línea 6")

# Goya
G.add_edge("Goya", "Manuel Becerra", line="Línea 2")
G.add_edge("Goya", "Sol", line="Línea 2")
G.add_edge("Goya", "Diego de León", line="Línea 4")
G.add_edge("Goya", "Velázquez", line="Línea 4")

# Manuel Becerra
G.add_edge("Manuel Becerra", "Goya", line="Línea 2")
G.add_edge("Manuel Becerra", "Diego de León", line="Línea 6")

# Moncloa
G.add_edge("Moncloa", "Argüelles", line="Línea 3")
G.add_edge("Moncloa", "Argüelles", line="Línea 6")
G.add_edge("Moncloa", "Cuatro Caminos", line="Línea 6")

# Nuevos Ministerios
G.add_edge("Nuevos Ministerios", "Avenida de América", line="Línea 6")
G.add_edge("Nuevos Ministerios", "Cuatro Caminos", line="Línea 6")
G.add_edge("Nuevos Ministerios", "Colombia", line="Línea 8")
G.add_edge("Nuevos Ministerios", "Alonso Martínez", line="Línea 10")
G.add_edge("Nuevos Ministerios", "Santiago Bernabéu", line="Línea 10")

# Ópera
G.add_edge("Ópera", "Sol", line="Línea 2")
G.add_edge("Ópera", "Plaza de España", line="Línea 2")
G.add_edge("Ópera", "Callao", line="Línea 5")
G.add_edge("Ópera", "Príncipe Pío", line="Ramal")

# Plaza de Castilla
G.add_edge("Plaza de Castilla", "Cuatro Caminos", line="Línea 1")
G.add_edge("Plaza de Castilla", "Chamartín", line="Línea 1")
G.add_edge("Plaza de Castilla", "Colombia", line="Línea 9")
G.add_edge("Plaza de Castilla", "Chamartín", line="Línea 10")
G.add_edge("Plaza de Castilla", "Santiago Bernabéu", line="Línea 10")

# Plaza de España
G.add_edge("Plaza de España", "Cuatro Caminos", line="Línea 2")
G.add_edge("Plaza de España", "Ópera", line="Línea 2")
G.add_edge("Plaza de España", "Callao", line="Línea 3")
G.add_edge("Plaza de España", "Argüelles", line="Línea 3")
G.add_edge("Plaza de España", "Príncipe Pío", line="Línea 10")
G.add_edge("Plaza de España", "Tribunal", line="Línea 10")

# Príncipe Pío
G.add_edge("Príncipe Pío", "Ópera", line="Ramal")
G.add_edge("Príncipe Pío", "Argüelles", line="Línea 6")
G.add_edge("Príncipe Pío", "Plaza de España", line="Línea 10")

# Santiago Bernabéu
G.add_edge("Santiago Bernabéu", "Plaza de Castilla", line="Línea 10")
G.add_edge("Santiago Bernabéu", "Nuevos Ministerios", line="Línea 10")

# Sol
G.add_edge("Sol", "Tribunal", line="Línea 1")
G.add_edge("Sol", "Goya", line="Línea 2")
G.add_edge("Sol", "Ópera", line="Línea 2")
G.add_edge("Sol", "Callao", line="Línea 3")

# Tribunal
G.add_edge("Tribunal", "Cuatro Caminos", line="Línea 1")
G.add_edge("Tribunal", "Sol", line="Línea 1")
G.add_edge("Tribunal", "Plaza de España", line="Línea 10")
G.add_edge("Tribunal", "Alonso Martínez", line="Línea 10")

# Velázquez
G.add_edge("Velázquez", "Goya", line="Línea 4")
G.add_edge("Velázquez", "Alonso Martínez", line="Línea 4")


                                        # POSICIÓN DE LOS NODOS
                                    # Y COLORES CORRESPONDIENTES


pos = {
"Alonso Cano": (765,510),
"Alonso Martínez": (735,585),
"Argüelles": (535,540),
"Avenida de América": (830,480),
"Callao": (670,660),
"Chamartín": (735,220),
"Colombia": (820,325),
"Cuatro Caminos": (640,415),
"Diego de León": (870,515),
"Goya": (870,600),
"Manuel Becerra": (910,560),
"Moncloa": (500,518),
"Nuevos Ministerios": (735,460),
"Ópera": (640, 715),
"Plaza de Castilla": (735,300),
"Plaza de España": (600,575),
"Príncipe Pío": (572,632),
"Sol": (700,715),
"Santiago Bernabéu": (735,380),
"Tribunal": (685,585),
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
edge_colors = [line_colors.get(G[u][v]['line'], 
'black') for u, v in G.edges()]

                                            # SE DIBUJA EL GRAFO

plt.figure(figsize=(12, 12))
nx.draw(
    G, 
    pos, 
    with_labels=True, 
    node_color="lightgray",
    node_size=3500, 
    font_size=10, 
    font_weight="bold", 
    font_color="black", 
    edge_color=edge_colors,
    width=3
)


def encontrar_ruta_optima(grafo, inicio, destino, algoritmo="dijkstra"):
    if algoritmo == "dijkstra":
        try:
            ruta = nx.shortest_path(grafo, source=inicio, target=destino, weight=None, method='dijkstra')
            print(f"Ruta óptima de {inicio} a {destino} usando Dijkstra: {ruta}")
        except nx.NetworkXNoPath:
            print(f"No hay ruta disponible de {inicio} a {destino}.")
    elif algoritmo == "floyd-warshall":
        try:
            ruta = nx.shortest_path(grafo, source=inicio, target=destino, weight=None, method='floyd-warshall')
            print(f"Ruta óptima de {inicio} a {destino} usando Floyd-Warshall: {ruta}")
        except nx.NetworkXNoPath:
            print(f"No hay ruta disponible de {inicio} a {destino}.")
    return ruta

while True:
    inicio = input("Ingrese la estación de inicio: ")
    if inicio in G:
        break
    print("Estación de inicio no válida. Por favor, inténtelo de nuevo.")

while True:
    destino = input("Ingrese la estación de destino: ")
    if destino in G:
        break
    print("Estación de destino no válida. Por favor, inténtelo de nuevo.")
print ("El viajero va de "+str(inicio)+" a "+str(destino))
ruta_optima = encontrar_ruta_optima(G, inicio, destino, algoritmo="dijkstra")

plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=3500, font_size=10, font_weight="bold",
        font_color="black", edge_color=edge_colors, width=3)

path_edges = list(zip(ruta_optima, ruta_optima[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="black", width=6)
plt.margins(0.1)
plt.tight_layout()
plt.show()



            # PARA CALCULAR DISTANCIAS, USA LOS VALORES DE POSICION (X,Y) Y ASI MEDIR LAS DISTANCIAS
# DEBES COMPARAR ESAS DISTANCIAS CON LAS REALES, Y AÑADIR LA VARIABLE DE TIEMPO ENTRE LAS PARADAS DEPENDIENDO TMB DE LA LINEA
