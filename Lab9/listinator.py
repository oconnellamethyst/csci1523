#1
def listinator(runninglist,incrementor,letters):
    '''
    Function that reverses letters recursively and also prints them individually to the terminal because I cannot read apparently, this is much easier with for loops :(

#5
    runninglist is a running list of letters, incrementor is an incrementor, letters is a list of letters
    '''
    runninglist.insert(0, letters[incrementor])
    print(letters[incrementor])
#10
    try:
        if incrementor > len(letters):
            return(runninglist)
        else:
#15
            incrementor += 1
            listinator(runninglist,incrementor,letters)
    except:
        return(runninglist)
#20

def main():
    print("Let's reverse a word!")
    word = input("What is the word? ")
#25
    letters = list(word)
    runninglist = []
    incrementor = 0
    listinator(runninglist,incrementor,letters)
#30
    print("And here is the reverse:", "".join(runninglist))
    return

#main
#35

main()

    
