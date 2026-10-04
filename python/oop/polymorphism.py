#polymorphism means he same interface or function name can work with different types of objects

class dog:
    def eat(self):
        print("BONE")

class cat:
    def eat(self):
        print("RAT")
hehe=cat()
hehhe=dog()
hehe.eat()
hehhe.eat()

a=[dog(),cat()]
for i in a:
    i.eat()

#DUCK TYPING
#An object’s suitability is determined by what it can do, not by what it is

def whatiteats(obj):
    obj.eat()

whatiteats(dog())
whatiteats(cat())
    

    
