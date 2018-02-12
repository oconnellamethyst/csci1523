AAA = "A"
BBB = "B"
CCC = 1
DDD = 11
EEE = 13
FFF = 5
GGG = 4.5
HHH = 1.8e-40
A = 'A' <= BBB <= 'Z'
B = GGG < HHH or EEE < FFF
C = not AAA >= BBB
D = not AAA < BBB or HHH > 0.0
E = DDD >= GGG or GGG >= 10
G = DDD == 10 or 11

print("A is", A)
print("B is", B)
print("C is", C)
print("D is", D)
print("E is", E)
print("G is", G)
