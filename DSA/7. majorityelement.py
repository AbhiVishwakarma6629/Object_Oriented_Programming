nums = [3,2,3]
d = {}
for i in nums:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
e = max(d)