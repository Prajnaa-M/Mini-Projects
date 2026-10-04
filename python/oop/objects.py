#EVERYTHING IN PYHTON IS CONSIDERED AN OBJECT

a=8
print(a.real)
print(a.imag)
print(a.bit_length())

#-----------------------------------LOOPS---------------------------------------
#SYNTAX: while condition is true: do sth

b=0
while b<=5:
    print(b)
    b+=1

#SYNTAX: for condition : do sth
for i in range(10):
    print(i+1)

list=["Amy","DAVID","TRIDOM","MIKE"]
for i,j in enumerate(list):         # enumertae gives both index and element
    print(i,j)

#'BREAK' or 'CONTINUE' inside loops and break or continue the flow
