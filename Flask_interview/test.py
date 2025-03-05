s = "Hello"
vowels = ['a', 'e', 'i', 'o', 'u']
s=list(s)
left=0
right=len(s)-1
while left < right:
    if s[left] in vowels and s[right] in vowels:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    elif s[left] in vowels and s[right] not in vowels:
        right -= 1
    else:
        left += 1
print("".join(s))

