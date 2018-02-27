evencount = 0
evensum = 0
oddcount = 0
oddsum = 0
integer = "null"
while integer != 0:
    integer = int(input("What is an integer? "))
    if integer < 0:
        print("Yo, no negative numbers!")
    elif integer == 0:
        print(" ")
    elif integer % 2 == 0:
        evencount += 1
        evensum = integer + evensum
    else:
        oddcount += 1
        oddsum = integer + oddsum
print("The number of even integers is", evencount)
print("The number of odd integers is", oddcount)
print("The sum of even integers is", evensum)
print("The sum of odd integers is", oddsum)
print("The total integers is", oddcount + evencount)
