# Dictionaries and Sets Lab Question 2
# Set operations


# Mammals defined

M = { 'dog', 'mouse', 'cat', 'horse', 'shrew', 'donkey', \
      'cow', 'goat', 'sheep', 'racoon', 'bear', \
      'lion', 'monkey' }

# Reptiles defined

R = { 'snake', 'alligator', 'lizard', 'turtle', \
      'crocodile' }

# N1
A = 'dog' in M
print(A)
print("-")

# N2
B = 'lizard' in M
print(B)
print("-")

# N3
C = 'monkey' in R
print(R)
print("-")

# N4
D = 'platapus' in M or 'platapus' in R
print(D)
print("-")

# N5
E = len(R)
print(E)
print("-")

# N6
F = M & R
print(F)
print("-")

# N7
print(R)
print("-")

# N8
for animal in R:
    print(animal)
print("-")

# N9
A = M | R
print(A)
print("-")

# N10
G = M in A
print(G)
