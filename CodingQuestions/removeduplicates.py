s = "MISSISSIPI"
print(list(s))

k=1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        s[k] = s[i]
        k += 1
print(s)