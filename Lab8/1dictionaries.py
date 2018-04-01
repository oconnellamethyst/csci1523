# Dictionaries and Sets Lab Question 1

M = { 100:'Vikings', 200:'Bears', 300:'Packers', \
      400:'Lions', 500:'Browns', 600:'Steelers', \
      700:'Patriots', 800:'Cowboys' }

# N1
A = 100 in M
print(A)
print("-")

# N2
B = 'Browns' in M
print(B)
print("-")

# N3
M[300] = 'Chargers'
print(M[300])
print("-")

# N4
M[700] = 'Colts'
print(M[700])
print("-")

# N5
print(M.keys())
print("-")

# N6
print(M.values())
print("-")

# N7
for key in M.keys():
    print(key)
print("-")

# N8
for value in M.values():
    print(value)
print("-")

# N9
for key, value in M.items():
    print(key, value)
print("-")

# N10
for X in M:
    print(X)
