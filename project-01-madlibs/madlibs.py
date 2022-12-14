# I did the import file extra which is evident when i use open("").
# I did the constnant character extra: character = random.choice(character)
#story = story.replace("<character>", character)
# I did the extra to fix capitalization: if i.find(".") != -1:
#nextWord = storyData[storyData.index(i) + 1]
# storyData[storyData.index(
# i) + 1] = nextWord.capitalize()


import random
f = open("story.dat", "r")
n = open("nouns.dat", "r")
v = open("verbs.dat", "r")
a = open("adjectives.dat", "r")
c = open("characters.dat", "r")
storyData = f.read()  # read the entire file into a string
nounData = n.read()  # read the entire file into a string
adjectiveData = a.read()  # read the entire file into a string
verbData = v.read()  # read the entire file into a string
characterData = c.read()
# shoutout to Thomas H. for showing me I needed to split the data into a list of strings
nounList = nounData.split()
# shoutout to Thomas H. for showing me I needed to split the data into a list of strings
verbList = verbData.split()
# shoutout to Thomas H. for showing me I needed to split the data into a list of strings
adjectiveList = adjectiveData.split()
characterList = characterData.split()


def madLib(story, character, noun, adjective, verb):
    # make character a constant variable chosen at random at the beginning of the function call. This way the character is the same throughout the story.
    character = random.choice(character)
    story = story.replace("<character>", character)
    # split the string into a list of strings so that we can iterate through it to find each madlib placeholder.
    storyData = story.split()
    for i in storyData:  # for each word in the story
        if i.find("<noun>") != -1:  # if there is any occurence of the word <noun>
            storyData[storyData.index(i)] = random.choice(
                noun)  # replace the word with a random noun
        elif i.find("<adjective>") != -1:  # if there is any occurence of the word <adjective>
            storyData[storyData.index(i)] = random.choice(
                adjective)  # replace the word with a random adjective
        elif i.find("<verb>") != -1:  # if there is any occurence of the word <verb>
            storyData[storyData.index(i)] = random.choice(
                verb)  # replace the word with a random verb
        if i.find(".") != -1:
            nextWord = storyData[storyData.index(i) + 1]
            storyData[storyData.index(
                i) + 1] = nextWord.capitalize()
    return " ".join(storyData)  # join the list of words into a string


print(madLib(storyData, characterList, nounList, adjectiveList, verbList))


# this is my old code that i want to leave here in case i need to reference it later
# def madLib(story, noun, adjective, verb):
#     character = random.choice(noun)
#     numberNoun = story.count("<noun>")
#     print("there are ", numberNoun, "nouns in the story")
#     for i in range(numberNoun):
#         story = story.replace("<noun>", random.choice(noun), 1)
#     story = story.replace("<character>", character)
#     story = story.replace("<adjective>", random.choice(adjective))
#     story = story.replace("<verb>", random.choice(verb))
#     return story
