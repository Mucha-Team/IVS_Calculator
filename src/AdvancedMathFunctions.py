def power(x):
    x = x ** 2
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

def nroot_rec( minimum, maximum, prevMid, prec, expo, origNum):
	middle=(maximum+minimum)/2
	prec+=1

	if (prevMid == middle):
		return middle

	if (prec < 200):
		if middle**expo > origNum:
			maximum=middle
			return nroot_rec( minimum, maximum, middle, prec, expo, origNum)

		elif middle**expo < origNum:
			minimum=middle
			return nroot_rec( minimum, maximum, middle, prec, expo, origNum)
		elif middle**expo == origNum:
			return middle
	else:
		return middle

def nroot( num1, expo):
	if num1 < 0:
		return - 1 #error, cant do root of neg number in real numbers
	else:
		return nroot_rec( 0, num1, -1, 1, expo, num1)