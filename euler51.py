import math

def isPrime(number):
    if number % 2 == 0:
        return False
    else:
        for i in range(2, int(math.ceil(math.sqrt(number))) + 1):
            if number % i == 0:
                return False

    return True

def round_down(num, divisor):
    return num - (num%divisor)

found = False
for i in range (1000000):
    if isPrime(i):
        #create a list of numbers that correspond to unique digits
        #1 corrsesponds to a digit that is the same, and 0 to
        #the rest for each digit
        matches = []
        for j in range(10):
            match = ""
            for k in str(i):
                if k == str(j):
                    match += '1'
                else:
                    match += '0'
            if match.find('1') != -1:
                matches.append(int(match))

        # loop through all possible digit replacement patterns for this number        
        for j in matches:
            primes = [i]
            nextPrime = i + j
            #set a max value so we can't accidentally go over
            place = round_down(j, 10 ** (len(str(j)) -1))
            maxPrime = round_down(i+10*place,10*place)
            #loop at most 10 times
            for k in range(10):
                if isPrime(nextPrime) and nextPrime < maxPrime:
                    primes.append(nextPrime)
                if len(primes) == 8:
                    found = True
                    print primes
                    break
                nextPrime += j
            if found:
                break
    if found:
        break
            
