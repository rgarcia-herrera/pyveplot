
# h = hiveplot( G, filename )

# an_axis = axis('main', 100, 400)
# an_axis.add_node(n, 0.1)
# an_axis.add_node(n1, 0.15)

# h.add_axis( an_axis )

# h.save()

import svgwrite

from svgwrite import cm, mm

class hiveplot:

    def __init__( self, G, filename):
        self.dwg = svgwrite.Drawing(filename=filename, debug=True)
        self.axes_lines = dwg.add( dwg.g(id='axes_lines') )
        self.axes = {}

    def draw_axes():
        for tag in self.axes:
            self.axes_lines.add( dwg.line( start = self.axes[tag].start,
                                           end   = self.axes[tag].end ))


class axis:
    
    def __init__( self, tag, start, end):
        self.tag   = tag
        self.start = start
        self.end   = end
        self.nodes = []

    def add_node(n, offset):
        self.nodes.append(n)
