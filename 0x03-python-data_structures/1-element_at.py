#!/usr/bin/python3
def element_at(my_list, idx):
    leng = len(my_list)

    for i in my_list:
        if idx < 0:
            return(None)
        elif idx > leng - 1:
            return(None)
        elif i == my_list[idx]:
            return(my_list[idx])
