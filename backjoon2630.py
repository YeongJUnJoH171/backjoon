
###
#8
#1 1 0 0 0 0 1 1
#1 1 0 0 0 0 1 1
#0 0 0 0 1 1 0 0
#0 0 0 0 1 1 0 0
#1 0 0 0 1 1 1 1
#0 1 0 0 1 1 1 1
#0 0 1 1 1 1 1 1
#0 0 1 1 1 1 1 1

### 
import sys

N = int(sys.stdin.readline()) 
Arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [] 


def recursive(x,y,N):
    color = Arr[x][y]
    for i in range (x, x+N):
        for j in range(y, y+N):
            if color != Arr[i][j]:
                recursive(x, y, N//2)
                recursive(x, y + N//2, N//2)
                recursive(x + N//2, y, N//2)
                recursive(x + N//2, y + N//2, N//2)
                return

    if (color ==  0):
        result.append(0)
    else :
        result.append(1)


recursive(0,0,N)
print(result.count(0))
print(result.count(1))
    

    