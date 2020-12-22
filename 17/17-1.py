#!/usr/bin/python3

import sys, copy

neighbours = []
for x in [-1,0,1]:
    for y in [-1,0,1]:
        for z in [-1,0,1]:
            if x == y == z == 0:
                continue
            neighbours.append([x,y,z])

cube = {}
minx = miny = minz = 0
maxz = 0
maxy = 0
maxx = 0
for line in sys.stdin:
    for maxx, c in enumerate(line.rstrip()):
        if c == '#':
            pos = "%d,%d,%d" % (maxx,maxy,maxz)
            cube[pos] = 1
    maxy += 1

def print_cube(cube):
    global minx, miny, minz, maxx, maxy, maxz
    for z in range(minz, maxz+1):
        print("%d:" % z)
        for y in range(miny, maxy):
            row = ""
            for x in range(minx, maxx):
                if get_cell(cube, x,y,z) == 1:
                    row += '#'
                else: 
                    row += '.'
            print(row)

def count_neighbours(cube, x, y, z):
    count = 0
    for n in neighbours:
        tz = z + n[0]
        ty = y + n[1]
        tx = x + n[2]
        count += get_cell(cube, tx, ty, tz)
    return count

def get_cell(cube, x, y, z):
    pos = "%d,%d,%d" % (x,y,z)
    if pos in cube and cube[pos] == 1:
        return 1
    return 0

def process_cube(cube):
    global minx, miny, minz, maxx, maxy, maxz
    minx -= 1
    miny -= 1
    minz -= 1
    maxx += 1
    maxy += 1
    maxz += 1
    
    newcube={}
    for z in range(minz, maxz+1):
        for y in range(miny, maxy+1):
            row = ""
            for x in range(minx, maxx+1):
                pos = "%d,%d,%d" % (x,y,z)
                count = count_neighbours(cube, x, y, z)
                if get_cell(cube, x, y, z) == 1:
                    if count == 2 or count == 3:
                        newcube[pos] = 1
                else:
                    if count == 3:
                        newcube[pos] = 1

    return newcube

print_cube(cube)
for n in range(6):
    print("ROUND: %d ------------------" % n)
    cube = process_cube(cube)
    print_cube(cube)
print(len(cube))