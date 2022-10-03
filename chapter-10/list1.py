myList = [76, 92.3, 'hello', True, 4, 76]

# Your code here
# Append “apple” and 76 to the list.
myList.append("apple")
myList.append(76)
# Insert the value “cat” at position 3.
myList.insert(3, "cat")
# Insert the value 99 at the start of the list.
myList.insert(0, 99)
# Find the index of “hello”.
print(myList.index("hello"))
# Count the number of 76s in the list.
print(myList.count(76))
# Remove the first occurrence of 76 from the list.
myList.remove(76)
# Remove True from the list using pop and index.
myList.pop(myList.index(True))
print(myList)
