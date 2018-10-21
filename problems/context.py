import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import euler.numbers.pell as pell
import euler.numbers.functions as f

import euler.algebra.poly as poly

import euler.geom.point as point
import euler.geom.line as line
import euler.geom.ellipse as ellipse

import euler.utils as utils
import euler.poker as poker

from euler.algorithms import kruskal