#!/usr/bin/python3

import sys
import re

maxid = 0
ids = {}
for line in sys.stdin:
    rows = line[:7]
    seat = line[7:]

    rows = rows.replace('F', '0').replace('B', '1')
    seat = seat.replace('R', '1').replace('L', '0')

    row = int(rows, 2)
    column = int(seat, 2)
    seatid = row * 8 + column

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