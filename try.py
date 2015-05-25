from pyveplot import *
import networkx as nx
import random


h = Hiveplot( 'example.svg')

axis0 = Axis( (200,200), (200,100))
axis1 = Axis( (200,200), (300,300))
axis2 = Axis( (200,200), (10,310))

h.axes.append( axis0 )
h.axes.append( axis1 )
h.axes.append( axis2 )


# a random network
g = nx.erdos_renyi_graph(100,0.3)

# distribute nodes in axes
the_axes = [ axis0,
             axis1,
             axis2, ]
for n in g.nodes():
    n = Node(n)
    a = random.choice(the_axes)
    # at random offsets
    a.add_node(n, random.random())




# edges from axis0 to axis1
for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):
        h.connect(axis0, e[0], 45,
                  axis1, e[1], -45,
                  stroke_width='0.34',
                  stroke_opacity='0.5',
                  stroke='green',
                  fill='none')

# edges from axis0 to axis2
for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis2.nodes):
        h.connect(axis0, e[0], -45,
                  axis2, e[1], 45,
                  stroke_width='0.34',
                  stroke_opacity='0.8',
                  stroke='red',
                  fill='none')

# edges from axis1 to axis2
for e in g.edges():
    if (e[0] in axis1.nodes) and (e[1] in axis2.nodes):
        h.connect(axis1, e[0], 15,
                  axis2, e[1], -15,
                  stroke_width='0.34',
                  stroke_opacity='0.7',
                  stroke='blue',
                  fill='none')

    

h.save()
