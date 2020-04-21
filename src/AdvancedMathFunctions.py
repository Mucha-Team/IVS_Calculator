def power(x, n):
    x = x ** n
    return x

def factorial(x):
	if x <= 0:
		return - 1 #error, cant do factorial of neg numbers in real numbers
	else:
		y = x - 1
		while y > 1:
			x = x * y
			y -= 1
		return x

def root( x, n):
	if nu < 0:
		return - 1 #error, cant do root of neg number in real numbers
	else:
		x = x ** (1 / n)
		return x