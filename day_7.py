import os
import re

with open(os.path.join('Inputs', 'day_7.txt')) as f:
    rules = f.read().split('\n')

bag_dict = {}
bag_pat = re.compile(r'^(\d)*\s([a-z\s]*)\sbag')
for rule in rules:
    bag, content_str = rule.split(' bags contain ')
    content_str = [c.replace('.', '').strip() for c in content_str.split(',')]
    contents = {}
    for c in content_str:
        if c == 'no other bags':
            contents = None
        else:
            num, bag_inside = re.search(bag_pat, c).groups()
            contents[bag_inside] = int(num)
    bag_dict[bag] = contents


def return_contents(item, sg_count):
    sg_count += len([x for x in bag_dict[item] if x == 'shiny gold'])
    for i in bag_dict[item]:
        if bag_dict[i] is not None:
            return_contents(i, sg_count)
    return sg_count


def return_parents(item, sg_count, return_list):
    for k, v in bag_dict.items():
        if v is not None and item in v:
            return_list.append(k)
            return_parents(k, sg_count, return_list)
            print(k)
    return return_list


def part_1():
    print(len(return_parents('shiny gold', 0, ['shiny gold'])))


def part_1_test():
    bag_dict = {}
    bag_pat = re.compile(r'^(\d)*\s([a-z\s]*)\sbag')
    for rule in rules:
        bag, content_str = rule.split(' bags contain ')
        content_str = [c.replace('.', '').strip() for c in content_str.split(',')]
        contents = {}
        for c in content_str:
            if c == 'no other bags':
                contents = None
            else:
                num, bag_inside = re.search(bag_pat, c).groups()
                contents[bag_inside] = int(num)
        bag_dict[bag] = contents

def part_2():
    pass


if __name__ == '__main__':
    part_1()
    # print(part_2())
