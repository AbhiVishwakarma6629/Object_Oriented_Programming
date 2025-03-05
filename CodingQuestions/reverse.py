n = 12345
while n != 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n//=10
print(reverse_num)