import re

hcl_re = re.compile('#[0-9a-f]{6}')

pid_re = re.compile('[0-9]{9}')

valid_passports = 0

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

passports_fields = []

passport_dicts = []

with open('input.txt', 'r') as f:
	passports = f.read().split('\n\n')

def print_passports(passports):
	for passport in passports:
		print(passport, end='\n---------\n')

def get_fields_from_passports(passports):
	for passport in passports:
		passport_fields = re.split('\n| ', passport)
		passport_dict = {}
		for field in passport_fields:
			key_and_value = field.split(':')
			passport_dict[key_and_value[0]] = key_and_value[1]
		passport_dicts.append(passport_dict)

get_fields_from_passports(passports)

# passport_dicts = [passport_dicts[0]]
# for key in passport_dicts[0].items():
	# print(key)

def byr_check(byr):
	return 1920 <= int(passport_dict['byr']) <= 2002

def iyr_check(iyr):
	return 2010 <= int(passport_dict['iyr']) <= 2020

def eyr_check(eyr):
	return 2020 <= int(passport_dict['eyr']) <= 2030

def hgt_check(hgt):
	hgt_units = passport_dict['hgt'][-2:]
	try:
		hgt_value = int(passport_dict['hgt'][:-2])
	except ValueError:
		return False
	if (hgt_units == 'cm') and (150 <= hgt_value <= 193):
		return True
	elif (hgt_units == 'in') and (59 <= hgt_value <= 76):
		return True
	else:
		return False

def hcl_check(hcl):
	hcl = str(passport_dict['hcl'])
	if len(hcl) == 7:
		if re.match(hcl_re, hcl) != None:
			return True
	return False

def ecl_check(ecl):
	ecl = str(ecl)
	if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return True
	return False

def pid_check(pid):
	pid = str(pid)
	if len(pid) == 9:
		if re.match(pid_re, pid) != None:
			return True
	return False


for passport_dict in passport_dicts:
	present_fields = set(passport_dict.keys()) - {'cid'}
	# print(present_fields, end='\t\t')
	if present_fields == required_fields:
		byr_valid = byr_check(passport_dict['byr'])
		iyr_valid = iyr_check(passport_dict['iyr'])
		eyr_valid = eyr_check(passport_dict['eyr'])
		hgt_valid = hgt_check(passport_dict['hgt'])
		hcl_valid = hcl_check(passport_dict['hcl'])
		ecl_valid = ecl_check(passport_dict['ecl'])
		pid_valid = pid_check(passport_dict['pid'])
		all_valid = byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid
		# print('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
		# print(byr_valid, iyr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid)
		if all_valid:
			print('V')
			valid_passports = valid_passports + 1
	else:
		print('I')

print(valid_passports)
