# Text File Reader
# Finds number of sentences, words, and letters in the Gettysburg Address file

try:
    gettysburg = open('gettysburg.txt','r')
    words = 0
    sentences = 0
    letters = 0
    for line in gettysburg:
        # words
        words = words + len(line.split())
        if len(line.split("-")) > 1:
            words = words + len(line.split("-")) - 1
        else:
            pass
        # letters and sentences
        for char in line:
            if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                letters += 1
            elif char in ".!?":
                sentences += 1
            else:
                pass
    print("In the text file gettysburg, there are",words,"words,",sentences,"sentences,and",letters,"letters.")
        
except:
    print("There's been an error!")
