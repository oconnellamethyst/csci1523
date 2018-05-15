def compare():
    '''
    Program that compares the user input of an integer to zero
    If the input is equal to zero, it returns True
    If not, it returns False
    '''
    output = False
    try:
        inty = int(input("Give me an integer! If it is zero, the output is True! "))
        if inty == 0:
            output = True
        else:
            pass
    except:
        print("Not an integer! ")
    return output

#main
print("The output is", compare())
