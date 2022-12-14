storyfile = open("demo.txt")
story_data = storyfile.read()
stopwords_data = open("stopwords.txt").read().split()


def clean(s):
    letters = []
    for letter in s:
        if letter.isalpha() or letter == " " or letter == "\n":
            letters.append(letter)
    result = "".join(letters)
    return result
#   cleans out the data file to return only letters and spaces, no punctuation or numbers


def build_bow(data):
    counts = {}
    for word in data.split():
        counts.setdefault(word, 0)
        counts[word] = counts[word]+1
    return counts
#   creates a tally of the words in the data file


data = clean(story_data)
bag = build_bow(data)

# .sorted() returns a list of tuples sorted by the first element in the tuple
# .reverse() reverses the order of the list


def get_words_min_max(bag, mincount, maxcount):
    results = []
    for word in bag.keys():
        if bag[word] >= mincount and bag[word] <= maxcount:
            results.append([word, bag[word]])
    return results


#print(get_words_min_max(bag, 1, 3))


def get_words_range(bag, mincount, maxcount):
    results = [[x, bag[x]]
               for x in bag if bag[x] >= mincount and bag[x] <= maxcount]
    return results


#print(get_words_range(bag, 100, 500))


def remove_stopwords(data, stopwords):
    for word in stopwords:
        if word in data:
            del data[word]
    return bag


print(remove_stopwords(bag, stopwords_data))


def remove_words_bag(bag, words_list):
    newbag = {}
    for word in bag.keys():  # for each word in the bag
        if word not in words_list:  # if the word is not in the list of words to remove
            newbag[word] = bag[word]  # add it to the new bag
    return newbag


print(remove_words_bag(bag, stopwords_data))
