from fractions import gcd
def next_farey(max_den, prev2num, prev2den, prev1num, prev1den):
        k = int((max_den + prev1den)/prev2den)
        p = k*prev2num - prev1num
        q = k*prev2den - prev1den
        return (p,q)

count = 0
done = False
prev1num = 1
prev1den = 11999
prev2num = 1
prev2den = 12000

while True:
        if prev1num * 2 >= prev1den:
                break
        if prev1num * 3 > prev1den:
                count +=1
        tmp = next_farey(12000, prev1num,prev1den,prev2num,prev2den)
        prev2num = prev1num
        prev2den = prev1den
        prev1num = tmp[0]
        prev1den = tmp[1]

print count


