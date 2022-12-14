# Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value.

def max(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max


print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Write a function to count how many odd numbers are in a list.
def odd(lst):
    count = 0
    for i in lst:
        if i % 2 == 1:
            count = count + 1
    return count


print(odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Sum up all the even numbers in a list.


def even(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum = sum + i
    return sum


print(even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
