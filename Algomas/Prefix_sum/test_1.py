# Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].
# Example:
# Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3
# Output: 9

def calculate_sum(nums):
    prefix_sum = [0] * (len(nums)+1)
    for i in range(len(nums)):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]
    return prefix_sum

def range_prefix(prefix_sum, i, j):
    return prefix_sum[j+1] - prefix_sum[i]

nums = [1,2,3,4,5,6]
i, j = 1, 3
prefix_S = calculate_sum(nums)
print(range_prefix(prefix_S, i, j))

