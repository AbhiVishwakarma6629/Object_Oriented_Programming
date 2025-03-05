lst = [1, 2, 3, 4, 1, 2, 3, 4]

d = {}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
ans_lst =[]
for k,v in d.items():
    ans_lst.append([k]*v)

print(ans_lst)
