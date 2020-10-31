for _ in range(int(input())):
    command = input()
    if command in ['clockwise', 'counterclockwise']:
        if (command == 'counterclockwise') ^ mirror:
            rot = (rot + 1) % 4  # CCW, or mirrored CW
        else:
            rot = (rot + 3) % 4  # CW, or mirrored CCW
    elif command in ['flip', 'mirror']:
        mirror ^= 1
        if command == 'flip':
            rot = (rot + 2) % 4
    else:
        i, j = map(int, command.split()[1:])
        if mirror:
            j = n - j - 1
        for _ in range(rot):
            i, j = j, n - i - 1
        print(legend[A[i][j]])
