#!/usr/bin/python3

import sys
import copy

instructions = []
for line in sys.stdin:
    inst = line.rstrip().split(' ')
    instructions.append(inst)

def exec_instructions(instructions):
    acc = 0
    pc = 0
    seen = {}
    while pc < len(instructions):
        if pc in seen:
            return acc

        seen[pc] = 1

        inst = instructions[pc]
        if inst[0] == 'jmp':
            pc = pc + int(inst[1])
            continue
        elif inst[0] == 'acc':
            acc = acc + int(inst[1])
        pc = pc + 1

def mod_instructions(instructions, pos):
    acc = 0
    pc = 0
    seen = {}

    if instructions[pos][0] == 'jmp':
        instructions[pos][0] = 'nop'
    elif instructions[pos][0] == 'nop':
        instructions[pos][0] = 'jmp'

    while pc < len(instructions):
        if pc in seen:
            return None

        seen[pc] = 1

        inst = instructions[pc]
        if inst[0] == 'jmp':
            pc = pc + int(inst[1])
            continue
        elif inst[0] == 'acc':
            acc = acc + int(inst[1])

        pc = pc + 1
    return acc

print(1,exec_instructions(instructions))

for p in range(len(instructions)):
    i = copy.deepcopy(instructions)
    r = mod_instructions(i, p)
    if r is not None:
        print(2,r)
        sys.exit