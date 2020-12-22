#!/usr/bin/python3

import sys, re

def find_paren(items):
    if ')' not in items:
        return None
    close = items.index(')')
    for x in range(close, -1, -1):
        #print (x,items[x])
        if items[x] == '(':
            return(x, close)

def do(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b

def solve(nums):
    items = nums.split(' ')
    total = None
    op = ''
    for n in items:
        if n == '*' or n == '+' or n == '-' or n == '/':
            op = n
        else:
            if total is None:
                total = int(n)
            else:
                total = do(op, total, int(n))
    return total


def process(items):

    p = find_paren(items)
    while p is not None:
        before = p[0]
        after = p[1]

        nitems = items[:before] + str(solve(items[before+1:after])) + items[after+1:]
        items = nitems
        p = find_paren(items)
    return(solve(items))

all = []
for line in sys.stdin:
    line = line.rstrip()
    print(line)
    all.append(process(line))

print(sum(all))