#CLASSES
class ahh:
    def queen(self):
        print("IM A SELF MADE QUEEN")
class person(ahh):                  # INHERITANCE FROM ANOTHER CLASS
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def yay(self):
        print("im so amazing!!! HA")

me=person("prajnaa",19)
print(me.name)
me.yay()
me.queen()                          # INHERITAMCE !!!

    
    
