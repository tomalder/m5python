from math import sqrt


def myfunc():
    a = 2
    b = 4
    print(a + b)



def myfunc2(a,b):
    sum = a**2 + b**2
    return sqrt(sum)



myfunc()
var = myfunc2(8,9)
print(var)
var = myfunc2(7,3)
print(var)
z = int(input())
y = int(input())
var = myfunc2(z,y)
print(var)
print(sqrt)

'''
the function myfunc, carrys out the process requested, but does not give back any results
by comparission the function myfunc2 gives us back the result and puts it into a varible called var
the 1st is called a procedure
the 2nd is called a function
'''