# 5 - Factorial: Implement a function that calculates the factorial of a given number.
def factorial(num):
    """find factorial (the multiplication of all numbers under it) of any number"""
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact
 

num = 10
print("Factorial of",num,"is",
factorial(num))