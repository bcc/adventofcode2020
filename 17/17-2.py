#!/usr/bin/python3

import sys, copy

neighbours = []
for x in [-1,0,1]:
    for y in [-1,0,1]:
        for z in [-1,0,1]:
            for w in [-1,0,1]:
                if  w== x == y == z == 0:
                    continue
                neighbours.append([x,y,z,w])

cube = {}
minx = miny = minz = minw = 0
maxz = 0
maxy = 0
maxx = 0
maxw = 0

for line in sys.stdin:
    for maxx, c in enumerate(line.rstrip()):
        if c == '#':
            pos = "%d,%d,%d,%d" % (maxx,maxy,maxz,maxw)
            cube[pos] = 1
    maxy += 1

def count_neighbours(cube, x, y, z,w):
    count = 0
    for n in neighbours:
        tz = z + n[0]
        ty = y + n[1]
        tx = x + n[2]
        tw = w + n[3]
        count += get_cell(cube, tx, ty, tz, tw)
    return count

def get_cell(cube, x, y, z, w):
    pos = "%d,%d,%d,%d" % (x,y,z,w)
    if pos in cube and cube[pos] == 1:
        return 1
    return 0

def process_cube(cube):
    global minx, miny, minz, maxx, maxy, maxz, minw, maxw
    minx -= 1
    miny -= 1
    minz -= 1
    minw -= 1
    maxx += 1
    maxy += 1
    maxz += 1
    maxw += 1
    
    newcube={}
    for w in range(minw, maxw+1):
        for z in range(minz, maxz+1):
            for y in range(miny, maxy+1):
                row = ""
                for x in range(minx, maxx+1):
                    pos = "%d,%d,%d,%d" % (x,y,z,w)
                    count = count_neighbours(cube, x, y, z, w)
                    if get_cell(cube, x, y, z, w) == 1:
                        if count == 2 or count == 3:
                            newcube[pos] = 1
                    else:
                        if count == 3:
                            newcube[pos] = 1

    return newcube

for n in range(6):
    cube = process_cube(cube)
print(len(cube))