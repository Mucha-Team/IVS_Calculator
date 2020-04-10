#   
#   Author: Krystof Vurm    xvurmk00
#   date: 10. 04. 2020
#   desc: basic math functions
#

def add(num1, num2):
    return float(num1) + float(num2)

def sub(num1, num2):
    return float(num1) - float(num2)

def mul(num1, num2):
    return float(num1) * float(num2)

def div(num1, num2):

	if float(num2) == 0:
		raise ZeroDivisionError

	result = float(num1) / float(num2)
	return result
	