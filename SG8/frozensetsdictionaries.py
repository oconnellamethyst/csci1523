# Ah, using frozensets in dictionaries right?

additivecolors = {frozenset(['Red','Green']):'Yellow',\
                  frozenset(['Blue','Green']):'Cyan',\
                  frozenset(['Red','Blue']):'Magenta',}

colorinput = set()
while len(colorinput) != 2:
    color = input('Give me Red, Blue or Green ')
    if color == 'Red' or color == 'Blue' or color == 'Green':
        colorinput.add(color)
    else:
        pass

stuckcolorinput = frozenset(colorinput)

print("Mixing these colors produces", additivecolors[stuckcolorinput])
