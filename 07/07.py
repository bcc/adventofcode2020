#!/usr/bin/python3

import sys
import re

def find_bags(bags, target):
    seen = []
    queue = []
    ret = {}
    queue.append(target)
    seen.append(target)

    while len(queue) > 0:
        current = queue.pop()
        if current in bags:
            items = bags[current]
            for item in items:
                if item not in seen:
                    count = int(items[item])
                    ret[item] = count
                    queue.append(item)
        seen.append(current)
    return ret


def find_bags2(bags, target):
    count = 1

    if target not in bags:
        return 1

    for item in bags[target]:
        v = find_bags2(bags, item)
        count = count + (v * int(bags[target][item]))

    return count


bags = {}
bags2 = {}
for line in sys.stdin:
    line = line.replace(' bags','')
    line = line.replace(' bag','')
    line = line.replace('.','')
    cont = line.rstrip().split(' contain ')
    outer = cont[0]
    inner = cont[1].split(', ')
    for bag in inner:
        m = re.match(r'^(\d+) (.*)$', bag)
        count = 0
        if m is not None:
            bag = m.group(2)
            count = m.group(1)
        if bag in bags:
            bags[bag][outer] = count
        else:
            t = {}
            t[outer] = count
            bags[bag] = t

        if bag == "no other":
            continue
        if outer in bags2:
            bags2[outer][bag] = count
        else:
            t = {}
            t[bag] = count
            bags2[outer] = t

valid1 = find_bags(bags, 'shiny gold')
print(1, len(valid1))

print(2, find_bags2(bags2, 'shiny gold')-1)
