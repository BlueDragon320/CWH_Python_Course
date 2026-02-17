''' 1. Take the string " i love python programming " and 
        1. Remove extra spaces from both ends
        2. Convert it to title case
        3. Count how many times "o" appears '''
    
text = " i love python programming "
print("Before: \n",text)
modtext1 = text.strip()
modtext2 = text.title()
modtext3 = text.count("o")
print("After: \n",modtext1 ,"\n", modtext2,"\n", modtext3)



'''2. Check if the string "123abc" is alphanumeric'''
taxt = "123abc"

print(taxt.isalnum())