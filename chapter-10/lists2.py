def average(numlist):
    sumNum = 0
    for num in numlist:
        sumNum += num
    return sumNum / len(numlist)


print(average([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))


def sum_of_squares(xs):
    # your code here
    sumNum = 0
    for num in xs:
        sumNum += num * num
    return sumNum


print(sum_of_squares([2, 3, 4]))
