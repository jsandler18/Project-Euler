#digit factorial sum, sum of each digit factorial
def dfs(n):
    result = 0
    for i in str(n):
        result += factorial(int(i))
    return result
    

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

#how many dfs to loop back to start number
def dfs_chain_len(n):
    result = 1
    loop = [n]
    n = dfs(n)
    while not n in loop:
       result += 1
       loop.append(n)
       n = dfs(n)
    return result

len60 = 0

for i in reversed(range(1,1000000)):
    if dfs_chain_len(i) == 60:
        len60 +=1
        print i
        print len60


print len60
    
