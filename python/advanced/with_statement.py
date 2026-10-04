name='DATA.txt'

try:
    file=open(name,'r')
    content=file.read()
    print(content)
finally:
    file.close()

#using "with"
#with can automatically close a file

with open(name,'r') as file:
    print(file.read())
