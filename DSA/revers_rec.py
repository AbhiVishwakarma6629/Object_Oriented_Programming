def rev_rec(list, start, end):
    if start >= end:
        return 
    list[start], list[end] = list[end], list[start]
    return rev_rec(list, start+1, end-1)

list = [1,2,3,4,5]
rev_rec(list, 0, len(list)-1)
print(list)

