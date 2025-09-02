#!/usr/bin/python3
"""
	Function: factorial

	Description:
		Recursively computes the factorial of a non-negative integer.
		The factorial of a number n (written as n!) is the product of all
		positive integers less than or equal to n.
		example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
	Parameters:
		n (int): A non-negative integer whose factorial is to be calculated.
	Returns:
		int: The factorial of the given number n.
"""
import sys

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
