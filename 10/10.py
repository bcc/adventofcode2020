#!/usr/bin/python3

import sys
from functools import lru_cache 

jolts = 0
adapt = [0]

for line in sys.stdin:
    i = int(line.rstrip())
    adapt.append(i)
adapt = sorted(adapt)

countjolts = {}
countjolts[3] = 1
valid = {}

for a in adapt:
    diff = a - jolts
    jolts = a
    if diff not in countjolts:
        countjolts[diff] = 1
    else:
        countjolts[diff] = countjolts[diff] + 1
print(1, countjolts[3] * countjolts[1])

# this is witchcraft
@lru_cache
def find_perms(adapt, n):
    current = adapt[n]
    pv = 0
    l = n + 4
    if l > len(adapt):
        l = len(adapt)

    for i in range(n+1, l):
        if adapt[i] > current + 3:
            continue

        pv = pv + find_perms(adapt, i)

    if pv == 0:
        return 1

    return pv

print(2, find_perms(tuple(adapt),0))
