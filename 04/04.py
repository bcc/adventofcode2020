#!/usr/bin/python3

import sys
import re

def process1(passport):
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
        print ('valid', len(passport))
        return 1
    return 0

def check_match(passport, k, m):
    if k in passport:
        n = re.match(m, passport[k])
        if n is not None:
            return n.group(0)
        else:
            return None
    else:
        return None

def check_between(n, min, max):
    if n is None:
        return False
    i = int(n)
    if i < min:
        return False
    if i > max: 
        return False
    return True

def process2(passport):
    print(passport)
#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    v = check_match(passport, 'byr', r'^\d+$')
    if not check_between(v, 1920,2020):
        return 0

#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    v = check_match(passport, 'iyr', r'^\d+$')
    if not check_between(v, 2010,2020):
        return 0

#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    v = check_match(passport, 'eyr', r'^\d+$')
    if not check_between(v, 2020,2030):
        return 0

#    hgt (Height) - a number followed by either cm or in:
#        If cm, the number must be at least 150 and at most 193.
#        If in, the number must be at least 59 and at most 76.
    if 'hgt' in passport:
        m = re.match(r'^(\d+)(cm|in)$', passport['hgt'])
        if m is None:
            return 0
        vh = 0
        if m.group(2) == 'cm':
            vh = 1
            if not check_between(m.group(1), 150,193):
                return 0
        if m.group(2) == 'in':
            vh = 1
            if not check_between(m.group(1), 59,76):
                return 0
        if vh == 0:
            return 0
    else:
        return 0

#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    v = check_match(passport, 'hcl', r'^#[0-9a-f]{6}$')
    if v is None:
        return 0

#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    v = check_match(passport, 'ecl', r'^(amb|blu|brn|gry|grn|hzl|oth)$')
    if v is None:
        return 0

#    pid (Passport ID) - a nine-digit number, including leading zeroes.
    v = check_match(passport, 'pid', r'^\d{9}$')
    if v is None:
        return 0

#    cid (Country ID) - ignored, missing or not.

    return 1

validcount1 = 0
validcount2 = 0
passport = {}
for line in sys.stdin:
    if line == "\n":
        validcount1 = validcount1 + process1(passport)
        validcount2 = validcount2 + process2(passport)
        passport = {}
        continue
    items = line.rstrip().split(' ')
    for item in items:
        (tag, data) = item.split(':')
        passport[tag] = data
validcount1 = validcount1 + process1(passport)
validcount2 = validcount2 + process2(passport)

print(1, validcount1)
print(2, validcount2)