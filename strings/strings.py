s1 ="Hello world"
s2= "my name is Mo"

s3 = """
THis is a multiline string
we use the triple quotes
for those
"""

# /n breaks up strings to create new lines
# concatenation using + in an argument
# * is used to multiply strings not the arithmetic
# .upper() or .lower() make a new string based on the values of the strig that is called
# you can slice a string by doing  s1[0:5] start at 0 and end at zero non inckusive

print(s1[0:3])
space_location = s1.find(" ")
s5 = s1[space_location+1 :]
print(s5)

def Initialize(name):
  name = input("Input your first and last name ")
  first = name[0].upper() +"."
  space_location = name.find(" ")
  last = name[space_location+1 :]
  finalName = first + last
  print(finalName)
  

Initialize("Muhammad Chaudhry")

def bondify(name):
  name = input("Input your first and last name")
  space_location = name.find(" ")
  last = name[space_location+1 :] 
  first = name[0].upper() + name[1:space_location]
  finalName= last +", " + first + " " + last
  print(finalName)

bondify("Mo")