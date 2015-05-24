from pyveplot import *                                                                                                                      
import networkx as nx

g = nx.erdos_renyi_graph(10,0.3)

h = Hiveplot(g, 'aguas.svg')

an_axis = Axis( (200,200), (300,100))

n = Node(1)
an_axis.add_node(n, 0.1)
n = Node(2)
an_axis.add_node(n, 0.5)
n = Node(3)
an_axis.add_node(n, 0.999)



another_axis = Axis( (200,200), (300,300) )

n = Node(4)
another_axis.add_node(n, 0.1)
n = Node(5)
another_axis.add_node(n, 0.5)
n = Node(6)
another_axis.add_node(n, 0.999)



# yet_another_axis = axis( (300,300), (410,110) )

# n = node(7)
# yet_another_axis.add_node(n, 0.1)
# n = node(8)
# yet_another_axis.add_node(n, 0.3)
# n = node(9)
# yet_another_axis.add_node(n, 0.6)
# n = node(0)
# yet_another_axis.add_node(n, 0.9)


h.axes.append( an_axis )
h.axes.append( another_axis )
#h.axes.append( yet_another_axis )



h.connect(an_axis, 1, 15,
          another_axis, 4, -15)

h.connect(an_axis, 1, 15,
          another_axis, 5, -15)

h.connect(an_axis, 1, 15,
           another_axis, 6, -15)


h.connect(an_axis, 2, 15,
          another_axis, 4, -15)

h.connect(an_axis, 2, 15,
          another_axis, 5, -15)

h.connect(an_axis, 2, 15,
           another_axis, 6, -15)


h.connect(an_axis, 3, 15,
          another_axis, 4, -15)

h.connect(an_axis, 3, 15,
          another_axis, 5, -15)

h.connect(an_axis, 3, 15,
           another_axis, 6, -15)

h.save()
