#lambda functions
#SYNTAX:lambda arguments: expression
#A lambda function is an anonymous function (a function with no name) written in one expression.

A= lambda a,b:a*b    #assigning this to a variable

print(A(2,4))

#-------------utility of lambda with map, filter and reduce----------------------

#---------------map()--------------------
num=[1,2,3]
def s(i):
    return i*i
result= map(s,num)
print(list(result))

#using lambda instead of function definitions
res=(map(lambda a:a*2,num))
print(list(res))

#---------------filter()-----------------
number=[1,2,3,4,5,6]
def iseven(n):
    return n%2==0
ans=filter(iseven,number)
print(list(ans))

#using lambda instead of function definitions
answer=(filter(lambda n:n%2==0,number))
print(list(answer))

#-------------reduce()-------------------
exp=[('car',234),('darkchocolate',345),('dress',443)]
sum1=0
for i in exp:
    sum1+=i[1]
print(sum1)

#lets use reduce now
#we first import it from functools library
from functools import reduce
sum2=reduce(lambda a,b:a+b[1],exp,0)   #here a is the counter, b is the iterable, 0 is the initial value
print(sum2)

    
    
