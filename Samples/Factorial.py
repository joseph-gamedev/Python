def factorial(n):
    """Returns n!"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))
print(factorial(2))
print(factorial(5))