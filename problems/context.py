import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import euler.numbers.pell as pell
import euler.numbers.functions as f

from euler.algebra.poly import Poly

from euler.geom.point import Point
from euler.geom.line import Line
from euler.geom.ellipse import Ellipse
from euler.geom.triangle import Triangle

from euler.utils import Utils
import euler.poker as poker

import euler.algorithms.kruskal as kruskal