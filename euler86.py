from fractions import gcd

triples = []
dimens = []
def ptriple_tree(a,b,c):
    k=1
    if a < 101 and b < 101 and c < 101:
        while k*a < 101 and k*b < 101 and k*c < 101:
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

