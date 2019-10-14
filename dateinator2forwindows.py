def datetoday(day, month, year):
# 22-01-04
#
# Date Utils
# By Fuzzyman see www.voidspace.org.uk/atlantibots/pythonutils.html

    d = day
    m = month
    y = year
    if m < 3:
        z = y-1
    else:
        z = y
    dayofweek = ( 23*m//9 + d + 4 + y + z//4 - z//100 + z//400 )
    if m >= 3:
        dayofweek -= 2
    dayofweek = (dayofweek%7)+1
    return dayofweek


def dateinator(title):
    '''
    Function that takes in a title and returns an integer representing a class sort

    Takes in title in the form of 'Audio recording 2019-02-19 13-07-45.wav'
    '''
    #15 end of Audio recording, 18+19, year, 21+22, month, 24+25 date, 27+28 tm1, 30+31 tm2
    year=int(title[18]+title[19])
    month=int(title[21]+title[22])
    date=int(title[24]+title[25])
    tm1=int(title[27]+title[28])
    tm2=int(title[30]+title[31])

    #Key value method

    #keyValue=date + (2.6*month -0.2) - 40 + (2000+year) + ((2000+year)/4) + (20/4)

    keyValue=datetoday(date,month,2000+year)
        
    print(keyValue)

    #Times, 1 = Sigs n Sys Lecture, 2 = Sigs n Sys Discussion,
    # 3, Analog Lecture, 4 Analog Discussion,
    # 5 Wind Energy Ess, 6 Junior Lab 1, 7 Junior Lab 1 Makeup, 8 Other
    if(keyValue==1): #Sunday
        print("Sun")
        codice = 8
        print("Rand")
    elif(keyValue==7): #Saturday
        print("Sat")
        codice = 8
        print("Rand")
    elif((keyValue==2) or (keyValue==4) or (keyValue==6)): #Monday or Wednesday or Friday
        #9:05-9:55 analog
        print("MWF")
        if((tm1 >= 8) and (tm1 <= 9)):
            codice = 3
            print("Analog")
        #10:05-10:55 sigs n sys
        elif((tm1 >= 10) and (tm1 <= 11)):
            codice = 1
            print("Sigs n Sys")
        #discussion, analog, sigs n sys
        elif((tm1 >= 13) and (tm1 <= 14)):
            if(keyValue==4):
                codice = 4
                print("Analog")
            elif(keyValue==6):
                codice = 2
                print("Sigs n Sys")
            else:
                codice = 8
                print("Rand")
        else:
            codice = 8
    elif((keyValue==3) or (keyValue==5)): #Tuesday or Thursday
        print("TTh")
        #lab makeup
        if((tm1 >= 8) and (tm1 <= 8)):
            if(keyValue==5):
                codice = 7
            else:
                codice = 8
        #wind ess
        elif((tm1 >= 9) and (tm1 <= 10)):
            codice = 5
        elif((tm1 >= 11) and (tm1 <= 14)):
            if(keyValue==3):
                codice = 6
            else:
                codice = 8
        else:
            codice = 8
    return codice

def mover():
    '''
    Moves things based on a code into a folder
    '''
    import os
    import shutil

    for filename in os.listdir('C:\\Users\\fort3\\Documents\\Audios\\'):
        if filename.endswith(".wav"): 
            code=dateinator(filename)


            #Times, 1 = Sigs n Sys Lecture, 2 = Sigs n Sys Discussion,
            # 3, Analog Lecture, 4 Analog Discussion,
            # 5 Wind Energy Ess, 6 Junior Lab 1, 7 Junior Lab 1 Makeup, 8 Other
    
            if(code==1):
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\EE3015L\\'+filename)
                pass
            elif(code==2):
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\EE3015D\\'+filename)
                pass
            elif(code==3):
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\EE3115L\\'+filename)
                pass
            elif(code==4):
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\EE3115D\\'+filename)
                pass
            elif(code==5):
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\EE5745\\'+filename)
                pass
            elif(code==6):
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\EE3101L\\'+filename)
                pass
            elif(code==7):
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\EE3101D\\'+filename)
                pass
            else:
                shutil.move('C:\\Users\\fort3\\Documents\\Audios\\'+filename, 'C:\\Users\\fort3\\Documents\\Audios\\RAND\\'+filename)
                pass
            
        else:
            pass

    
 
def main():
    mover()
    print('done')
    return

#main

main()
