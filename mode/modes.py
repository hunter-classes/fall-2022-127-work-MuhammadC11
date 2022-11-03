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


def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive
    tally = [0] * 100
    for value in dataset:
        tally[value] += 1
    maxCount = 0
    modeSoFar = 0
    for i in range(100):
        if tally[i] > maxCount:
            maxCount = tally[i]
            modeSoFar = i
    return modeSoFar

    # make a list of 100 slots
    # and set them all to 0
    # this will store our tallies

    # 2. loop through the dataset
    # and increment the tally for each value in the dataset

    # 3. the index with the highest tally is the mode


print("the mode is", fastMode([4, 6, 67, 8, 9, 9, 10, 10, 10, 10, 10, 11, 12]))
