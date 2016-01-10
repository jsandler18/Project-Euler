bound = 50000
ways = [0 for x in range(bound+1)]
ways[0] = 1

for i in range(1, bound+1):#for each number that a sum could be split into
	for j in range(i, bound+1):#for each number that can include the largest number we are up to in the sum
		ways[j] = (ways[j] + ways[j-i]) % 1000000#the first part of the sum = i, the number of ways to make j += the number of ways to make j-i
	if ways[i] == 0:
		print "%d has %d (partitions % 1000000)" % (i, ways[i])
		break
	if i % 1000 == 0:
		print i

print ways[bound]