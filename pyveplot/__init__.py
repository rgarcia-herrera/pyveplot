
# h = hiveplot( G, filename )

# an_axis = axis( 100, 400)
# an_axis.add_node(n, 0.1)
# an_axis.add_node(n1, 0.15)

# h.axes.append( an_axis )

# h.save()

import svgwrite
from svgwrite import cm, mm


class hiveplot:

    def __init__( self, G, filename):
        self.dwg = svgwrite.Drawing(filename=filename, debug=True)
        self.axes_lines = self.dwg.add( self.dwg.g(id='axes_lines', stroke="grey", stroke_opacity="0.5") )
        self.axes  = []
        self.nodes = {}
        self.G = G

    def draw_axes(self):
        for axis in self.axes:
            self.axes_lines.add(axis.getDwg())

    def draw_edges(self):
        for a in self.axes:
            for n in a.nodes.values():
                self.nodes[n.ID] = n
        
        edges = self.dwg.add( self.dwg.g(id='edges', stroke='red', stroke_opacity='0.4'))
        for e in self.G.edges():
            n0 = self.nodes[e[0]]
            n1 = self.nodes[e[1]]
            edges.add(
                self.dwg.line( start = (n0.x, n0.y),
                               end   = (n1.x, n1.y)))

            
    def save(self):
        self.draw_axes()
        self.dwg.add( self.axes_lines )
        self.draw_edges()
        self.dwg.save()




        
class axis:
    
    def __init__( self, start=(0,0), end=(0,0), nodes={}):
        self.start = start
        self.end   = end
        self.nodes = nodes
        self.dwg   = svgwrite.Drawing()


    def add_node(self, node, offset):
        # calculate x,y from offset considering axis start and end points
        width  = self.end[0] - self.start[0]
        height = self.end[1] - self.start[1]        
        node.x = self.start[0] + (width * offset)
        node.y = self.start[1] + (height * offset)
        self.nodes[node.ID] = node

        
    def draw(self):
        # draw axis
        self.dwg.add( self.dwg.line( start = self.start,
                                     end   = self.end ))
        # draw my nodes
        for node in self.nodes.values():
            self.dwg.add( node.getDwg() )

    def getDwg(self):
        self.draw()
        return self.dwg
        


class node:
    def __init__(self, ID):
        self.ID = ID
        self.x = 0
        self.y = 0
        self.r = 1*mm
        self.dwg   = svgwrite.Drawing()        
        
    def getDwg(self):
        self.dwg.add(self.dwg.circle(center = (self.x, self.y),
                                     r      = self.r,
                                     stroke = 'blue',
                                     stroke_width = 0))
        return self.dwg



        
