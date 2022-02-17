'''

Este snipet es para realizar un graficador de los grafos

falta:

graph:
size:
node_color:
with_labels:


'''

import networkx as nx
import matplotlib.pyplot as plt



class Draft(object):

    def __init__(self, graph):
        self.graph = graph
    
    def by_centrallity(graph):
        # Crear grafo en función de los valores de la centralidad
        # Sería un plot de 3 slots que me devuelven 3 gradfos en función de las métricas.
        pass


    def by_node_size(graph, attr):
        # Es un grafo que me grafica en función atributo del grafo al darle como "tamaño" este valor numérico
        pass

    
    def by_relevance(graph):
        # Función para graficar en torno al conjunto de nodos más relevantes.
        pass


    def by_tridimension(graph):
        # Función para graficar de manera tridimensional.
        pass

    