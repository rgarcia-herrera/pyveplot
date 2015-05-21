
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
        self.axes_lines = self.dwg.add( dwg.g(id='axes_lines', stroke="grey", stroke_opacity="0.5") )
        self.axes = []

    def draw_axes():
        for axis in self.axes:
            self.dwg.add(axis.getDwg())

    def save(self):
        self.draw_axes()
        self.dwg.save()


class axis:
    
    def __init__( self, start=(0,0), end=(0,0), nodes={}):
        self.start = start
        self.end   = end
        self.nodes = nodes
        self.dwg   = svgwrite.Drawing()


    def add_node(node, offset):
        # calculate x,y from offset considering axis start and end points
        width  = self.start[0] - self.end[0]
        height = self.start[1] - self.end[1]        
        node.x = self.start[0] + (width * offset)
        node.y = self.start[1] + (height * offset)
        self.nodes[node.ID] = node

        
    def draw():
        # draw axis
        self.dwg.add( self.dwg.line( start = self.start,
                                     end   = self.end ))
        # draw my nodes
        for node in self.nodes.values():
            self.dwg.add( node.getDwg() )

    def getDwg():
        self.draw()
        return self.dwg
        


class node:
    def __init__(self, ID):
        self.ID = ID
        self.x = 0
        self.y = 0
        self.r = 1*mm
        self.dwg   = svgwrite.Drawing()        
        
    def getDwg():
        self.dwg.add(self.dwg.circle(center = (self.x, self.y),
                                     r      = self.r,
                                     stroke = 'blue',
                                     stroke_width = 0))
        return self.dwg
