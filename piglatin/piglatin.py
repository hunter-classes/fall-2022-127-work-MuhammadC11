def bondify(name):
    space_location = name.find(" ")
    last = name[space_location+1].upper() + name[space_location+2:]
    first = name[0].upper() + name[1:space_location]
    finalName = last + ", " + first + " " + last
    return finalName


print(bondify("Muhammad Chaudhry"))


"""
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words

"""


def piglatin(word):
    low = word.lower()

    if low[0] == "a" or low[0] == "e" or low[0] == "i" or low[0] == "u" or low[0] == "y":
        return low + "yay"

    else:
        first_letter = low[0]
        return low[1:] + first_letter + "ay"


print(piglatin("ello bruv"))
