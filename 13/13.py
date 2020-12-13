#!/usr/bin/python3

import sys

estimate = int(input())
line = input()
buses = line.rstrip().split(',')
ibus = []


bestwait = None
bestbus = 0
for bus in buses:
    if bus == 'x':
        ibus.append(1)
        continue
    bus = int(bus)

    ibus.append(bus)
    mins = estimate % bus
    wait = bus - mins
    if bestwait is None or bestwait > wait:
        bestwait = wait
        bestbus = bus

print(1, bestwait * bestbus) 

l = []
biggest = 0
bigpos = 0
for i,bus in enumerate(ibus):
    if bus != 1:
        l.append(i)
    if bus > biggest:
        biggest = bus
        bigpos = i


#print(l)

ts = 0
mult = 1
for i in l:
    while True:
        if (ts + i) % ibus[i] == 0:
            break
        ts = ts + mult
    mult = mult * ibus[i]
print(2,ts)   


## Garbage, too slow even with looping on the largest value - offset
step = ibus[0]
current = -1 * bigpos
while True:
    current = current + biggest
    if current % step != 0:
        continue

    worked = True
    for i in l:
        ctime = current + i
        if ctime % ibus[i] != 0:
            worked = False
            break

    if worked:
        print(2, current)
        sys.exit()
