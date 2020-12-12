#!/usr/bin/python3

import sys

class Ship:
    
    def __init__(self):
        self.facing = 'E'
        self.x = 0
        self.y = 0

        self.moves = {'E': [1,0],
                'S': [0,-1],
                'W': [-1,0],
                'N': [0,1]}

        self.turns = {'E': ['N','S','W'],
                'S': ['E','W','N'],
                'W': ['S','N','E'],
                'N': ['W','E','S']}

    def rotate(self, direction, degrees):
        if degrees == 180:
            self.facing = self.turns[self.facing][2]
        elif degrees == 90 and direction == 'L':
            self.facing = self.turns[self.facing][0]
        elif degrees == 90 and direction == 'R':
            self.facing = self.turns[self.facing][1]
        elif degrees == 270 and direction == 'L':
            self.facing = self.turns[self.facing][1]
        elif degrees == 270 and direction == 'R':
            self.facing = self.turns[self.facing][0]
        else:
            raise Exception("Invalid Turn")

    def move(self, direction, num):
            if direction == 'F':
                self.x = self.x + (self.moves[self.facing][0] * num)
                self.y = self.y + (self.moves[self.facing][1] * num)
            else:
                self.x = self.x + (self.moves[direction][0] * num)
                self.y = self.y + (self.moves[direction][1] * num)

    def do(self, instruction, unit):
        if instruction in ['L', 'R']:
            self.rotate(instruction, unit)
        else:
            self.move(instruction, unit)


ship = Ship()
for line in sys.stdin:
    instruction = line[0]
    unit = int(line[1:])
    ship.do(instruction, unit)

print(1,abs(ship.x) + abs(ship.y))
