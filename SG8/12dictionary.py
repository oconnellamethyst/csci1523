spanishdays = {'Sunday':'Domingo','Monday':'Lunes',\
               'Tuesday':'Martes','Wednesday':'Miercoles',\
               'Thursday':'Jueves','Friday':'Viernes','Saturday':'Sabado'}

print('Monday in Spanish is', spanishdays[Monday])

try:
    day = input('Enter the name of a day of the week in'\
                'English in the format "Monday":')
    print(day, 'in Spanish is', spanishdays[day])
except:
    print("Error!")
