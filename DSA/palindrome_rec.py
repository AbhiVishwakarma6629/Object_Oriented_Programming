def pali_rec(str, i, j):
    if i > j:
        return True
    if str[i] != str[j]:
        return False
    return pali_rec(str, i+1, j-1)
str = "abcbad"
print(pali_rec(str, 0, len(str)-1))
