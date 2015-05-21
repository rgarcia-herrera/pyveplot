from pyveplot import *                                                                                                                      
import networkx as nx

g = nx.erdos_renyi_graph(10,0.3)

h = hiveplot(g, 'aguas.svg')
