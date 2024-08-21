"""
-> Methods which performs operation on external data
-> it can also perform operations on class data
-> no need to pass object or class reference
-> created using decorator '@staticmethod'
"""


class Bank:
    bank_name = "BOI"
    rate_of_interest = 12.25

    @staticmethod
    def simple_interest(principle, n):
        si = (principle * n * Bank.rate_of_interest) / 100
        print(si)


principle = float(input("Enter the princip le: "))
n = int(input("Enter the number: "))
Bank.simple_interest(principle, n)
