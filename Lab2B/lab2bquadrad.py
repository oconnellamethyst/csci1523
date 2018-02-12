import math
A = float(input("This program solves the quadratic formula. In the equation Ax**2 + Bx + C What is A? "))
B = float(input("What is B? "))
C = float(input("What is C "))
answerone = (-B + math.sqrt(B**2 - (4*A*C)))/(2*A)
answertwo = (-B - math.sqrt(B**2 - (4*A*C)))/(2*A)
print("The answers are", answerone, " and", answertwo)
