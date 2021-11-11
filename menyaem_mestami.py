"""
Created on Thu Nov 11 18:38:33 2021

@author: Lenovo
"""
# def change(lst):
#     new_start = lst.pop()
#     new_end = lst.pop(0)
#     lst.append(new_end)
#     lst.insert(0,new_start)
#     return lst

# print(change([1,2,3]))

def change(lst):
    lst [0], lst [-1] = lst[-1], lst[0]
    return lst
print(change([1,2,3,9]))