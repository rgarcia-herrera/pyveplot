# -*- coding: utf-8 -*-
"""
The creation of a Hive plot with Pyveplot is a straightforward
process. A Hive plot consists of:

* radialy distributed linear axes
* nodes along those axes
* conections among those nodes

Pyveplots provides the corresponding objects: a *Hiveplot* class
which contains an arbitrary number of *Axis* objects which in
turn contain an arbitrary number of *Node* objects, and a method
to connect them.
"""
import svgwrite
from svgwrite import cm, mm
from math import sin, cos, atan2, degrees, radians, tan, sqrt



class Hiveplot:
    """
    Base class for a Hive plot.

    Example
    -------
    ::
        from pyveplot import *
        import networkx, random
    
        # a network
        g = networkx.barabasi_albert_graph(50, 2)
    
        # our hiveplot object
        h = Hiveplot( 'short_example.svg')
                        # start     end
        h.axes = [Axis( (200,200), (200,100), stroke="grey"),
                  Axis( (200,200), (300,300), stroke="blue"),
                  Axis( (200,200), (10,310),  stroke="black")]
    
        # randomly distribute nodes in axes
        for n in g.nodes():
            random.choice( h.axes ).add_node( Node(n), random.random() )
    
        for e in g.edges():
            if (e[0] in h.axes[0].nodes) and (e[1] in h.axes[1].nodes):
                # edges from axis0 to axis1    
                h.connect(h.axes[0], e[0], 45,
                          h.axes[1], e[1], -45,
                          stroke_width='0.34', stroke_opacity='0.4', stroke='purple')
            elif (e[0] in axis0.nodes) and (e[1] in axis2.nodes):
                # edges from axis0 to axis2
                h.connect(h.axes[0], e[0], -45,
                          h.axes[2], e[1], 45,
                          stroke_width='0.34', stroke_opacity='0.4', stroke='red')
            elif (e[0] in axis1.nodes) and (e[1] in axis2.nodes):
                # edges from axis1 to axis2
                h.connect(h.axes[1], e[0], 15,
                          h.axes[2], e[1], -15,
                          stroke_width='0.34', stroke_opacity='0.4', stroke='magenta')
    
        h.save()

    """
    def __init__( self, filename):
        self.dwg   = svgwrite.Drawing(filename=filename, debug=True)
        self.axes  = []

    def draw_axes(self):
        for axis in self.axes:
            self.dwg.add(axis.getDwg())


    def connect(self, axis0, n0_index, source_angle, axis1, n1_index, target_angle, **kwargs):
        """Draw edges as Bézier curves.

        Start and end points map to the coordinates of the given nodes
        which in turn are set when adding nodes to an axis with the
        Axis.add_node() method, by using the placement information of
        the axis and a specified offset from its start point.
        
        Control points are set at the same distance from the start (or end)
        point of an axis as their corresponding nodes, but along an invisible
        axis that shares its origin but diverges by a given angle.


        Parameters
        ----------
        axis0        : source Axis object
        n0_index     : key of source node in nodes dictionary of axis0
        source_angle : angle of departure for invisible axis that diverges from axis0 and holds first control points
        axis1        : target Axis object
        n1_index     : key of target node in nodes dictionary of axis1
        target_angle : angle of departure for invisible axis that diverges from axis1 and holds second control points
        kwargs       : extra SVG attributes for path element, optional
                       Set or change attributes using key=value

        """        
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
        """Initialize Axis object with start, end positions and optional SVG attributes

        Parameters
        ----------
        start  : ( x, y ) start point of the axis
        end    : (x1, y1) end point of the axis
        kwargs : extra SVG attributes for line element, optional
                 Set or change attributes using key=value

        Example
        -------
        >>> axis0 = Axis( (150, 200), # start
                          (150, 0),   # end
                          stroke="black", stroke_width=1.5) # pass SVG attributes of axes
        
        """
        self.start = start
        self.end   = end
        self.nodes = {}
        self.dwg   = svgwrite.Drawing()
        self.attrs = kwargs


    def add_node(self, node, offset):
        """Add a Node object to nodes dictionary, calculating its coordinates using offset

        Parameters
        ----------
        node   : a Node object
        offset : float 
                 number between 0 and 1 that sets the distance
                 from the start point at which the node will be placed

        """
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
    """Base class for Node objects. 

    Holds coordinates for node placement and a svgwrite.Drawing()
    object in the *dwg* attribute.

    """
    def __init__(self, ID):
        """
        Parameters
        ----------
        ID: a unique key for the nodes dict of an axis.
        """
        self.ID = ID
        self.x = 0
        self.y = 0
        # self.r = 1.5
        self.dwg   = svgwrite.Drawing()        
        
    def getDwg(self):
        return self.dwg



        
