# Velocity Module
import math

"""
Function that computes the velocity of a freely falling object subject
to an acceleration due to gravity, a, from an initial height of x.

For the velocity function:
x - expressed in meters
a - expressed in meters/sec*sec


Example calculation:
Assume x = 100 meters, a = 9.8 meters/(sec^2)

The velocity on impact with ground would be:
v = 9.8 * sqrt(2.0*100/9.8)
v = 44.23 meters per sec
"""

def velocity(a,x):
    v = a * math.sqrt(2.0*x/a)
    return v
