import os
import re

with open(os.path.join('Inputs', 'day_2.txt')) as f:
    data = f.read().split('\n')

matches = []
for item in data:
    policy, pw = item.split(': ')
    num_range, letter = policy.split(' ')
    low_num, high_num = num_range.split('-')
    low_num = int(low_num)
    high_num = int(high_num)
    match = re.search(letter, pw)


