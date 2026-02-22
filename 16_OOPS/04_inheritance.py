class Animal: # Parent class (superclass)
    location = "Austria"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic animal sound")
        
class Dog(Animal): 
    def speak(self): 
        super().speak()
        print("Woof!")
        
d = Dog("bruno")
d.speak()
print(d.location)