person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'

}
person['age'] = person['age'] + 1

print(person)

k = person.keys()
print(k)
klist = [x for x in person.keys()]
print(klist)
v = person.values()
print(v)

vlist = [x for x in person.values()]
print(vlist)


s1 = {"name": "Evan", "age": 30, "scores": [95, 90, 75]}
s2 = {"name": "Jose", "age": 30, "scores": [90, 80, 78]}
s3 = {"name": "Matt", "age": 30, "scores": [90, 80, 100]}
s4 = {"name": "Derek", "age": 30, "scores": [90, 80, 70]}

student_list = [s1, s2, s3, s4]
student_dict = {}
for item in student_list:
    student_dict[item['name']] = item
print(student_dict)

s = """This is a string with a bunch of words in it. This is another sentence. This is the last sentence. how do we get the number of words in this string?"""

# ord() returns the unicode code point for a single character string
# chr() returns the character for a given unicode code point


def count_letters(s):
    """
    Count the number of letters in a string"""
    counts = {}

    for letter in s:
        if letter in counts.keys():
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


print(count_letters(s))


def count_words(s):
    """
    Count the number of words in a string"""
    counts = {}

    for word in s.split():
        # set default value to 0 if key doesn't exist
        counts.setdefault(word, 0)  # increment the value by 1 if key exists
        counts[word] += 1
    return counts


print(count_words(s))
