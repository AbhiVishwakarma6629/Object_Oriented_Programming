class Search:
    def binary_search(self, lst, target):
        left = 0
        right = len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] < target:
                left = mid + 1
            elif lst[mid] > target:
                right = mid - 1
            else:
                return f"Taget found at index -> {mid}"
        return -1

    def linear_search(self, lst, target):
        for i in range(len(lst) - 1):
            if lst[i] == target:
                return f"Target found at index -> {i}"
        return -1


obj = Search()
search = input("Enter the search(Binary\Linear): ")
if search.lower() == "linear":
    lst = list(map(int, input("Enter the number with spaces and without pressing enter: ").split()))
    target = int(input("Enter the target: "))
    print(obj.linear_search(lst, target))
elif search.lower() == "binary":
    lst = list(map(int, input("Enter the number with spaces and without pressing enter: ").split()))
    target = int(input("Enter the target: "))
    print(obj.binary_search(lst, target))
else:
    print("Enter the correst input............!")
