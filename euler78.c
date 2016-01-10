#include <stdio.h>

#define BOUND 100000

int main() {
	int ways[BOUND+1];
	int i, j;
	ways[0] = 1;
	for (i = 1; i <= BOUND; i++) {
		for (j = i; j <= BOUND; j++) 
			ways[j] = (ways[j] + ways[j-i]) % 1000000;
		if (ways[i] == 0) {
			printf("%d has %d (partitions %% 1000000)\n", i, ways[i]);
			break;
		}
		if (i % 1000 == 0)
			printf("%d\n",i);
	}
	return 0;
}