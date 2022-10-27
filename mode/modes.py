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


def mode(dataset):
    """
    returns the mode of a dataset
    """
    mode = None
    maxCount = 0
    for value in dataset:
        frequency = dataset.count(value)
        if frequency > maxCount:
            maxCount = frequency
            mode = value
    return mode


print("the mode is", mode([4, 4, 4, 4, 4, 4, 5, 6, 6, 7, 8, 6, 9, 10]), )


def modev2(dataset):
    modeSoFar = dataset[0]
    freqSoFar = freq(dataset, modeSoFar)
    for item in dataset[1:]:
        if freq(dataset, item) > freqSoFar:
            modeSoFar = item
            freqSoFar = freq(dataset, item)
    return modeSoFar


print("the mode is", mode([4, 6, 67, 8, 9, 9, 10, 11, 12]))
