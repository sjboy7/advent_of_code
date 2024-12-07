# spoilers for day 5











import sys
from collections import defaultdict as dd
import functools

rules = []
while True:
    line = sys.stdin.readline()
    if line == '\n':
        break
    rules.append(list(map(int, line.split('|'))))

pages = set()

page_rules = dd(lambda: { '>': set(), '<':set(),})
for a, b in rules:
    page_rules[a]['>'].add(b)
    page_rules[b]['<'].add(a)
    pages |= {a, b}

npages = len(pages)

def page_cmp(a, b):
    assert((a in page_rules[b]['<']) ^ (a in page_rules[b]['>']))
    if a in page_rules[b]['<']:
        return -1
    if a in page_rules[b]['>']:
        return 1
    return 0

total_1 = 0
total_2 = 0
for line in sys.stdin.readlines():
    update = list(map(int, line.split(',')))
    if update == (s := sorted(update, key=functools.cmp_to_key(page_cmp))):
        total_1 += update[len(update)//2]
        pass
    else:
        total_2 += s[len(update)//2]

print(total_1)
print(total_2)