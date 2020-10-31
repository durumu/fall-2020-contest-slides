from collections import defaultdict

apprentices = defaultdict(list)

for _ in range(int(input())):
    apprentice, master = input().split()
    apprentices[master].append(apprentice)

for _ in range(int(input())):
    master = input().strip()
    print(*sorted(apprentices[master]))