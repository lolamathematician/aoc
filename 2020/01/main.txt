from itertools import combinations

with open('input.txt', 'r') as f:
	l = [int(line[:-1]) for line in f]

combs = [triple for triple in combinations(l, 3)]

for triple in combs:
	if triple[0] + triple[1] + triple[2] == 2020:
		print(triple[0] * triple[1] * triple[2])
