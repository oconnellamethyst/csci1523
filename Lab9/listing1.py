# Python implementation of a recursive solution to the
# problem of determining the factorial of a number, n

def factorial(n):
    print('Factorial Call!')
    if (n == 0 or n ==0): # Why is that there?
        print('This is the base case!')
        return 1; # and that
    else:
        ('This is the general case!, now running with input": ',n)
        return n * factorial(n - 1)

def main():
    print('Hey look, initialization!')
    n = eval(input("Number to find factorial: ")) # What does the eval function do?
    print("The value of n input: ",n)
    n_fac = factorial(n)
    print("The factorial of n: ", n_fac)

main()

