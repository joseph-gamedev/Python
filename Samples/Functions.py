import math
import time

def Add(a,b):
    return a+b

def RectangleArea(l,b):
    return l*b

def IsOdd(x):
    """Return 'True" if 'x' is a odd number"""
    return x%2 != 0

def IsPrime(x):
    if x == 1:
        return False 

    divisor = math.floor(math.sqrt(x))
    for num in range(2,1+divisor):
        if x%num == 0:
            return False 
    return True



print(Add(3,4))
print("Rectangle area: "  + str(RectangleArea(4,3)))
print("IsOdd: " + str(IsOdd(2)))
print("IsPrime: " + str(IsPrime(73)))