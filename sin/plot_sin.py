#!/usr/bin/env python3

import sin
import numpy
import math
import matplotlib.pyplot
from plot_axis import setup_trigo_axis

xmax = 10
xmin = -10

x = numpy.linspace(xmin, xmax, num=1000)
ours1 = list(map(sin.sin1, x))
ours2 = list(map(sin.sin2, x))
lib = list(map(math.sin, x))
matplotlib.pyplot.ylim([-2, 2])
setup_trigo_axis(matplotlib.pyplot, matplotlib.pyplot.axes(), xmin, xmax)

matplotlib.pyplot.plot(x, ours1, label='sin1')
matplotlib.pyplot.plot(x, ours2, label='sin2')
matplotlib.pyplot.plot(x, lib, label='math.sin')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

