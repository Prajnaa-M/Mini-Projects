#-----------------------------------------------------TUPLES-----------------------------------------------------
names=("BEAU","Ananya","david","Mycroft")

print(names.index("Ananya"))  #to find index of an element

print(len(names))             #to find length

print("david" in names)       #membership

#sort(names)print(names)is invalid
print(sorted(names))          #to sort a tuple and this not change the original tuple

#you also cant append or insert
new_names=names+("Prajnaa","muvva")
print(new_names)

#-----------------------------------------------DICTIONARIES-----------------------------------------------
#KEYS CAN BE ANY IMMUTABLE DATA TYPE BUT VALUE CAN ME OF ANY TYPE

d={"name":"BEAU","age":8,"friend":"DAVID","marks":120,"skin":"white"}
print(d["name"])

d['name']='syd'        #changes value of the key
print(d)

#d['color'] would give us KEY ERROR
#we can create a default value using get()
print(d.get('color'))  #this gives us none
print(d.get('color','blue'))#returns blue but the original dictionary remains unchanged
print(d)

print(d.pop('age'))    #returns the value removed and returns the original dictionary
print(d)

print(d.popitem())     #returns the last key-pair value and the original dictionary
print(d)

del d['marks']         #deletes a specific key-value pair

print("marks" in d)    #membership

print(list(d.keys()))  #returns a list of all keys in the dictionary

print(list(d.values()))#returns all the values in the dictionary

print(d.items())       #returns all the items of the dictionary

print(len(d))          #returns the length of the dictionary

dcopy= d.copy()        #creates a copy of the dictionary
print(dcopy)
print(dcopy==d)        #True 
print(dcopy is d)      #False

