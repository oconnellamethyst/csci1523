def coinchange(integer):
    '''
    Gives the change in (quarters, dimes, nickels, pennies) for a number (integer)
    between 1 and 99
    '''
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while(integer >= 25):
        if(integer >= 25):
            integer -= 25
            quarters += 1
        else:
            pass
    while(integer >= 10):
        if(integer >= 10):
            integer -= 10
            dimes += 1
        else:
            pass
    while(integer>= 5):
        if(integer >= 5):
            integer -= 5
            nickels += 1
        else:
            pass
    pennies = integer
    return(quarters, dimes, nickels, pennies)

def main():
    '''
    Main of the program
    '''

    integer = int(input("What do you need change for? Enter an integer between 1 and 99: "))
    while integer < 1 or integer > 99:
        integer = int(input("Please enter an integer between 1 and 99 "))
    coins = coinchange(integer)
    print("Your change is:", coins[0], "quarters,", coins[1], "dimes,", coins[2], "nickels, and", coins[3], "pennies.")

#main

main()
        
        
