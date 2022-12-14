def bondify(name):
    space_location = name.find(" ")
    last = name[space_location+1].upper() + name[space_location+2:]
    first = name[0].upper() + name[1:space_location]
    finalName = last + ", " + first + " " + last
    return finalName


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
    length = len(word)
    if first.isupper():
        lowerfirst = first.lower()
        if lowerfirst in 'aeiuo':
            if word[length - 1] in '!,.?':
                word = word[0:length - 1] + 'yay' + word[length - 1]
                return word
            # if tthe first letter is contained in "aeiuo" then add "yay" to the end
            return word[0:length] + 'yay'

        else:
            if word[length - 1] in '!,.?':
                word = word[1:length - 1] + \
                    lowerfirst + "ay" + word[length - 1]
                newword = word[0].upper() + word[1:]
                return newword
            else:
                word = word[1:length] + lowerfirst + "ay"
                newword = word[0].upper() + word[1:]
                return newword
