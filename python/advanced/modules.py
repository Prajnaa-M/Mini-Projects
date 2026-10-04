import names        #importing a module from another file
names.name()

from names import name  #importing a function from a module present in another file
name()

from modules import PRACTICE   #importing a module in another subfolder
PRACTICE.quality()

from modules.PRACTICE import quality   #importing a function from a module present in an another subfolder
quality()

#SOME MODULES FROM THE PYTHON STANDARD LIBRARY

#1.math
#2.re (for regular expressions)
#3.json (to work with JSON)
#4.datetime (to work with dates)
#5.sqlite3 (to use SQLite)
#6.os (for operating system utilities)
#7.random (for random number generation)
#8.statistics (for statistics utilities)
#9.requests (to perform HTTP network requests)
#10.http (to create HTTP servers)
#11.urllib(to manage URLs)

import math          #using standard math library
print(math.sqrt(9))
from math import *
print(sqrt(4))


