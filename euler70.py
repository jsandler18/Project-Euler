from fractions import gcd
from math import sqrt, ceil
from decimal import *

def relPrimes(num, primes):
        result = 1
        for i in primes:
                result *= (1 - 1/Decimal(str(i)))

        return int(round(num * result,0))

def arePerms(num1, num2):
        num1digs = [0,0,0,0,0,0,0,0,0,0]
        num2digs = [0,0,0,0,0,0,0,0,0,0]
        for i in str(num1):
                num1digs[ord(i) - ord('0')] +=1
        for i in str(num2):
                num2digs[ord(i) - ord('0')] +=1

        return num1digs == num2digs
        

def primes(start, end):
        result = []
        for i in range(start, end+1):
                if i % 2 != 0 and i != 1:
                        isPrime = True
                        for j in range(3,int(ceil(sqrt(i)) +1)):
                                if i % j == 0:
                                        isPrime = False
                                        break
                        if isPrime:
                                result.append(i)
        return result

p = primes(2000,5000)
minn = 0
minrat = 2

i = 0
j = 1

while (i < len(p)):
        while (j < len(p)):
                n = p[i] * p[j]
                if n < 10 ** 7:
                        rels = relPrimes(n, [p[i], p[j]])
                        if arePerms(n, rels):
                                rat = float(n)/rels
                                if rat < minrat:
                                        minrat = rat
                                        minn = n
                j+=1
        i+=1
        j=i+1

print minn
print minrat





        
        

