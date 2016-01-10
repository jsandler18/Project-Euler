from decimal import *
from euler import digital_sum
from math import sqrt, ceil

result = 0
squares = [1,4,9,16,25,36,49,64,81,100]
getcontext().prec = 102
for i in range(1,101):
    if not i in squares:
        i = Decimal(i).sqrt()
        result += digital_sum(str(i)[:101].replace(".",""))


print result
