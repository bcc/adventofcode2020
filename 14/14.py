#!/usr/bin/python3

import sys, re

mask = None

def parse_mask(mask):
    mask0 = mask1 = mask
    mask0 = mask0.replace('X','1')
    mask1 = mask1.replace('X','0')
    return(int(mask0,2), int(mask1,2))

def setbit(val, offset):
    mask = 1 << offset
    return (val | mask)

def clearbit(val, offset):
    mask = ~(1 << offset)
    return (val & mask)

def parse_mask2(val, mask):
    mask = mask[::-1]
    nums = [val]
    for m in range(len(mask)):
        t = []
        for v in nums:
            if mask[m] == 'X':
                t.append(setbit(v, m))
                t.append(clearbit(v, m))
            else:
                t.append(v)
        nums = t
    return nums

p1 = {}
p2 = {}
mask0 = mask1 = 0
tmask = ""
for line in sys.stdin:
    line = line.rstrip()

    m = re.match(r'^mask \= (\S+)$', line)
    if m is not None:
        tmask = m.group(1)
        (mask0, mask1) = parse_mask(tmask)
        continue
    
    m = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
    p2pos = pos = int(m.group(1))
    p2val = val = int(m.group(2))

    val = val & mask0
    val = val | mask1
    p1[pos] = val

    p2perms = parse_mask2(p2pos | mask1, tmask)
    for p in p2perms:
        p2[p] = p2val

print(1, sum(p1.values()))
print(2, sum(p2.values()))