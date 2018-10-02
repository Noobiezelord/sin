import sin
import math

assert(sin.sin1(0) == 0)
assert(abs(sin.sin1(math.pi/2) - 1) <= 1e-15)

# A FAIRE : continuer les tests (plus de valeurs, tester sin2, sin3, sin4 également)

print("OK")
