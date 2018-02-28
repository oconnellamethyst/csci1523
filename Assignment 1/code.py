# Amethyst O'Connell
# CSCI 1523
# Mary Anderson

# citation: https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
from random import randint
from math import sqrt

go = 0
cont = 1

number = "null"
numerator = 0
denominator = 0

incrementer = 1
average = 0

x = "null"
y = "null"
d = "null"

while (go <= 0):
    go2 = 0
    go3 = 0

    print("Welcome to Part 1, Numbers will now be generated")
    for z in range(20):
      print (randint(1,101))


    cont = input("Would you like to continue? Y/N ")
    if cont == "N":
        go += 1
        go2 += 1
        go3 += 1
        print("Terminating program...")
    else:
        print("Continuing to Part 2")
        print(" ")
    
    while (go2 <= 0):
        for a in range(500):
            number = randint(1,65537)
            if (number >= 512 and number <= 2048):
                numerator += 1
                denominator += 1
            else:
                denominator += 1
        print("The fraction of numbers generated that is between 512 and 2048 is: ", numerator, "/", denominator)

        cont = input("Would you like to continue? Y/N ")
        if cont == "N":
            go += 1
            go2 += 1
            go3 += 1
            print("Terminating program...")
        else:
            print("Continuing to Part 3")
            print(" ")

        while (go3 <= 0):
                
            while incrementer < 1000:
                x = randint(1,10001)
                y = randint(1,10001)
                d = sqrt(x**2 + y**2)
                average = average + d
                incrementer += 1
        
            average = average / 1000
            print("The average distance from the origin is ", average)
    
            cont = input("Would you like to continue? Y/N ")
            if cont == "N":
                go += 1
                go2 += 1
                go3 += 1
                print("Terminating program...")
            else:
                go2 += 1
                go3 += 1
                print("Continuing to the start")
                print(" ")
