# String formatting

template = "Hey {}, how are you doing?"

a = "Ram"
b = "Sham"
c = "Raju"
d = "Rohan"

s1 = template.format(a)
s2 = template.format(b)

print(s1, s2)


name = "Jaron"
marks = 74
print(f"{name} you scored {marks} in Maths")
