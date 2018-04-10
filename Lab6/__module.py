from velocity import velocity
from kinetic import kinetic

# MAIN PROGRAM

# A person standing on a bridge that is 100 meters above a road drops a 2.5kilo object, what is velocity and ke?
aa = 9.8
xa = 100
ma = 2.5
va = velocity(aa,xa)
ka = kinetic(va,ma)


print("Answer, a person standing on a bridge...:\n", "velocity:", va, "\n kinetic energy:", ka)


# Bullet 1200 m/sec velocity, how much weight to get same KE?

vb = 1200
mb = (2*ka)/(vb**2)

print("Answer, a bullet would need to weigh", mb, "kilograms to have the same KE")
