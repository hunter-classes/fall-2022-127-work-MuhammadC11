def findLargest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


print("the smallest number is", findLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

number = 7


def freq(l, v):
    count = 0
    for i in l:  # for each item in the list
        if i == v:  # if the item is equal to the value
            count += 1  # add one to the count
    return count


print("the value", number, "appears", freq(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], number), "times")
