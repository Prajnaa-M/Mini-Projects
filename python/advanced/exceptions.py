#---------------------------------------------EXCEPTIONS---------------------------------------------------
#SYANTX:
##try:
##    code that might raise an exception
##    risky_code()
##
##except ValueError:
##    runs if ValueError occurs
##    handle_value_error()
##
##except ZeroDivisionError:
##    runs if ZeroDivisionError occurs
##    handle_zero_division()
##
##except Exception as e:
##    runs for ANY other exception
##    print(e)
##
##else:
##    runs ONLY if no exception occurred



##    success_code()
##
##finally:
##    runs ALWAYS (exception or not)
##    cleanup_code()

try:
    result=2/0
except ZeroDivisionError:
    print("a number cant be divided by zero you dumb daft dimbo")
finally:
    result=1

print(result)

try:                          #prints only one idicating that the finally block runs no matter what
    res=4/2
except ZeroDivisionError:
    print("a number cant be divided by zero you dumb daft dimbo")
finally:
    res=1
print(res)

#we can also raise errors
#raise Exception('ERROR :(((')

#also we can intercept it like this
try:
    raise Exception('ERROR :(((')
except Exception as i:
    print(i)

#we can also define our own exception
class myexp(Exception):
    print("inside")
    pass            #pass in Python is basically a “do nothing” statement, It’s used when Python requires a block, but you don’t want to write code yet.
try:
    raise myexp()
except myexp:
    print("HAHA MORON")

