# Question 2 Python function example

def Question1Function2(aaa, bbb, ccc):
    aaa[4] = -35
    bbb[1] = 0
    ccc = 'a new string to view'
    return sum(aaa), min(bbb), ccc

AAA = [4.5, 5, 6.9, 23.5, 45]
BBB = [98, 23, 45, 22, 44]
CCC = 'String for function 2'

aa, bb, cc = Question1Function2(AAA, BBB, CCC)

print(AAA,"-",BBB,"-",CCC,"-","aaa-bbb-ccc-",aa,"-",bb,"-",cc)
