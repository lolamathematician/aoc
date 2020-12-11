with open('input.txt', 'r') as f:
	positions = [(line)]

positions = []
number_of_positions = len(positions)
positions_visited = []
accumulator = 0

def step(position, operation, action):
	if position in positions_visited:
		print(accumulator)
		quit()
	if operation == 'acc':
		acc = accumulator + 1
		position = position + 1
	elif operation == 'jmp':
		position = position + action
	elif operation == 'nop':
		position = position + 1
	position = position % number_of_positions
	positions_visited.append(position)

