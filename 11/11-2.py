#!/usr/bin/python3

import sys
import copy

waiting = []
for line in sys.stdin:
    waiting.append(line.rstrip())

def check_seat (waiting, seat_x, seat_y):
    seats = [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
    count = 0
    for seat in seats:
        x = seat_x + seat[0]
        y = seat_y + seat[1]
        while x >= 0 and x < len(waiting[seat_y]) and y >= 0 and  y < len(waiting):
            s = waiting[y][x]
            if s == 'L':
                break
            if s == '#':
                count = count + 1
                break
            x = x + seat[0]
            y = y + seat[1]
    return count


seen = {}
stable = 0
occ = 0
while True:
    newwaiting = []
    occ = 0
    for seat_y in range(len(waiting)):
        newrow = ''
        for seat_x in range(len(waiting[seat_y])):
            count = check_seat(waiting,seat_x,seat_y)
            if waiting[seat_y][seat_x] =='.':
                newrow = newrow + '.'
            elif waiting[seat_y][seat_x] =='#' and count >= 5:
                newrow = newrow + 'L'
            elif  waiting[seat_y][seat_x] =='L' and count == 0:
                newrow = newrow + '#'
                occ = occ + 1
            else:
                newrow = newrow + waiting[seat_y][seat_x]
            
            if newrow[-1] == '#':
                occ = occ + 1

        newwaiting.append(newrow)
    waiting = newwaiting

    #print("\n".join(waiting))
    #print()
    pattern = "".join(newwaiting)
    if pattern in seen:
        break

    seen[pattern] = 1
    stable = stable + 1
    
print('2',stable, occ)


