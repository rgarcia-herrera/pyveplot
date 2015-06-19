from pyveplot import *
import networkx, random

# a network
g = networkx.barabasi_albert_graph(50, 2)

# our hiveplot object
h = Hiveplot( 'short_example.svg')
            # start      end
axis0 = Axis( (200,200), (200,100), stroke="grey") 
axis1 = Axis( (200,200), (300,300), stroke="blue")
axis2 = Axis( (200,200), (10,310),  stroke="black")

h.axes = [ axis0, axis1, axis2 ]

# randomly distribute nodes in axes
for n in g.nodes():
    node = Node(n)
    random.choice( h.axes ).add_node( node, random.random() )

for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):       # edges from axis0 to axis1    
        h.connect(axis0, e[0], 45,
                  axis1, e[1], -45,
                  stroke_width='0.34', stroke_opacity='0.4',
                  stroke='purple')
    elif (e[0] in axis0.nodes) and (e[1] in axis2.nodes):     # edges from axis0 to axis2
        h.connect(axis0, e[0], -45,
                  axis2, e[1], 45,
                  stroke_width='0.34', stroke_opacity='0.4',
                  stroke='red')
    elif (e[0] in axis1.nodes) and (e[1] in axis2.nodes):     # edges from axis1 to axis2
        h.connect(axis1, e[0], 15,
                  axis2, e[1], -15,
                  stroke_width='0.34', stroke_opacity='0.4',
                  stroke='magenta')

h.save()
