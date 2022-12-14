import random
import piglatin
counting = [x for x in range(1, 10)]
print(counting)
tens = [10 for x in range(5, 10)]
print(tens)
random_list_v2 = [random.randrange(1, 10) for x in range(10)]
print(random_list_v2)
random_list_v3 = [random.randrange(1, 10) for x in range(10)]
print(random_list_v3)

sentence = "Manchester United"
splitsent = sentence.split()

# upper = [word.capitalize() for word in sentence.split()]
# print(upper)
upper2 = [piglatin.piglatin(word) for word in splitsent]
print(upper2)
