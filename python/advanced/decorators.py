#DECORATORS: to modify the behaviour of the function without modifying the function itself
#syntax: def decorator(func):
##          def wrapper():
##              print("Before function")
##              func()
##              print("After function")
##          return wrapper




def hehe(func):     #defining a decorator; it takes a function as a parameter
    def wrapper():
        print("before")
        val=func()
        print("after")
        return val
    return wrapper
@hehe
def hello():
    print('hi')
hello()
