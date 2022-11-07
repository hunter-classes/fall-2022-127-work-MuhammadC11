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
