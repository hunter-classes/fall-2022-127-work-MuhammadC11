#is even function number 7
def is_even(n):
   number = int(n)
   if number % 2 == 0:
     return True
   else:
     return False
    
print(is_even(107))

#is odd function number 8
def is_odd(n):
   number = int(n)
   if number % 2 != 0:
     return True
   else:
     return False
    
print(is_odd(110))

#is right angled number 10
def is_rightangled(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    # your code here

print(is_rightangled(3,4,5))

# is right angled where parameter order doesn't matter


def is_rightangled(a, b, c):
    if a**2 + b**2 == c**2 or a**2 +c**2 == b**2 or b**2 + c**2 == a**2 :
        return True
    else:
        return False
    # your code here

print(is_rightangled(4,3,5))


