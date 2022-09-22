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
    first = word[0]
    # I want to check if the first letter is a vowel and if so, just add "yay" to the end
    # I want to check if the first letter is a consonant and if so, move it from the start to the end and add "ay"
    if first in 'aeiuo':
        return word + "yay"

    else:
        return word[1:] + first + "ay"


print(piglatin("telashes are weird"))
