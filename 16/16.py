#!/usr/bin/python3

import sys, re

rules = {}
invalid = 0
unpossible = {}
opts = 0
myticket = None

for line in sys.stdin:
    line = line.rstrip()
    m = re.match(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$', line)
    if m is not None:
        rules[m.group(1)] = [int(m.group(2)),int(m.group(3)),int(m.group(4)),int(m.group(5))]

    m = re.match(r'^([\d+,])+$', line)
    if m is not None:
        values = line.split(',')
        if myticket is None:
            myticket = values

        # Part 1
        skip = False
        for v in values:
            v = int(v)
            valid = 0
            for r in rules:
                k = rules[r]
                if k[0] <= v <= k[1] or k[2] <= v <= k[3]:
                    valid += 1

            if valid == 0:
                invalid += v
                skip = True
        if skip:
            continue
    

        # Part 2
        for i,v in enumerate(values):
            v = int(v)

            for r in rules:
                k = rules[r]
                if not (k[0] <= v <= k[1] or k[2] <= v <= k[3]):
                    if r in unpossible:
                        unpossible[r].append(i)
                    else:
                        unpossible[r] = [i]

        opts = len(values)

# dirty hacks done dirt cheap.
possible = {}
for r in rules:

    if r in unpossible:
        poss = unpossible[r]
    else: 
        poss = []

    t = []
    for i in range(opts):
        if i not in poss:
            t.append(i)
    possible[r] = t


final = {}
used = {}
for rules in sorted(possible, key=lambda key: len(possible[key])):
    #print(rules, possible[rules])
    if rules not in final:
        for i in possible[rules]:
            if i not in used:
                final[rules] = i
                used[i] = 1
                break


r2 = 1
for field in final:
    #print(field, final[field], myticket[final[field]])
    if field.startswith('departure'):
        r2 *= int(myticket[final[field]])
        
print(1, invalid)
print(2, r2)