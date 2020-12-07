import string

with open('input.txt', 'r') as f:
	groups = f.read().split('\n\n')

common_letters_per_group = []

for group in groups:
	number_of_people_in_group = group.count('\n') + 1
	distinct_letters = 0
	for letter in string.ascii_lowercase:
		if group.count(letter) == number_of_people_in_group:
			distinct_letters = distinct_letters + 1
	common_letters_per_group.append(distinct_letters)

print(sum(common_letters_per_group))
