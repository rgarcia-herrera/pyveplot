Pyveplot
========

A nice way of visualizing complex networks are `Hiveplots <http://www.hiveplot.com/>`_.


This library uses `svgwrite <http://svgwrite.readthedocs.org/en/latest/classes/shapes.html>`_ to 
programmatically create images like this one:

.. image:: https://github.com/CSB-IG/pyveplot/raw/master/example.png


A short example
---------------

Create a plot from a network, randomly selecting whichever axis to place 50 nodes.::

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


.. image:: https://github.com/CSB-IG/pyveplot/raw/master/short_example.png
  
The more elaborate `example.py <https://github.com/CSB-IG/pyveplot/blob/master/example.py>`_ 
shows how to use shapes for nodes, placement of the control points and attributes of edges, and the attributes
of axes.


Installation
------------

Install library, perhaps within a virtualenv::

    $ pip install pyveplot


