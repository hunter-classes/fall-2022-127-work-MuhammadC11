# Extras are as follows:

# Store your translations in a file named pirate.dat the file should have lines in the form “word:translation.”

# Handle upper and lower case and/or punctuation


tdata = open("pirate.dat").read()
idata = open("input.txt").read()
translations = tdata.split('\n')
input = idata.lower().split()
dictionary = {}

# create a dictionary from pirate.dat
for line in translations:
    (english, pirate) = line.split(':')
    dictionary[english] = pirate

del_punct = []
for word in input:
    if ',' in word or '.' in word or '!' in word:
        del_punct.append(word[0:-1])
    else:
        del_punct.append(word)


# translate the input
index = 0
updatedStory = []
for word in del_punct:
    if word in dictionary.keys():
        updatedStory.append(dictionary[word])
    else:
        updatedStory.append(word)
    updatedStory[0] = updatedStory[0].capitalize()
    if "," in input[index]:
        updatedStory[index] += ","
    elif "." in input[index]:
        updatedStory[index] += "."
    elif "!" in input[index]:
        updatedStory[index] += "!"
    if updatedStory[index] == "i":
        updatedStory[index] = "I"
    elif "." in updatedStory[index - 1]:
        updatedStory[index] = updatedStory[index].capitalize()
    elif "?" in updatedStory[index - 1]:
        updatedStory[index] = updatedStory[index].capitalize()
    elif "!" in updatedStory[index - 1]:
        updatedStory[index] = updatedStory[index].capitalize()
    index = index + 1
finalStory = " ".join(updatedStory)
print(finalStory)
