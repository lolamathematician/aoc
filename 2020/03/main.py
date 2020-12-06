import math

right_move_length = 3
down_move_length = 1

x_current = 0
y_current = 0

trees_hit = 0

input_width = len

with open('input.txt', 'r') as f:
	lines = f.readlines()
	block_width =  len(lines[0])
	y_max = len(lines) - 1
	number_of_moves = y_max / down_move_length
	x_max = number_of_moves * right_move_length
	number_of_times_need_to_repeat = math.ceil(x_max/block_width)
	l = [line[:-1]*number_of_times_need_to_repeat for line in lines]
	l[-1] += '.' * number_of_times_need_to_repeat

for i in l:
	print(l)

# print(x_max, y_max, number_of_moves, number_of_times_need_to_repeat)

while y_current <= y_max	:
	if l[y_current][x_current] == '#':
		trees_hit += 1
	x_current += 1
	y_current += 1
	print(x_current, y_current, trees_hit)

print(trees_hit)
