#-----------------------------------------------variables--------------------------------------------------
name="prajnaa"
print(type(name))  #to find type of a variable

print(type(name)==str) #checks if var is of a given variable type
print(isinstance(name,str))#same as the above line

num="3"
print(type(num))
print(type(int(num)))




#------------------------------------------------assignment operators----------------------------------------
print(
    3+5,
    3-5,
    3*5,
    5/3,
    5//3,
    5%3,
    3**5,
    sep="\n")

a=3      # print(a+=3) is inavliid
a+=3
print(a)




#------------------------------------------------comparison operators---------------------------------------------
a=2
b=3

print(a==b, a!=b , a<=b , a>=b, sep="\n")




#-----------------------------------------------logical operators(and, or , not)--------------------------------------
x=True
y=False
print(x and y , x or y, not x, not y , sep="\n")

print(0 or 1)               #the operator 'or' returns the first value thats not false or the last value
print(False or "hi")
print([] or False)
print(False or [])
print("hi" or "hello")

print(0 and 1)              #the 'and' operator returns the first false value or the last
print(1 and 0)
print(False and "hi")
print([] and False)
print(False and [])
print("hi" and "hello")




#----------------------bitwise operators are  & ,| , ^ , ~ , << , >> , these are binary AND ,OR, XOR, NOT ,and shift left and right------------------------




#--------------------------------------------------identity operatorss are is and is not-----------------------------------------------------




#--------------------------------------------------membership operators are in and not in------------------------------------------------------




#------------------------------ternary operator syntax: x if condition else y----------------------------------------
c=2
d=4
print("yayy") if a<b else print("ew")








