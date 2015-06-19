import svgwrite
from svgwrite import cm, mm
from math import sin, cos, atan2, degrees, radians, tan, sqrt



class Hiveplot:

    def __init__( self, filename):
        self.dwg   = svgwrite.Drawing(filename=filename, debug=True)
        self.axes  = []

    def draw_axes(self):
        for axis in self.axes:
            self.dwg.add(axis.getDwg())



    def connect(self, axis0, n0_index, source_angle, axis1, n1_index, target_angle, **kwargs):
        n0    = axis0.nodes[n0_index]
        n1    = axis1.nodes[n1_index]

        pth  = self.dwg.path(d="M %s %s" % (n0.x, n0.y), fill='none', **kwargs) # source

        # compute source control point
        alfa = axis0.angle() + radians(source_angle)
        length = sqrt( ((n0.x - axis0.start[0])**2) + ((n0.y-axis0.start[1])**2)) 
        x = axis0.start[0] + length * cos(alfa);
        y = axis0.start[1] + length * sin(alfa);

        pth.push("C %s %s" % (x, y)) # first control point in path

        # compute target control point
        alfa = axis1.angle() + radians(target_angle)
        length = sqrt( ((n1.x - axis1.start[0])**2) + ((n1.y-axis1.start[1])**2)) 
        x = axis1.start[0] + length * cos(alfa);
        y = axis1.start[1] + length * sin(alfa);
        
        pth.push("%s %s" % (x, y))   # second control point in path

        pth.push("%s %s" % (n1.x, n1.y)) # target
        self.dwg.add(pth)

            
    def save(self):
        self.draw_axes()
        self.dwg.save()




        
class Axis:
    
    def __init__( self, start=(0,0), end=(0,0), **kwargs):
        self.start = start
        self.end   = end
        self.nodes = {}
        self.dwg   = svgwrite.Drawing()
        self.attrs = kwargs


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
                                     end   = self.end,
                                     **self.attrs ))
        # draw my nodes
        for node in self.nodes.values():
            self.dwg.add( node.getDwg() )

    def getDwg(self):
        self.draw()
        return self.dwg

    def angle (self):
        xDiff = self.end[0] - self.start[0]
        yDiff = self.end[1] - self.start[1]
        return atan2(yDiff, xDiff)



class Node:
    def __init__(self, ID):
        self.ID = ID
        self.x = 0
        self.y = 0
        self.r = 1.5
        self.dwg   = svgwrite.Drawing()        
        
    def getDwg(self):
        return self.dwg



        
