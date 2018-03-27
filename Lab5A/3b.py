# Question 3 Python function example

def Question1Function3(aaa=10.0, bbb=4.0, ccc='no string'):
    return aaa, bbb, ccc

AAA = 20.0
BBB = 8.0
CCC = 'a new string'

# first call
aa, bb, cc = Question1Function3(AAA, BBB, CCC)
print(AAA,"-",BBB,"-",CCC,"-","aaa-bbb-ccc-",aa,"-",bb,"-",cc)

# second call
aa, bb, cc = Question1Function3()
print(AAA,"-",BBB,"-",CCC,"-","aaa-bbb-ccc-",aa,"-",bb,"-",cc)

# third call
aa, bb, cc = Question1Function3(aaa=25, ccc='new string')
print(AAA,"-",BBB,"-",CCC,"-","aaa-bbb-ccc-",aa,"-",bb,"-",cc)
