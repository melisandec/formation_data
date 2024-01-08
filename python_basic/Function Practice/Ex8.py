# 8 - Prime Checker: Write a function that determines if a number is prime.
def prime_check(num):
    if num <= 1:
        return False
    # Loop through all numbers from 2 to the square root of num (rounded down to the nearest integer) 
    # then if num is divisible by any of these numbers, return False:
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


# Test the function with n = 11
print(prime_check(11))