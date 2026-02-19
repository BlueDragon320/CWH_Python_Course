'''Two types of modules in python:
1) Build in Modules
2) External Modules

https://docs.python.org/3/py-modindex.html
'''

import mymodule
import requests

mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)