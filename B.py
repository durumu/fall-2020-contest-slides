from string import ascii_uppercase
letters = set('BCDFGHJKLMNPRSTVWXYZ')
numbers = set('0123456789')
match = [letters]*3 + [set('-')] + [numbers]*4

n = int(input())
for _ in range(n):
    plate = input().strip()
    if len(plate) != 8:
        print('NO')
        continue
    for char, match_set in zip(plate, match):
        if char not in match_set:
            print('NO')
            break
    else:
        print('YES')