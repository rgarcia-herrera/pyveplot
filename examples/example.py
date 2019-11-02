from pyveplot import *
import networkx as nx
import random


h = Hiveplot( 'example.svg')


axis0 = Axis( (150, 200), # start
              (150, 0),   # end
              stroke="black", stroke_dasharray="4 2", stroke_width=1.5) # pass SVG attributes of axes
# define as many axes as you need
axis1 = Axis( (150,200), (300,300), stroke="yellowgreen", stroke_width=2, stroke_opacity=0.6 )
axis2 = Axis( (150,200), (  0,300), stroke="blue", stroke_opacity="0.3", stroke_width=2)

h.axes = [ axis0, axis1, axis2 ]



# a random network
g = nx.erdos_renyi_graph(70, 0.3)




# randomly distribute nodes in axes
for n in g.nodes():
    nd = Node(n)
    a = random.choice(h.axes)
    # at random offsets, add_node method calculates node's x,y
    a.add_node(nd, random.random())

    # alter node drawing after adding it to axis to keep coordinates
    if random.choice([True, False]):
        nd.dwg = nd.dwg.circle(center = (nd.x, nd.y),
                               r      = float(nx.degree(g, n)) / 10.0,
                               fill   = 'orange',
                               fill_opacity = 0.5,
                               stroke = random.choice(['red','crimson','coral','purple']),
                               stroke_width = 0.3)
    else:
        # nodes' drawings can be any SVG shape
        degree = float(nx.degree(g, n)) / 5.0
        nd.dwg = nd.dwg.rect(insert = (nd.x - (degree/2.0), nd.y - (degree/2.0)),
                             size   = (degree, degree),
                             fill   = 'midnightblue',
                             fill_opacity = 0.5,
                             stroke = random.choice(['royalblue','indigo','blue','purple']),
                             stroke_width = 0.5)



# edges from axis0 to axis1
for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):
        h.connect(axis0, e[0],
                  45,  # angle of invisible axis for source control points
                  axis1, e[1], 
                  -45, # angle of invisible axis for target control points
                  stroke_width   = 0.34,  # pass any SVG attributes to an edge
                  stroke_opacity = 0.4,
                  stroke         = 'purple',
                  )
    if (e[1] in axis0.nodes) and (e[0] in axis1.nodes):
        h.connect(axis0, e[1], 45,  
                  axis1, e[0], -45, 
                  stroke_width   = 0.34,  # pass any SVG attributes to an edge
                  stroke_opacity = 0.4,
                  stroke         = 'purple',
                  )

        
    # edges from axis1 to axis2
    if (e[0] in axis1.nodes) and (e[1] in axis2.nodes):
        h.connect(axis1, e[0], 15,
                  axis2, e[1], -15,
                  stroke_width   = 0.34,
                  stroke_opacity = 0.4,
                  stroke         = random.choice(['blue', 'red', 'purple', 'green', 'magenta']),
                  )

    if (e[1] in axis1.nodes) and (e[0] in axis2.nodes):
        h.connect(axis1, e[1], 15,
                  axis2, e[0], -15,
                  stroke_width   = 0.34,
                  stroke_opacity = 0.4,
                  stroke         = random.choice(['blue', 'red', 'purple', 'green', 'magenta']),
                  )
        
    # edges from axis0 to axis2
    if (e[0] in axis0.nodes) and (e[1] in axis2.nodes):
        h.connect(axis0, e[0], -45,
                  axis2, e[1], 45,
                  stroke_width   = 0.34,
                  stroke_opacity = 0.4,
                  stroke         = 'red',
                  )

    if (e[1] in axis0.nodes) and (e[0] in axis2.nodes):
        h.connect(axis0, e[1], -45,
                  axis2, e[0], 45,
                  stroke_width   = 0.34,
                  stroke_opacity = 0.9,
                  stroke         = 'crimson',
                  )

        

h.save()
