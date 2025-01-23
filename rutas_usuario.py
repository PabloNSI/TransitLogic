class RutasUsuario:
    def __init__(self, archivo):
        self.archivo = archivo
        self.rutas = self.cargar_rutas()

    def cargar_rutas(self):
        rutas = []
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    rutas.append(linea.strip())
        except FileNotFoundError:
            pass
        return rutas

    def guardar_ruta(self, inicio, destino, transbordos, tiempo_viaje):
        ruta = "Inicio: " + str(inicio) + ", Destino: " + str(destino) + ", Transbordos: " + str(transbordos) + ", Tiempo de viaje: " + str(tiempo_viaje) + " minutos"

        self.rutas.append(ruta)
        with open(self.archivo, 'a') as file:
            file.write(ruta + '\n')

    def editar_ruta(self, index, inicio, destino, transbordos, tiempo_viaje):
        self.rutas[index] = "Inicio: " + str(inicio) + ", Destino: " + str(destino) + ", Transbordos: " + str(transbordos) + ", Tiempo de viaje: " + str(tiempo_viaje) + " minutos"
        with open(self.archivo, 'w') as file:
            for ruta in self.rutas:
                file.write(ruta + '\n')

    def ver_rutas(self):
        return self.rutas
    
    def eliminar_ruta(self, index):
        try:
            # Eliminamos la ruta de la lista
            ruta_eliminada = self.rutas.pop(index)
            
            # Sobreescribimos el archivo sin la ruta eliminada
            with open(self.archivo, 'w') as file:
                for ruta in self.rutas:
                    file.write(ruta + '\n')
            
            print(f"Ruta eliminada: {ruta_eliminada}")
        except IndexError:
            print("Índice no válido. No se pudo eliminar la ruta.")


    