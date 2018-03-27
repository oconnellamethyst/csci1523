def ie(p, i=0.06, pr=1000.0):
    return (1 + i)**p*pr

print(ie(1)) # Part A
print(ie(5, .1)) # Part B
print(ie(5, .1, 2000)) # Part C
print(ie(5, pr=3000, i=0.1)) # Part D
# print(ie(pr=3000, i=0.1, 5)) # Part E
print(ie(p=5, pr=3000, i=0.1)) # Part F
