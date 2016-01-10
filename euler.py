from math import sqrt,ceil
from decimal import Decimal

"""returns a list of primes from 2 to n"""
def prime_sieve(n):
    p = [True for x in range(n+1)]#list from 0 to n init to true, true = prime
    p[0] = False
    p[1] = False
    for i in range(2,int(round(ceil(sqrt(n))))): #loop for i <= sqrt(n)
        if p[i]:#if i is marked as prime
            j = 0
            while i*i+j*i <= n:#loop through multiples and unmark as prime
                p[i*i+j*i] = False
                j+=1
    i = 0
    result = []
    for j in p: # loop through list and extract primes from idices
        if j:
            result.append(i)
        i+=1

    return result

"""takes two lists of numbers that are the coefficients of the polynomials
and multiplies them together.  these polynomials need not be of the same degree,
but all coefficients up to the largest degree in each polynomial must be filled
with 0 if there is no value there"""
def multiply_polynomials(p1, p2):
    result = [0 for x in range(len(p1) + len(p2) - 1)]
    for pow1,co1 in enumerate(p1):
        for pow2, co2 in enumerate(p2):
            result[pow1+pow2] += co1*co2

    return result

"""takes a number and returns the sum of its digits. The parameter can
be a string containing a number, an int or a decimal object"""
def digital_sum(n):
    result = 0
    if type(n) is not str:
        n = str(n)
    for i in n:
        result += (ord(i) - ord('0'))

    return result
