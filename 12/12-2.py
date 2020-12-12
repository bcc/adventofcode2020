#!/usr/bin/python3

import sys

class Ship:
    
    def __init__(self):
        self.facing = 'E'
        self.wp_x = 10
        self.wp_y = 1
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
            self.wp_x = self.wp_x * -1
            self.wp_y = self.wp_y * -1
        elif (degrees == 90 and direction == 'L') or (degrees == 270 and direction == 'R'):
            t = self.wp_x
            self.wp_x = self.wp_y * -1
            self.wp_y = t
        elif (degrees == 90 and direction == 'R') or (degrees == 270 and direction == 'L'):
            t = self.wp_x
            self.wp_x = self.wp_y
            self.wp_y = t * -1
        else:
            raise Exception("Invalid Turn")

    def movewp(self, direction, num):
        self.wp_x = self.wp_x + (self.moves[direction][0] * num)
        self.wp_y = self.wp_y + (self.moves[direction][1] * num)

    def move(self, num):
        self.x = self.x + (self.wp_x * num)
        self.y = self.y + (self.wp_y * num)

    def do(self, instruction, unit):
        if instruction == 'F':
            self.move(unit)
        elif instruction in ['L', 'R']:
            self.rotate(instruction, unit)
        else:
            self.movewp(instruction, unit)


ship = Ship()
for line in sys.stdin:
    instruction = line[0]
    unit = int(line[1:])
    ship.do(instruction, unit)

print(2,abs(ship.x) + abs(ship.y))
