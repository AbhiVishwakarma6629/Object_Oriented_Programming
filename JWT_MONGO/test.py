def fact(n):
    if n<=0:
        return 1
    if n<=2:
        return 2
    return n * fact(n-1)

print(fact(6))
