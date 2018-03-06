# these snippets of code are to be used to fill in the blanks below:

# add items to a python list
A = []
A.append( 45 )
for n in range (4):
    A.append( 10*n-3 )

# insert items into a Python list
B = [ 10, 11, 12, 13 ]
B.insert( 2, 99 )
B.insert( 0, 88 )

# remove items from a Python list
C = [ 10, 20, 30, 40, 20 ]
C.remove( 40 )
C.remove( 20 )

# pop elements off of a list
D = [ 10, 20, 30, 40, 20 ]
E = D.pop( 2 )
F = D.pop()

# execute functions on a list object
Z = [ 10, 20, 30, 40, 20 ]
G = Z.index( 40 )
H = Z.count( 20 )

# sort the elements of an array using sort member function
I = [ 15, -7, 12, -4, 14 ]
I.sort()

print("A=",A)
print("B=",B)
print("C=",C)
print("D=",D)
print("E=",E)
print("F=",F)
print("G=",G)
print("H=",H)
print("I=",I)
