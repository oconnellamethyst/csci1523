value = float(input("How much does your house cost? (No dollar signs or commas) "))
income = float(input("What is your combined income? (No dollar signs or commas) "))
residence = str(input("Have you owned a primary residence in the last three years? (y/n) "))

if (value < 800000 and income < 225000 and residence == 'n'):
    print("You qualify for the First-Time Home Buyer Tax Credit")
else:
    print("You do not qualify for the First-Time Home Buyer Tax Credit")
