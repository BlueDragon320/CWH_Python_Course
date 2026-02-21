'''1. Create a tuple coordinates = (10, 20) and print both elements.
2. Try to modify the tuple by setting coordinates[0] = 50 note what happens.
3. Convert the tuple to a list, change its first elements to 50, and conver it back to tuple'''


coordinates = (10, 20)

a ,b = coordinates
print(a,b)

# coordinates[0] = 50   doesnot get assigned throws error
# print(coordinates)

corlist = list(coordinates)
corlist[0] = 50
coordinates = tuple(corlist)
print(coordinates)