from velocity import velocity
from kinetic import kinetic

# A person standing on a bridge that is 100 meters above a road drops a 2.5kilo object, what is velocity and ke?
a = 9.8
x = 100
m = 2.5
v = velocity(a,x)
k = kinetic(v,m)


print("Answer, a person standing on a bridge...:\n", "velocity:", v, "\n kinetic energy:", k)


# Bullet 1200 m/sec, how much weight to get same KE?

a = 1200
v = velocity(a,x)

m = k/(kinetic(v,m)/m)

print("Answer, a bullet would need to weigh", m, "kilograms to have the same KE")
