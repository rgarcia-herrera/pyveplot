from pyveplot import *                                                                                                                      
import networkx as nx

g = nx.erdos_renyi_graph(10,0.3)

h = hiveplot(g, 'aguas.svg')

an_axis = axis( (10,10), (100,100))

n = node(1)
an_axis.add_node(n, 0.1)
n = node(2)
an_axis.add_node(n, 0.5)
n = node(3)
an_axis.add_node(n, 0.999)



another_axis = axis( (10,10), (-100,10) )

n = node(4)
another_axis.add_node(n, 0.1)
n = node(5)
another_axis.add_node(n, 0.5)
n = node(6)
another_axis.add_node(n, 0.999)



yet_another_axis = axis( (10,10), (10,-200) )

n = node(7)
yet_another_axis.add_node(n, 0.1)
n = node(8)
yet_another_axis.add_node(n, 0.3)
n = node(9)
yet_another_axis.add_node(n, 0.6)
n = node(0)
yet_another_axis.add_node(n, 0.9)


h.axes.append( an_axis )
h.axes.append( another_axis )
h.axes.append( yet_another_axis )

h.save()
