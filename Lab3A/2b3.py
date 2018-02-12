# basic control and relational operators

L = 20
if (L != 20) or (L % 10 == 0):
    L += 1
    if L % 2 == 0:
        L += 5
    else:
        L+= 7
        L -= 2
    if L % 5 > 2:
        L -= 4
        L += 3
L-= 8
print('L is', L)
