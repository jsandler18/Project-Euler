from fractions import gcd

lengths = [0] * 1500001

def ptriple_tree(a,b,c):
    size = a+b+c
    k=1
    if size < 1500000:
        while k*size < 1500000:
            lengths[k*size] +=1
            k+=1
        #recursively calls ptriple_tree on each of the
        #three matrix transformations that generate a unique
        #prime triple
        ptriple_tree((a-2*b+2*c),(2*a-b+2*c),(2*a-2*b+3*c))
        ptriple_tree((a+2*b+2*c),(2*a+b+2*c),(2*a+2*b+3*c))
        ptriple_tree((-a+2*b+2*c),(-2*a+b+2*c),(-2*a+2*b+3*c))



#generate pythagorean triples using a "tree" with 3,4,5 as the root
a = 3
b = 4
c = 5

ptriple_tree(a,b,c)



count = 0
for i in lengths:
    if i == 1:
        count += 1
        
print count

print lengths[120]
