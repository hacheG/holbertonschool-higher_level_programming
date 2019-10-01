#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = a_dictionary.copy()
    for i in new_a_dictionary:
        new_a_dictionary[i] = new_a_dictionary[i]*2
    return new_a_dictionary
