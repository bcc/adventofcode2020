#!/usr/bin/python3

import sys, re

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def process_rules(rules, id):
    rule = rules[id]
    check = rule.split(" ")
    r = "("
    p = ""
    q = ""
    for c in check:
        if is_integer(c):
            r += process_rules(rules, c)
        elif c == '"a"':
            r += "a"
        elif c == '"b"':
            r += "b"
        elif c == '|':
            r += "|"
    r += p
    r += ")" 
    r += q

    return r

def process_rules2(rules, id):
    rule = rules[id]
    check = rule.split(" ")
    r = "("
    p = ""
    q = ""
    for c in check:
        if is_integer(c):
            if id == "8":
                return "(" + process_rules2(rules, "42" ) + ")+"
            elif id == "11":
                x = []
                for t in range(1,15):
                    x.append("(" + process_rules2(rules, "42" )+"{" + str(t) + "}" +  process_rules(rules, "31" ) + "{" + str(t) + "}"+ ")")

                return  "(" +  "|".join(x) + ")"
            else:
                r += process_rules2(rules, c)
        elif c == '"a"':
            r += "a"
        elif c == '"b"':
            r += "b"
        elif c == '|':
            r += "|"
    r += p
    r += ")" 
    r += q

    return r


rules = {}
r = r2 = ""
count = count2 = 0
for line in sys.stdin:
    line = line.rstrip()

    m = re.match(r'^(\d+): (.*?)$', line)
    if m is not None:
        id = m.group(1)
        rule = m.group(2)
        rules[id] = rule
        continue

    if line == "":
        r = "^" + process_rules(rules, "0") + "$"
        r2 = "^" + process_rules2(rules, "0") + "$"

    m = re.match(r'^([ab]+)$', line)
    if m is not None:
        check = re.match(r, m.group(1))
        if check is not None:
            count += 1

        check2 = re.match(r2, m.group(1))
        if check2 is not None:
            count2 += 1

print(1, count)
print(2, count2)