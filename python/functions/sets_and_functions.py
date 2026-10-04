#------------------------------------SETS------------------------------------
#can contain only hashable data type elements(immutable)
#has NO DUPLICATE VALUES i.e, is any elemnt is present more than once, it considers it as only one...

set1={"Amy","mayur"}
set2={"Amy"}

union=set1 | set2   #union of sets (OR)
print(union)

inter=set1 & set2   #intersection of sets(AND)
print(inter)

diff=set1-set2      #difference of 2 sets
print(diff)

print(set1<set2)    #to check which set has more elements
print(set1>set2)


print(list(set1))

#-----------------------------FUNCTIONS-----------------------------------------

#SYNTAX: def fn_name(parameter) and the value you pass while calling the function is the argument

def hi(name="Prajnaa"):        #default parameter
    print("My name is ",name)
    
hi("muvva")
hi()

#nested functions

def a():
    name="PRAJNAA"
    def concat():
        nonlocal name          #to access the variable in the outer function
        print("your name is ",name)
    concat()
a()
