#   
#   Author: Krystof Vurm    xvurmk00
#   date: 10. 04. 2020
#   desc: basic math functions
#

# returns the sum of 2 numbers: num1+num2
def add(num1, num2):
    return float(num1) + float(num2)

# returns the difference of 2 numbers: num1-num2
def sub(num1, num2):
	return float(num1) - float(num2)

# returns a multiple of 2 numbers: num1*num2
def mul(num1, num2):
    return float(num1) * float(num2)

# 1st value is the divident
# 2nd value is the divisor
# returns num1/num2
def div(num1, num2):
	if float(num2) == 0:
		raise ZeroDivisionError

	result = float(num1) / float(num2)
	return result

# returns negation of a number: -(num1)
def neg(num1):
	return -num1
	