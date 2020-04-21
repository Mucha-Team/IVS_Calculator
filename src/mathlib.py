#   
#   Author: Krystof Vurm    xvurmk00
#   date: 10. 04. 2020
#	file mathlib.py
#	last edit: 20. 04. 2020
#   desc: basic math functions
#

##
# @file mathlib.py
#
# @brief mathematic library with basic arithmetic functions
# @details this library can be used for basic arithemtic functions
#

##
# function that sums up 2 numbers
# 
# @param num1 is the number that will be combined with num2
# @param num2 is the number that will be added to num1
# @return returns total amount of 2 values combined 
#
def add(num1, num2):
    return float(num1) + float(num2)

##
# function that decrease 2nd number from the 1st
# 
# @param num1 is the base number
# @param num2 is the number that will be substracted from the 1st number
# @return returns difference of 2 numbers 
#
def sub(num1, num2):
	return float(num1) - float(num2)

##
# function that multiplies 2 values
# 
# @param num1 number that is the multiplicand
# @param num2 number that is the multiplier
# @return returns product of 2 numbers
#
def mul(num1, num2):
    return float(num1) * float(num2)

##
# function that divides 1st number with the 2nd 
# 
# @param num1 number that is the divident
# @param num2 number that is the divisor
# @return returns product of 2 numbers
# @throws ZeroDivisionError when dividing by zero throw ZeroDivisionError
#
def div(num1, num2):
	if float(num2) == 0:
		raise ZeroDivisionError

	result = float(num1) / float(num2)
	return result

##
# function that changes sign of a number
# 
# @param num1 number that will be negated
# @return returns negation of number
#
def neg(num1):
	return -num1
	