from fractions import gcd

triples = []
dimens = []

m = 100

def ptriple_tree(a,b,c):
    k=1
    if a <= m and b <= m and c <= m:
        while k*a <= m and k*b <= m and k*c <= m:
            triples.append((k*a,k*b,k*c))
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

print triples

ways = 0
for triple in triples:
    m = max(triple)
    for leg in triple:
        if leg != m:
            ways += leg//2

print ways
