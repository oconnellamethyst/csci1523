level = int(input("What is the level? "))
# Can't have working code without actually declaring the variables used

if level <= 1:
    print('Value is well within range')
    print('Recheck within one year')
elif level <= 2:
    # Keep all of the indents on the same line for readability
    print('Value is within range')
    print('Recheck within one month')
elif level <= 3:
    # Both of these need to be on the same level for the code to work
    print('Value is slighly high')
    print('Recheck within one week')
elif level <= 4:
    print('Value abnormally high')
    print('Shut down system immediately')
    # What do you want your code to do if it's input is none of these?
    # End with an else just in case
else:
    print('Error!')
