# 6 - Fibonacci Sequence: Write a function to return the nth element of the Fibonacci sequence.
def Fibonacci_sequence(n):
    """Fibanacci is sequence in which each number is the sum of the two preceding ones.
    We will find the nth element with this function"""
    if n <= 0:
        print("incorect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else: 
        return Fibonacci_sequence(n-1)+Fibonacci_sequence(n-2)

# Driver Program
 
print(Fibonacci_sequence(3))