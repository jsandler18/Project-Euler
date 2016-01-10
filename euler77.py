from euler import prime_sieve, multiply_polynomials

primes = prime_sieve(10000)

for i in range(12,500):
    result = map(lambda x:int(x%2==0),[j for j in range(i+1)])
    for j in primes:
        if j > i:
            
            break
        elif j == 2:
            continue
        else:
            tmp = map(lambda x:int(x%j==0),[k for k in range(i+1)])
            result = multiply_polynomials(result,tmp)
    if result[i] > 5000:
        print "%d can be written as the sum of primes in %d ways" % (i, result[i])
