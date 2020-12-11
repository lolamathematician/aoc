import re

cleaning_rule = re.compile('bags|bag')

with open('input.txt', 'r') as f:
	raw_rules = [line.replace('\n', '') for line in f.readlines()]

def clean_rules(initial_rules):
	sup_sub_rules = [raw_rule.split(' contain ') for raw_rule in raw_rules]

	final = sup_sub_rules

	return sup_sub_rules

final = clean_rules(raw_rules)

bag_rules = [raw_rule[0] for raw_rule in final]

bag_rules_set = {i for i in bag_rules}

print(len(raw_rules))
print(len(final))
print(len(bag_rules))
print(len(bag_rules_set))
