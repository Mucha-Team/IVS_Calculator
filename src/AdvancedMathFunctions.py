def power(x):
    x = x ** 2
    return x

def factorial(x):
    y = x - 1
    while y > 1:
        x = x * y
        y -= 1
    return x