#!/usr/bin/python3

import sys

for line in sys.stdin:
    nums = line.rstrip().split(',')

    seen = {}
    turn = 1
    last = 0
    # Load numbers
    for n in nums:
        n = int(n)
        if n in seen:
            seen[n].append(turn)
        else:
            seen[n] = [turn]

        turn += 1
        last = n

    next = 0

    while turn <= 30000000:

        if last not in seen:
            next = 0
        else:
            a = seen[last]
            if len(a) == 1:
                next = 0
            else:
                next = a[-1] - a[-2]
  
        if next in seen:
            seen[next].append(turn)
        else:
            seen[next] = [turn]

        if turn == 2020:
            print(1,next)

        turn += 1
        last = next

    print (2, next)
    
