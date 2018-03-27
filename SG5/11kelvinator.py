# Temperature Conversion (Kelvin-Fahernheit / Fahrenheit-Kelvin)
def displayWelcome():
    print('This program will covert a range of temperatures')
    print('Enter (F) to convert Fahrenheit to Kelvin')
    print('Enter (K) to convert Kelvin to Fahrenheit\n')

def getConvertTo():
    which = input('Enter selection: ')
    while which != 'F' and which != 'K':
        which = input('Enter selection: ')
    return which

def tempToKelvinFromFahren(start, end):
    print('\n Degrees', ' Degrees')
    print('Fahrenheit', 'Kelvin')

    for temp in range (start, end + 1):
        converted_temp = (temp - 32.0) * 5.0/9.0 + 273.154
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))

def tempToFahrenFromKelvin(start, end):
    print('\n Degrees', ' Degrees')
    print(' Kelvin', 'Fahrenheit')

    for temp in range (start, end + 1):
        converted_temp = 1.8 * (temp - 273.15) + 32.0
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))

# ---- main

# Display program welcome

displayWelcome()

# Get which conversion from user
which = getConvertTo()

# Get range of temperatures to convert
temp_start = int(input('Enter starting temperature to convert: '))
temp_end = int(input('Enter ending temperature to convert: '))
# Display range of converted temperatures
if which == 'F':
    tempToKelvinFromFahren(temp_start, temp_end)
else:
    tempToFahrenFromKelvin(temp_start, temp_end)

    
