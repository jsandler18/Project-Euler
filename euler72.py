def prime_factorization_sieve(n):
        nums = [[] for x in range(n)]
        #start counting primes at 2
        prime = 2
        #loop until primes too big
        while prime < n:
                """power is the size of the step to increment when adding primes.
                for example, when prime = 2 and power = 2. you append 2 to [2], then jump
                2 and append 2 to [4]. when power is increased to 4. you append 2 to [4] and
                jump and append 2 to [8]"""
                power = prime
                while power < n:
                        #multiple is the index
                        multiple = power
                        while multiple < n:
                                nums[multiple].append(prime)
                                multiple += power
                        power *= prime

                #find next prime
                k = prime + 1
                if k >= n:
                        return nums
                #find the first empty spot in the list, will have no factors
                while len(nums[k]) > 0:
                       k+=1
                       if k >= n:
                               return nums

                prime = k
        return nums

def product(nums):
        result = 1
        for i in nums:
                result *= i
        return result

pfs = prime_factorization_sieve(1000001)
print "prime sieve done"
tots = []

for i in pfs:
        tot = product(i)
        for j in set(i):
                tot *= (1 - 1/float(j))
        tots.append(int(round(tot)))
print "totients done"

print sum(tots) - 2
