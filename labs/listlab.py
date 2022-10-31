
def smallest(lst):
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest


print("this function returns the smallest number in a list")
print("the smallest number in the list is:", smallest(
    [10000, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
print("----------------------------------------------")


# Write a function that returns a new list that contains all the odd items in the original list
def onlyOdd(lst):
    odd = []
    for i in lst:
        if i % 2 == 1:
            odd.append(i)
    return odd


print("the onlyOdd function returns only the odd numbers from a list")
print('the only odd numbers in this list are:',
      onlyOdd([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print("----------------------------------------------")
# Write a function that takes a string and returns a new string where all the words are capitalized.


def capitalizeAll(sent):
    newStr = ""
    newStr = sent.upper()
    return newStr


print("the capitalizeAll function takes a string and converts all characters to uppercase")
print(capitalizeAll("hello how are you doing today!"))
print("----------------------------------------------")


# Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case.


def upperFive(sent):
    splitSent = sent.split()
    newSent = []
    for i in splitSent:
        if len(i) <= 5:
            newSent.append(i)
        else:
            newSent.append(i.upper())
    jointSent = " ".join(newSent)
    return jointSent


print("the upperFive function takes a string and converts all words longer than 5 characters to uppercase")
print(upperFive("Hey Michaelangelo how are you and your wonderful family doing on this lovely and enticing thursday afternoon."))
print("----------------------------------------------")

# Write a function that takes a list of numbers and returns a new list with each item squared


def squareList(numb):
    squared = []
    for i in numb:
        squared.append(i**2)
    return squared


print("the squareList function takes a list of numbers and squares each number")
print("the input numbers are 1,2,3,4,5,6,7,8,9,10. Those numbers squared are:",
      squareList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("----------------------------------------------")


# Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
def sumofTwo(numb1, numb2):
    sumList = []
    index = 0
    for i in numb1 and numb2:
        sumList.append(numb1[index] + numb2[index])
        index += 1
    return sumList


print("the sumofTwo function takes two lists of numbers and adds them together")
print("the sum of the two lists are:", sumofTwo([1, 2, 3], [25, 30, 35]))
print("----------------------------------------------")

# number 10: Count how many words in a list have length 5.


def countWords(lst):
    numlen5 = 0
    for i in lst:
        if len(i) == 5:
            numlen5 += 1
    return numlen5


print("There are", countWords(
    ["words", "valid", "number", "where", "how"]), "words with 5 characters in them")
print("----------------------------------------------")

# Sum all the elements in a list up to but not including the first even number.


def sumUntilEven(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            break  # stop the loop
        else:
            sum += i
    return sum


print("the sum of the list up to the first even number is:",
      sumUntilEven([3, 5, 7, 9, 11, 13, 15, 17, 18]))
print("----------------------------------------------")
