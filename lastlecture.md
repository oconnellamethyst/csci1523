# Lecture on Recursive functions from Mary Anderson

## Factorial is used as an example, but it is more efficient as a loop


This can be found on Page 466

```
def factorial(n):
	print(n)
	if n==0:
		return 1
	return n * factorial(n-1)
```

is better as

```
def ifactorial(n)
	result = 1
	if n==0:
		return result
	for k in range(n, 0, -1):
		result = result * k
	return result
```
## Pros
Recursive functions make the code look elegant
Complex tasks can be broken down
Sequence generation can be easier

## Cons
Recursive functions are hard to debug, inefficient, take up memory and time, and are challenging to think through

## Selection Sort program

Number 12 selection sort program

Smallest and put it at the end

```
def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax

...
```
[Interactive Python, the Selection Sort](interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html)

## Binary Sort program

```
def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)//2 #truncating
		if alist[midpoint]==item:
			print(item)
			return True
		else:
			if item<alist[midpoint]:
				return binarySearch(alist[:midpoint],item)
			else:
				return binarySearch(alist[:midpoint+1:],item)
# main

testlist = [0,1,2,3,4,5,5]
print(binarySearch(testlist, 3))
```

## Number 16 in the book

```
def myfunc(n):
	print(n)
	if n==0:
		return 0
	else:
		return myfunc(n-1) + 2

# main

myfunc(8)
```

## Number 17 in the book
def reverseString(s):
	if len(s) > 1:
		reverseString(s[1: ])
	print(s[0], end=''
```

## Let's look at the lab, page 2
