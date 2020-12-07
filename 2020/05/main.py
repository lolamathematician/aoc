with open('input.txt', 'r') as f:
	boarding_passes = [line[:-1] for line in f.readlines()]

def get_seat_id(seat_string):
	row_string = seat_string[:7]
	col_string = seat_string[-3:]

	row_binary_string = row_string.replace('F', '0')
	row_binary_string = row_binary_string.replace('B', '1')

	col_binary_string = col_string.replace('L', '0')
	col_binary_string = col_binary_string.replace('R', '1')

	row_decimal = int(row_binary_string, 2)
	col_decimal = int(col_binary_string, 2)

	seat_id = row_decimal * 8 + col_decimal

	return seat_id


seat_ids = [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]

seat_ids.sort()

for i in range(len(seat_ids)):
	if (seat_ids[i] + 1) != seat_ids[i+1]:
		print(seat_ids[i-2:i+2])
		break
