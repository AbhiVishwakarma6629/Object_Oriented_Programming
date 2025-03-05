def all_digits_even(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

even_num = []

for num in range(6000, 9000):
    if num%2==0 and all_digits_even(num):
        even_num.append(num)
    
print(even_num)