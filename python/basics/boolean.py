a= -1              #-1 is true only "" , False and 0 are false
if a:
    print("yayyy")

#'any' function

a=True
b=False
c=any([a,b])
print(c)

#'all' function

d=all([a,b])
print(d)


#--------------------COMPLEX DATA TYPE-----------------------

num1=2+3j
print(num1.real)

num2=complex(2,3)
print(num2.imag)

print(type(num1))


#---------------SOME MORE BUILT IN FUNCTIONS------------------

print(abs(-3))
print(round(5.9))
print(round(5.789,2))


#-------------------ENUMS--------------------------

from enum import Enum

class color(Enum):
    RED=1
    green=2
    blue=3

print(color.RED.value)  #to print values
print(color.green.value)
print(color.RED)

for i in color:         #to list colors
    print(i)

print(color(3))

print(list(color))  #prints list of all values

print(len(color))

