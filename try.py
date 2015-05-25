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

# randomly distribute nodes in axes
the_axes = [ axis0,
             axis1,
             axis2, ]
for n in g.nodes():
    nd = Node(n)
    a = random.choice(the_axes)
    # at random offsets, add_node method calculates node's x,y
    a.add_node(nd, random.random())

    # alter node drawing after adding it to axis
    if random.choice([True, False]):
        nd.dwg = nd.dwg.circle(center = (nd.x, nd.y),
                               r      = float(nx.degree(g, n)) / 20.0,
                               fill   = 'orange',
                               stroke = random.choice(['red','green','blue','purple']),
                               stroke_width = 0.1)
    else:
        # nodes' drawings can be any svg shape
        degree = float(nx.degree(g, n)) / 20.0
        nd.dwg = nd.dwg.rect(insert = (nd.x - (degree/2.0), nd.y - (degree/2.0)),
                             size   = (degree, degree),
                             fill   = 'green',
                             stroke = random.choice(['red','green','blue','purple']),
                             stroke_width = 0.1)




# edges from axis0 to axis1
for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):
        # pass any SVG attributes to an edge
        h.connect(axis0, e[0],
                  45,  # source angle
                  axis1, e[1], 
                  -45, # target angle
                  stroke_width='0.34',
                  stroke_opacity='0.4',
                  stroke='purple',
                  fill='none')

# edges from axis0 to axis2
for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis2.nodes):
        h.connect(axis0, e[0], -45,
                  axis2, e[1], 45,
                  stroke_width='0.34',
                  stroke_opacity='0.4',
                  stroke='red',
                  fill='none')

# edges from axis1 to axis2
for e in g.edges():
    if (e[0] in axis1.nodes) and (e[1] in axis2.nodes):
        h.connect(axis1, e[0], 15,
                  axis2, e[1], -15,
                  stroke_width='0.34',
                  stroke_opacity='0.4',
                  stroke='blue',
                  fill='none')

    

h.save()
