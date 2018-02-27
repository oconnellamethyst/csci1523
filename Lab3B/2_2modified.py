'''
Simple loop, if-elif-else
'''

A,B,C = 0,0,0

for N in range(11):
    if (N%2 == 0 and N%3 == 0):
        A += 1
        B += 1
    elif N%2 == 0:
        A += 1
    elif N%3 == 0:
        B += 1
    else:
        C += 1
    print("A =", A)
    print("B =", B)
    print("C =", C)
    print("N =", N)
