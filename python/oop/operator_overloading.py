#OPERATOR OVERLOADING
#thats we use to make classes comparable and to make them work with python operators

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):                         #this gt means greater than
        return True if self.age>other.age else False

person1=Human('rmr',2.5)
person2=Human('escape',5.5)

print(person1>person2)

#common methods for common operators like __gt__

##| Operator   | Method        |
##| ---------- | ------------- |
##| `+`        | `__add__`     |
##| `-`        | `__sub__`     |
##| `*`        | `__mul__`     |
##| `/`        | `__truediv__` |
##| `==`       | `__eq__`      |
##| `<`        | `__lt__`      |
##| `<=`       | `__le__`      |
##| `>`        | `__gt__`      |
##| `>=`       | `__ge__`      |
##| `len(obj)` | `__len__`     |
##| `obj[i]`   | `__getitem__` |
##| `str(obj)` | `__str__`     |

