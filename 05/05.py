#!/usr/bin/python3

import sys

maxid = 0
ids = {}
for line in sys.stdin:
    line = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    seatid = int(line, 2)

    ids[seatid] = 1
    if maxid < seatid:
        maxid = seatid

print(1, maxid)

seen = 0
for i in range(maxid):
    if i not in ids:
        if seen == 1:
            print(2,i)
            sys.exit
    else:
        seen = 1