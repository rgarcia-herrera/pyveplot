from pyveplot import *                                                                                                                      
import networkx as nx
import random
from itertools import combinations

h = Hiveplot( 'aguas.svg')

the_axes = [
    Axis( (200,200), (300,100)),
    Axis( (200,200), (300,300)),
    Axis( (200,200), (10,310)) ]

for a in the_axes:
    h.axes.append( a )

g = nx.erdos_renyi_graph(100,0.3)

for n in g.nodes():
    n = Node(n)
    a = random.choice(the_axes)
    a.add_node(n, random.random())



for a in combinations(the_axes, 2):
    a0 = a[0]
    a1 = a[1]

    for e in g.edges():
        if (e[0] in a0.nodes) and (e[1] in a1.nodes):
            h.connect(a0, e[0], 15,
                      a1, e[1], 15)
    

h.save()
