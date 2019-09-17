#!/usr/bin/python3

def new_in_list(my_list, idx, element):
   cpy_list = my_list
   leng = len(cpy_list)
   
   for i in cpy_list:
      if idx < 0:
         return(cpy_list)
      elif idx > leng:
         return(cpy_list)
      elif i == cpy_list[idx]:
         cpy_list[idx] = element
         return(my_list)
