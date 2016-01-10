from fractions import gcd

def relPrimes(num):
	relPrimes = []
	for i in range(1,num):
		if gcd(num, i) == 1:
			relPrimes.append(i)
	return relPrimes

n = 6
phi = 3

while n < 1000000:
        x = relPrimes(n)
        del x[0]
        for i in x:
                #if higher ratios
                if float(i * n) / (phi * len(relPrimes(i))) > float(n)/phi:
                        n *= i
                        phi *= len(relPrimes(i))
                        print n
                        break



