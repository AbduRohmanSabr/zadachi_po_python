"""
функцию, которая будет принимать
 список чисел и возвращать сумму чисел,
 пропущенных в списке.
"""

def sum_missing_numbers(lst):
    return sum(range(min(lst), max(lst) + 1)) - sum(lst)


# def sum_missing_numbers(lst):
#     return sum(x for x in range(min(lst), max(lst)) if x not in lst )

sum_missing_numbers([19, 17, 16, 15, 10, 11, 12])