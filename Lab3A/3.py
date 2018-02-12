init = int(input("Give me the initial integer in the series "))
n = int(input("Give me the number of terms "))
n = n + init - 1
m = 0

while (n >= init):
    m = m + n**2
    n -= 1
print("The sum of the squares is", m)
