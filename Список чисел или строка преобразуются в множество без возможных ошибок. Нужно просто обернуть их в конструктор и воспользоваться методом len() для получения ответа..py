def to_set(element):
    st = set(element)
    return st, len(st)

print(to_set('я обычная строка'))
print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))