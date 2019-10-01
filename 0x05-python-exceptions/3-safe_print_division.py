#!/usr/bin/python3
def safe_print_division(a, b):
	divRes = None
	try:
		divRes = a /b
	except ZeroDivisionError:
		return None
	finally:
		print("{} {}".format("Inside result:", divRes))
	return divRes