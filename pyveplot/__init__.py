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
from .classes import Hiveplot, Axis, Node
from .utils import UnitConverter, PolarPlotter


__version__ = "0.6.0"
__version_info__ = tuple(int(i) for i in __version__.split('.'))

__all__ = ["Hiveplot", "Axis", "Node", "UnitConverter", "PolarPlotter"]
