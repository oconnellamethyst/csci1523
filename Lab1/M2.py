print('Welcome to the SETI program')
print('This program will allow you to enter specific values related to')
print('the likelihood of finding intelligent life in our galaxy. All')
print('percentages should be written as integers, e.g., 40 and not .40')
print()
R = 7
p = 100
n = int(input('How many planets per star do you think can support life: '))
f = 100
i = 100
c = 100
L = int(input('Number of years you think civilizations last?: '))
num_detectable_civilizations = R * (p/100) * n * (f/100) * (i/100) * (c/100) * L
print()
print('Based on the values entered ...')
print('there are an estimated', round(num_detectable_civilizations), 'potentially detectable civilizations in our galaxy')
