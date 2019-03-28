from __future__ import absolute_import, division, unicode_literals, print_function
import os
import random
import shutil
import sys
from datetime import datetime
from collections import Counter

import pytest
import networkx

from pyveplot import Hiveplot, Axis, Node


TEST_DIR = os.path.dirname(os.path.realpath(__file__))


def assert_same_contents(fpath1, fpath2):
    with open(fpath1) as f1, open(fpath2) as f2:
        assert f1.read() == f2.read()


def assert_same_lines(fpath1, fpath2):
    with open(fpath1) as f1, open(fpath2) as f2:
        assert Counter(f1.readlines()) == Counter(f2.readlines())


def test_short_example(tmpdir, request):
    fname = "short_example.svg"
    ref_fpath = os.path.join(TEST_DIR, fname)
    test_fpath = str(tmpdir.join(fname))

    # seed must be the same
    random.seed(1)

    # a network
    g = networkx.barabasi_albert_graph(50, 2, seed=2)

    # our hiveplot object
    h = Hiveplot(test_fpath)
    # start      end
    axis0 = Axis((200, 200), (200, 100), stroke="grey")
    axis1 = Axis((200, 200), (300, 300), stroke="blue")
    axis2 = Axis((200, 200), (10, 310), stroke="black")

    h.axes = [axis0, axis1, axis2]

    # randomly distribute nodes in axes
    for n in g.nodes():
        node = Node(n)
        random.choice(h.axes).add_node(node, random.random())

    for e in g.edges():
        if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):  # edges from axis0 to axis1
            h.connect(axis0, e[0], 45,
                      axis1, e[1], -45,
                      stroke_width='0.34', stroke_opacity='0.4',
                      stroke='purple')
        elif (e[0] in axis0.nodes) and (e[1] in axis2.nodes):  # edges from axis0 to axis2
            h.connect(axis0, e[0], -45,
                      axis2, e[1], 45,
                      stroke_width='0.34', stroke_opacity='0.4',
                      stroke='red')
        elif (e[0] in axis1.nodes) and (e[1] in axis2.nodes):  # edges from axis1 to axis2
            h.connect(axis1, e[0], 15,
                      axis2, e[1], -15,
                      stroke_width='0.34', stroke_opacity='0.4',
                      stroke='magenta')

    h.save(pretty=True)

    try:
        if sys.version_info >= (3, 6):
            assert_same_contents(ref_fpath, test_fpath)
        # elif (3, 0) < sys.version_info < (3, 6):
        else:
            # cannot check for exact identity in CPython < 3.6 due to
            # non-deterministic dict ordering
            assert_same_lines(ref_fpath, test_fpath)
    except AssertionError:
        if request.config.getoption("--dump"):
            ver = '.'.join(str(i) for i in sys.version_info)
            dt = datetime.now().isoformat().replace(':', '-')
            shutil.copyfile(test_fpath, os.path.join(TEST_DIR, '_'.join([ver, dt, fname])))
        if sys.version_info < (3, 0):
            pytest.xfail("Python 2 paths are visibly identical, but numerically different")
        raise
