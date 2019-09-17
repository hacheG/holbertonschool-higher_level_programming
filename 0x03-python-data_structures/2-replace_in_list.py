#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
   leng = len(my_list)

   for i in my_list:
        if idx < 0:
            return(my_list)
        elif idx > leng:
            return(my_list)
        elif i == my_list[idx]:
            my_list[idx] = element
            return(my_list)
