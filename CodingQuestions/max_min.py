lst = [('IV', 4), ('II', 2), ('I', 1), ('III', 3), ('V', 5), ('VI', 6)]

min_tup = min(lst, key=lambda x:x[1])
max_tup = max(lst, key=lambda x:x[1])

print(min_tup)
print(max_tup)