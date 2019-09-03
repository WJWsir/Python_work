space = ' '
for i in range(1,10):
    for j in range(1,i):
        print('%8s' % ' ',sep = ' ',end = ' ')  
    for j in range(i,10):
        print('%-2d*%2d=%2d' %(i,j,i*j),sep = ' ',end = ' ')
    print()
