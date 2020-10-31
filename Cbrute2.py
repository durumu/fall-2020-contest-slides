if survive(-1):
    print('fine')
else:
    for i in range(1,n+1):
        if survive(i):
            print('shoot',i)
            exit()
    print('hopeless')
