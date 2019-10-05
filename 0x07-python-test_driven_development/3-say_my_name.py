#!/usr/bin/python3
"""
    Function that prints the name of a person
"""


def say_my_name(first_name, last_name=""):
	  """
    Args:
        first_name: string
        last_name: string
    Raises:
        TypeError:
                 * first_name must be a string
                 * last_name must be a string
    Returns:
        print the name and last name
    """
	msnErr1 = "first_name must be a string"
	msnErr2 = "last_name must be a string"

	if isinstance(first_name, str) is not True:
		raise TypeError(msnErr1)

	if isinstance(last_name, str) is not True:
		raise TypeError(msnErr2)

	else:
		print("My name is {} {}".format(first_name, last_name))
