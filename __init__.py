
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
        self.axes_lines = dwg.add( dwg.g(id='axes_lines', stroke="grey", stroke_opacity="0.5") )
        self.axes = []

    def draw_axes():
        for axis in self.axes:
            axis.draw()
            self.dwg.add(axis.dwg)

    def save(self):
        self.draw_axes()
        self.dwg.save()


class axis:
    
    def __init__( self, start, end):
        self.start = start
        self.end   = end
        self.nodes = []
        self.dwg   = svgwrite.Drawing()

    def add_node(n, offset):
        self.nodes.append(n)
        # calculate x,y from offset considering axis angle and size


    def draw():
        self.dwg.add( self.dwg.line( start = self.start,
                                     end   = self..end ))
        # draw my nodes

        

