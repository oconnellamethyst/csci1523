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

    #Times, 1 = Power Systems Journey, 2 = Sustainable Energy Systems,
    # 3, Signals and Sys Lect, 4 Signals and Sys Disc.,
    # 5 Microcont Lect, 6 Microcont Disc, 7 Microcont Lab, 8 Other
    if(keyValue==1): #Sunday
        print("Sun")
        codice = 8
    elif(keyValue==7): #Saturday
        print("Sat")
        codice = 8
    elif(keyValue==2): #Monday
        #10:10 - 11:00 sigs and sys lecture, start 30 min early so #10:10 to 11:30
        print("Mon")
        if((tm1 >= 9) and (tm1 <= 11)):
            codice = 3
        #13 to 15 Sust
        elif((tm1 >= 13) and (tm1 <= 15)):
            codice = 2
        else:
            codice = 8
    elif(keyValue==3): #Tuesday
        print("Tues")
        if((tm1 >= 9) and (tm1 <= 11)):
            codice = 5
        elif((tm1 >= 12) and (tm1 <= 14)):
            codice = 1
        elif((tm1 >= 15) and (tm1 <= 20)):
            codice = 7
        else:
            codice = 8
    elif(keyValue==4): #Wednesday
        #10:10 - 11:00 sigs and sys lecture, start 30 min early so #10:10 to 11:30
        print("Wed")
        if((tm1 >= 9) and (tm1 <= 11)):
            codice = 3
        elif(tm1==12):
            codice = 4
        elif((tm1 >= 13) and (tm1 <= 15)):
            codice = 2
        else:
            codice = 8
    elif(keyValue==5): #Thursday
        print("Thur")
        if((tm1 >= 9) and (tm1 <= 10)):
            codice = 5
        elif(tm1==11):
            codice = 6
        elif((tm1 >= 12) and (tm1 <= 17)):
            codice = 1
        else:
            codice = 8
    elif(keyValue==6): #Friday
        print("Fri")
        if((tm1 >= 9) and (tm1 <= 11)):
            codice = 3
        else:
            codice = 8  
    return codice

def mover():
    '''
    Moves things based on a code into a folder
    '''
    import os
    import shutil

    for filename in os.listdir('/home/amethyst/Documents/Audios'):
        if filename.endswith(".wav"): 
            code=dateinator(filename)


            #Times, 1 = Power Systems Journey, 2 = Sustainable Energy Systems,
            # 3, Signals and Sys Lect, 4 Signals and Sys Disc.,
            # 5 Microcont Lect, 6 Microcont Disc, 7 Microcont Lab, 8 Other
    
            if(code==1):
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/GCC3027/'+filename)
                pass
            elif(code==2):
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/EE2701/'+filename)
                pass
            elif(code==3):
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/EE3015/'+filename)
                pass
            elif(code==4):
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/EE3015D/'+filename)
                pass
            elif(code==5):
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/EE2361/'+filename)
                pass
            elif(code==6):
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/EE2361D/'+filename)
                pass
            elif(code==7):
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/EE2361L/'+filename)
                pass
            else:
                shutil.move('/home/amethyst/Documents/Audios/'+filename, '/home/amethyst/Documents/Audios/Misc/'+filename)
                pass
            
        else:
            pass

    
 
def main():
    mover()
    print('done')
    return

#main

main()
