from pyveplot import *
from palette import Color
from math import sin, cos, pi
from svgwrite.utils import rgb
import networkx as nx
import numpy as np
import random
import operator


h = Hiveplot( 'example_note.svg')


l = 200
x0 = 1000
y0 = 1600 
theta = 0
delta_theta = (2 * pi) / 5
theta = 0
x1 = x0 + (l * cos (theta))
y1 = y0 + (l * sin (theta))
axis0 = Axis( (x0,y0), # start point
              (x1,y1), # end point
              stroke="magenta", stroke_width=2.5) # pass SVG attributes of axes

# define as many axes as you need

l = 336
x0 = 1000
y0 = 1600 
theta += delta_theta
x1 = x0 + (l * cos (theta))
y1 = y0 + (l * sin (theta))
axis1 = Axis( (x0,y0), (x1,y1), stroke="royalblue", stroke_width=2.5)

l = 564
x0 = 1000
y0 = 1600 
theta += delta_theta

x1 = x0 + (l * cos (theta))
y1 = y0 + (l * sin (theta))
axis2 = Axis( (x0,y0), (x1,y1), stroke="limegreen", stroke_dasharray="4 3", stroke_width=2)


l = 948
x0 = 1000
y0 = 1600 
theta += delta_theta
x1 = x0 + (l * cos (theta))
y1 = y0 + (l * sin (theta))
axis3 = Axis( (x0,y0), (x1,y1), stroke="forestgreen", stroke_dasharray="10 5 5", stroke_width=4)


l = 1512
x0 = 1000
y0 = 1600 
theta = (3 * pi) / 2
x1 = x0 + (l * cos (theta))
y1 = y0 + (l * sin (theta))
axis4 = Axis( (x0,y0), (x1,y1), stroke="midnightblue", stroke_dasharray="10 5 20 5", stroke_width=4)



the_axes = [ axis0,
             axis1,
             axis2, 
             axis3,
             axis4 ]

h.axes = the_axes


g = nx.barabasi_albert_graph(200, 16)



counts, bins = np.histogram(g.degree(g.nodes()).values(), bins=5)
degrees   = g.degree(g.nodes())
sorted_dg = sorted(degrees.items(), key=operator.itemgetter(1))

delta4 = 0.99/float(counts[0])
delta3 = 0.95/float(counts[1])
delta2 = 0.96/float(counts[2])
delta1 = 0.97/float(counts[3])
delta0 = 1/float(counts[4])

offset0 = 0
offset1 = 0
offset2 = 0
offset3 = 0
offset4 = 0


a0_color = Color('#ffee00')
a2_color = Color('#5a004c')
a3_color = Color('#336699')
# place nodes on axes
print "place nodes on axes"
for n,d in sorted_dg:
    nd = Node(n)

    if d >= bins[0] and d < bins[1]:
        offset4 += delta4
        axis4.add_node(nd, offset4)


    if d >= bins[1] and d < bins[2]:
        offset3 += delta3
        axis3.add_node(nd, offset3)


    if d >= bins[2] and d < bins[3]:
        offset2 += delta2
        axis2.add_node(nd, offset2)
        degree = float(nx.degree(g, n)) / 3.0
        nd.dwg = nd.dwg.rect(insert = (nd.x - (degree/2.0), nd.y - (degree/2.0)),
                             size   = (degree, degree),
                             fill   = rgb(a2_color.r*100, a2_color.g*100, a2_color.b*100, mode="%"),
                             stroke_width = 0)
        a2_color = a2_color.lighter(amt=0.02)


    if d >= bins[3] and d < bins[4]:
        offset1 += delta1
        axis1.add_node(nd, offset1)

        if random.choice([True, False]):
            nd.dwg = nd.dwg.circle(center = (nd.x, nd.y),
                                   r      = float(nx.degree(g, n)) / 4.3,
                                   fill   = rgb(a3_color.r*100, a3_color.g*100, a3_color.b*100, mode="%"),
                                   stroke = 'red',
                                   stroke_width = 1.6)
        else:
            degree = float(nx.degree(g, n)) / 3.0
            nd.dwg = nd.dwg.rect(insert = (nd.x - (degree/2.0), nd.y - (degree/2.0)),
                                 size   = (degree, degree),
                                 fill   = rgb(a3_color.r*100, a3_color.g*100, a3_color.b*100, mode="%"),
                                 stroke = rgb(33,66,99),
                                 stroke_width = 0.01)

        a3_color = a3_color.lighter(amt=0.08)



    if d >= bins[4] and d < bins[5]:
        offset0 += delta0
        axis0.add_node(nd, offset0)
        if random.choice([True, False]):
            nd.dwg = nd.dwg.circle(center = (nd.x, nd.y),
                                   r      = float(nx.degree(g, n)) / 5.0,
                                   fill   = rgb(a0_color.r*100, a0_color.g*100, a0_color.b*100, mode="%"),
                                   stroke_width = 0)
        else:
            degree = float(nx.degree(g, n)) / 3.0
            nd.dwg = nd.dwg.rect(insert = (nd.x - (degree/2.0), nd.y - (degree/2.0)),
                                 size   = (degree, degree),
                                 fill   = rgb(a0_color.r*100, a0_color.g*100, a0_color.b*100, mode="%"),
                                 stroke_width = 0)

        a0_color = a0_color.darker(amt=0.05)


        

    


# edges from axis0 to axis1
for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):
        h.connect(axis0, e[0],
                  45,  # source angle
                  axis1, e[1], 
                  -45, # target angle
                  stroke_width=1,  # pass any SVG attributes to an edge
                  stroke_opacity=0.7,
                  stroke='indigo',
                  fill='none')

# edges from axis1 to axis2
for e in g.edges():
    if (e[0] in axis1.nodes) and (e[1] in axis2.nodes):
        h.connect(axis1, e[0], 45,
                  axis2, e[1], -45,
                  stroke_width=0.85,
                  stroke_opacity=0.7,
                  stroke=random.choice(['gold','salmon','orange']),
                  fill='none')

# edges from axis2 to axis3
for e in g.edges():
    if (e[0] in axis2.nodes) and (e[1] in axis3.nodes):
        h.connect(axis2, e[0], 45,
                  axis3, e[1], -45,
                  stroke_width=0.6,
                  stroke_opacity=0.5,
                  stroke=random.choice(['magenta','mediumblue','orchid','mediumpurple']),
                  fill='none')



# edges from axis3 to axis4
for e in g.edges():
    if (e[0] in axis3.nodes) and (e[1] in axis4.nodes):
        h.connect(axis3, e[0], 35,
                  axis4, e[1], -35,
                  stroke_width='0.34',
                  stroke_opacity='0.8',
                  stroke=random.choice(['seagreen','slateblue','lawngreen']),
                  fill='none')


# edges from axis4 to axis0
for e in g.edges():
    if (e[0] in axis4.nodes) and (e[1] in axis0.nodes):
        h.connect(axis4, e[0], 45,
                  axis0, e[1], -45,
                  stroke_width=2,
                  stroke_opacity='0.4',
                  stroke='crimson',
                  fill='none')


print "writing file"
h.save()
