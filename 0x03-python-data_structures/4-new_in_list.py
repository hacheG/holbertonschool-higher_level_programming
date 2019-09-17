#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    leng = len(cpy_list)

    for i in cpy_list:
        if idx < 0:
            return(cpy_list)
        elif idx > leng - 1:
            return(cpy_list)
        elif i == cpy_list[idx]:
            cpy_list[idx] = element
            return(cpy_list)
