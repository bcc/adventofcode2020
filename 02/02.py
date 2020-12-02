#!/usr/bin/python3

import sys

ints = []
for line in sys.stdin:
    instructions = line.rstrip().split(' ')

    c = instructions[0].split('-')
    c_min = int(c[0])
    c_max = int(c[1])
    c_char = instructions[1][0]
    pw = instructions[2]

    # Part 1 test
    count = 0
    for c in pw:
        if c == c_char:
            count = count + 1

    if c_min <= count <= c_max:
        print(1, pw)

    # Part 2 test
    count2 = 0
    if c_min <= len(pw) and pw[c_min - 1] == c_char:
        count2 = count2 + 1
    
    if c_max <= len(pw)  and pw[c_max - 1] == c_char:
        count2 = count2 + 1

    if count2 == 1:
        print(2, pw)