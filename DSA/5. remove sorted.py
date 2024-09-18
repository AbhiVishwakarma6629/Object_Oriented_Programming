nums = [3,2,2,3]
val = 3

def remove_val(nums):
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k+=1
    return k

print(remove_val(nums))
