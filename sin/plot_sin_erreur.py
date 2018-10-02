#!/usr/bin/env python3

import sin
import numpy
import math
import matplotlib.pyplot as plt
from plot_axis import setup_trigo_axis

def sin1_erreur(n):
    return abs(sin.sin1(n) - math.sin(n))

def sin2_erreur(n):
    return abs(sin.sin2(n) - math.sin(n))

def sin3_erreur(n):
    return abs(sin.sin3(n) - math.sin(n))

def sin4_erreur(n):
    return abs(sin.sin4(n) - math.sin(n))

xmin = -20
xmax = 20
ymax = 2

x = numpy.linspace(xmin, xmax, num=1000)
ours1 = list(map(sin1_erreur, x))
ours2 = list(map(sin2_erreur, x))
ours3 = list(map(sin3_erreur, x))
ours4 = list(map(sin4_erreur, x))

fig, ax = plt.subplots(nrows=2, ncols=1)
log = plt.subplot(211)
plt.ylim([1e-30, ymax])
setup_trigo_axis(plt, log, xmin, xmax)

log.spines['bottom'].set_position(('axes', 0))
log.set_yscale('log')

#plt.plot(x, ours1, label='erreur sin1 (log)')
#plt.plot(x, ours2, label='erreur sin2 (log)')
#plt.plot(x, ours3, label='erreur sin3 (log)') # décommenter pour tracer cette courbe
plt.plot(x, ours4, label='erreur sin4 (log)') # décommenter pour tracer cette courbe
plt.legend()

lin = plt.subplot(212)
setup_trigo_axis(plt, lin, xmin, xmax)

#plt.plot(x, ours1, label='erreur sin1 (linéaire)')
#plt.plot(x, ours2, label='erreur sin2 (linéaire)')
#plt.plot(x, ours3, label='erreur sin3 (linéaire)') # décommenter pour tracer cette courbe
plt.plot(x, ours4, label='erreur sin4 (linéaire)') # décommenter pour tracer cette courbe
plt.legend()

plt.show()
