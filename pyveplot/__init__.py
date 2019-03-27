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
from pyveplot.classes import Hiveplot, Axis, Node

__all__ = ["Hiveplot", "Axis", "Node"]
