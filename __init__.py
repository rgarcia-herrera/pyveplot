
# h = hiveplot( G, filename )

# h.add_axis( start, end )

# h.axes[0].add_node( n, offset )

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

    def add_node(n, offset):
        self.nodes.append(n)
