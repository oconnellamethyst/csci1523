# Kinetic Energy Module
"""
Function that computes the kinetic energy of mass, m, at a velocity, v.

For the kinetic energy function:
m - expressed as kilograms
v - expressed as meters per sec

Example calculation:
Assume a mass of 1 kilogram and a velocity of 100 meters per second.

ke = 0.5 * 1 * v ** 2
ke = 5000 kilogram-meters^2/sec^2
"""

def kinetic(v,m):
    ke = 0.5*m*v**2
    return ke
