#!/usr/bin/python3

import sys
import itertools

def testvalid(numbers, i):
    for a, b in itertools.combinations(numbers, 2):
        if a + b == i:
            #print('ok: ',a,b,)
            return True
    return False

def findcontig(numbers, i):
    for start in range(len(numbers)-1):
        c = 0
        for end in range(start, len(numbers)):
            c = c + numbers[end]
            if c == i:
                return sorted(numbers[start:end+1])
    return None

preamble = 25
numbers = []
allnum = []
bad = None

for line in sys.stdin:
    i = int(line.rstrip())
    if len(numbers) >= preamble:
        if not testvalid(numbers, i):
            bad = i
        numbers.pop(0)

    numbers.append(i)
    allnum.append(i)
    
print(1, bad)

cont = findcontig(allnum, bad) 
print(2,cont[0] + cont[-1])