legend = {
    '.' : 'grass',
    '#' : 'city',
    'M' : 'mountain',
    'T' : 'tree'
}

n = int(input())
A = [input() for _ in range(n)]

rot, mirror = 0, 0
