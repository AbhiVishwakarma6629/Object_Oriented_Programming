nums = [2,7,9,11]
target = 9
dict = {}
for i, v in enumerate(nums):
    comp = target - v
    if comp in dict:
        print([dict[comp], i])
    else:
        dict[v] = i
