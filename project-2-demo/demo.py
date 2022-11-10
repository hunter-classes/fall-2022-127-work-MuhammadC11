def clean(s):
    letters = []
    for letter in s:
        if letter.isalpha() or letter == " " or letter == "\n":
            letters.append(letter)
    result = "".join(letters)
    return result
#   return only letters and spaces, no punctuation or numbers


def build_bow(data):
    counts = {}
    for word in data.split():
        counts.setdefault(word, 0)
        counts[word] = counts[word]+1

    return counts


file = open("demo.txt")
raw_data = file.read()
data = clean(raw_data)
bag = build_bow(data)

# .sorted() returns a list of tuples sorted by the first element in the tuple
# .reverse() reverses the order of the list


def get_words_min_max(bag, mincount, maxcount):
    results = []
    for word in bag.keys():
        if bag[word] >= mincount and bag[word] <= maxcount:
            results.append([word, bag[word]])
    return results


print(get_words_min_max(bag, 1, 3))


def get_words_range(bag, mincount, maxcount):
    results = [[x, bag[x]]
               for x in bag if bag[x] >= mincount and bag[x] <= maxcount]
    return results


print(get_words_range(bag, 100, 500))
