def poundsToMetric(pounds):
    # whole number division of a fraction instead of multiplication to keep this number whole
    fraction = 1/0.455
    kilograms = int(pounds // fraction)
    # same with my use of the modulus
    print(pounds % fraction)
    grams = (pounds % fraction) * 455

    print(kilograms, "kilograms, and", grams, "grams")
    return(kilograms, grams)

poundsToMetric(float(input("How many pounds? ")))
