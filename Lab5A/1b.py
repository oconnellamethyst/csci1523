# Question 1 Python function example

def Question1Function(aaa, bbb, ccc):
    aaa = aaa * aaa
    bb = aaa * aaa
    ccc = 'String from function'

    return aaa, bb, ccc

AAA = 3.0
BBB = 34.0
CCC = 'String for question 1'

aa, bb, cc = Question1Function(AAA, BBB, CCC)

print(AAA,"-",BBB,"-",CCC,"-","aaa-bbb-ccc-",aa,"-",bb,"-",cc)
