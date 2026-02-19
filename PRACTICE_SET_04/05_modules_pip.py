'''1. Import the math module and use it to:
    1. Find the square root of 144
    2. Calculate sin(90)'''
    
import math

square = math.sqrt(144)
print(square)

deg = math.radians(90)
print(deg)

'''2. Install and import the request module and use it to fetch data from ''https://api.github.com'''

import requests
reqt = requests.get("https://api.github.com")
print(reqt.text)