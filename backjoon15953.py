import sys

N = int(sys.stdin.readline()) 
Arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def fest1(x):
    if (x == 1):
        return 5000000
    elif ( 1 < x <=3):
        return 3000000
    elif (3 < x <= 6):
        return 2000000
    elif ( 6 < x <= 10):
        return 500000
    elif ( 10 < x <= 15):
        return 300000
    elif ( 15 < x <= 21):
        return 100000
    else:
        return 0; 

def fest2(y):
    if (y == 1):
        return 5120000
    elif ( 1 < y <=3):
        return 2560000
    elif (3 < y <= 7):
        return 1280000
    elif ( 7 < y <= 15):
        return 640000
    elif ( 15 < y <= 31):
        return 320000
    else:
        return 0;

    
for i in range(N):
    x = Arr[i][0]  
    y = Arr[i][1]
    print(fest1(x) + fest2(y))


            