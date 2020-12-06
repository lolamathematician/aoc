import math

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

trees_hit_record = []

with open('input.txt', 'r') as f:
	lines = [line.replace('\n', '') for line in f.readlines()]

# x_mod is the width of one input line to handle x_current going over the edge of the input
x_mod = len(lines[0])

# reduce y_max by one as the first line has index 0 in lines
y_max = len(lines) - 1

for slope in slopes:
	trees_hit = 0
	x_current = 0
	y_current = 0
	right_move_length = slope[0]
	down_move_length = slope[1]
	# x_full_position = 0
	while y_current <= y_max:
		if lines[y_current][x_current] == '#':
			trees_hit += 1
			# print('#')
		# else:
		# 	print('.')
		# print(x_current, '\t', x_full_position, '\t', y_current, '\t', trees_hit, end='\t')
		x_current = (x_current + right_move_length) % x_mod
		# x_full_position = x_full_position + right_move_length
		y_current = y_current + down_move_length
	trees_hit_record.append(trees_hit)
	# print('\n', '-'*34)

print(trees_hit_record)