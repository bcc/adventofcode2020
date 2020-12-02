#!/usr/bin/python3

import sys

ints = []
for line in sys.stdin:
  ints.append(int(line.rstrip()))

p = range(0, len(ints))
# Inefficient, but fast enough.
for x in p:
    for y in p:
        if x == y:
            continue

        for z in p:
            if x == z or y == z:
                continue

            if ints[x] + ints[y] + ints[z] == 2020:
                print (2, ints[x] * ints[y] * ints[z])
            
        if ints[x] + ints[y] == 2020:
            print (1, ints[x] * ints[y])