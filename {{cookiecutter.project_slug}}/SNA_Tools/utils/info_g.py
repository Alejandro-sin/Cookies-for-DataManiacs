'''

Este snipet sirve para extraer los datos de centralidad, nodos y relaciones


'''

import networkx as nx
import matplotlib.pyplot as plt




'''
Podemos crear una clase que me devuelva un objeto Reporte

Un reporte puede:

1. Devolver información básica del grafo en conteos.
2. Información detallada de los atributos que hay y relaciones de nodos.
3. Una muestra pequeña de como se ve la data
4. Información sobre la centralidad, una especie de plantilla.

'''

class Reporter(object):


    def __init__(self,name):
        pass


    def basic_info(self, graph):
        pass


    def full_info(self, graph):
        pass

    def small_sample(self, graph):
        pass

    def centrallity_info(self, graph):
        # Degree centrality
        # Betweeness centrality
        # Clossness centrality
        pass