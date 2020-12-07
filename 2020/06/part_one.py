import string

with open('input.txt', 'r') as f:
	groups = f.read().split('\n\n')

distinct_letters_per_group = []

for group in groups:
	distinct_letters = 0
	for letter in string.ascii_lowercase:
		if letter in group:
			distinct_letters = distinct_letters + 1
	distinct_letters_per_group.append(distinct_letters)

print(sum(distinct_letters_per_group))
