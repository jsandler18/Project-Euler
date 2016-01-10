from itertools import permutations
class Ring:

    #data should be a list of 10 elements
    #first 5 go on outside, second 5 go on inside
    def __init__(self, data):
        #ring is a list of of triplets, read from data. 
        #first half are external nodes and second half are internal
        self.ring = []
        for i in range(len(data)/2):
            self.ring.append([data[i], data[i+len(data)/2], data[i+1+len(data)/2] if i+1+len(data)/2 < len(data) else data[len(data)/2]])

    def __str__(self):
            result = ""
            for i in self.ring:
                result += str(i[0]) + str(i[1]) + str(i[2])
            return result
    def isValid(self):
        cursum = sum(self.ring[0])
        for i in self.ring:
            if cursum != sum(i):
                return False
            cursum = sum(i)
        return True


largest = 0
#put largest numbers in external nodes for largest sum
for i in permutations([7,8,9,10]):
    for j in permutations([1,2,3,4,5]):
        #6 must always come first, because counting starts from smallest external node
        x = Ring((6,) + i + j)
        if x.isValid():
            largest = int(str(x)) if int(str(x)) > largest else largest

print largest

        
