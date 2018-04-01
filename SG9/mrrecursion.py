n = 5

def myfunc(n):
    if n == 0:
        return 0
    else:
        return myfunc(n-1) + 2
