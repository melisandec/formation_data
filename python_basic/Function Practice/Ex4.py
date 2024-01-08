# 4 - Sum of List: Define a function that returns the sum of all numbers in a list.
def sum_of_list (list):
    somme = 0
    for numbers in list:
        somme += numbers
    return somme

print(sum_of_list([2,5,100,200]))

