arr = [1, 3, 2, 5, 7, 2, 8, 10, 5]
k = 3

def max_avg(arr, k):
    if len(arr) < k:
        return False
    
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_avg(arr, k))