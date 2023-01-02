
import sys

N = int(input()) 
Arr = [list(map(int, input())) for _ in range(N)]
#result = [] 

def recursive(x,y,N):
    color = Arr[x][y]
    for i in range (x, x+N):
        for j in range(y, y+N):
            if color != Arr[i][j]:
                print("(", end='')
                recursive(x, y, N//2)
                recursive(x, y + N//2, N//2)
                recursive(x + N//2, y, N//2)
                recursive(x + N//2, y + N//2, N//2)
                print(")", end='')
                return

    if color == 0:
        print(0, end='')
    else :
        print(1, end='')


recursive(0,0,N)

