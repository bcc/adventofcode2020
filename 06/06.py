#!/usr/bin/python3

import sys

def process_group(groupq):
    return len(groupq)

def process_group2(groupq, gsize):
    count = 0
    for q in groupq:
        if groupq[q] == gsize:
            count = count + 1
    return count

p1sum = 0
p2sum = 0
gsize = 0
groupq = {}

for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        p1sum = p1sum + process_group(groupq)
        p2sum = p2sum + process_group2(groupq, gsize)
        gsize = 0
        groupq = {}
        continue
    gsize = gsize + 1
    for q in line:
        if q in groupq:
            groupq[q] = groupq[q] + 1
        else:
            groupq[q] = 1
p1sum = p1sum + process_group(groupq)
p2sum = p2sum + process_group2(groupq, gsize)

print (1,p1sum)
print (2,p2sum)