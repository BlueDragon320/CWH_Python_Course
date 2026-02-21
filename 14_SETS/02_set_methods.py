s = {32, 43, 54, 65, 23 , 4}

print(s)

s.add(32)
s.add(54)
s.remove(54) # Throws error if the number doesnot exist
s.discard(454) # this does not throw error
print(s)