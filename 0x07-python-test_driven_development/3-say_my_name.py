#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
	msnErr1 = "first_name must be a string"
	msnErr2 = "last_name must be a string"

	if isinstance(first_name, str) is not True:
		raise TypeError(msnErr1)

	if isinstance(last_name, str) is not True:
		raise TypeError(msnErr2)

	else:
		print("My name is {} {}".format(first_name, last_name))
