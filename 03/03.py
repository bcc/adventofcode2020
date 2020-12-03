#!/usr/bin/python3

import sys

x_move1 = 3
y_move1 = 1

p2_move = [ [1,1], [3,1], [5,1], [7,1], [1,2] ]

lines = []
for line in sys.stdin:
  lines.append(line.rstrip())

def check_slope(lines, x_move, y_move):
    count = 0
    x = 0
    y = 0
    while y < len(lines)-1:
        for i in range(0, x_move):
            x = (x + 1) % (len(lines[y]))

        for i in range(0,y_move):
            y = y + 1
        
        if lines[y][x] == '#':
            count = count + 1

    return count


print(check_slope(lines, x_move1, y_move1))

result = 1
for p2 in p2_move:
    result = result * check_slope(lines, p2[0], p2[1])

print(result)