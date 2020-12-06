with open('input.txt', 'r') as f:
	l = [i.split(' ') for i in f.readlines()]
	l1 = [[int(j[0].split('-')[0]), int(j[0].split('-')[1]), j[1][0], j[2][:-1]] for j in l]

valid_count = 0

# for k in l1:
# 	if k[0] <= k[3].count(k[2]) <= k[1]:
# 		valid_count += 1

for k in l1:
	if k[3][k[0]-1] == k[2] and k[3][k[1]-1] != k[2]:
		valid_count += 1
	if k[3][k[0]-1] != k[2] and k[3][k[1]-1] == k[2]:
		valid_count += 1

print(valid_count)
