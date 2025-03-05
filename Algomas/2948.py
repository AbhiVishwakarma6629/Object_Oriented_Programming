nums = [1,7,6,18,2,1]
limit = 3
sorted_nums = sorted(nums)

# 1 1 2 6 7 18
#     i
print(sorted_nums)
grouping_dict = {sorted_nums[0]:0}
count = 0
for i in range(1, len(nums)):
    if sorted_nums[i] - sorted_nums[i-1] > limit:
        count += 1
    grouping_dict[sorted_nums[i]] = count

# {1: 0, 2: 0, 6: 1, 7: 1, 18: 2}

group_elements_in_array = {}
for i in range(len(sorted_nums)):
    group_no = grouping_dict[sorted_nums[i]]
    if group_no in group_elements_in_array:
        group_elements_in_array[group_no].append(sorted_nums[i])
    else:
        group_elements_in_array[group_no] = [sorted_nums[i]]

# {0: [1, 1, 2], 1: [6, 7], 2: [18]}
#  [1,7,6,18,2,1]

for i in range(len(nums)):
    group_num = grouping_dict[nums[i]]
    smallest_num_group = group_elements_in_array[group_num]
    nums[i] = smallest_num_group[0]
    smallest_num_group.pop(0)
print(nums)


