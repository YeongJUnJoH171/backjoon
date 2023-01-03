import sys
import math
N, K = map(int, input().split())
Arr = list(map(int, input().split()))

def sFun(target):
    dis = 0 
    
    avg = sum(target)/len(target)#산술평균
    for z in target:
        dis+=(z-avg)**2
    return dis/len(target)#분산 반환


answer = list()

for i in range (N-K+1):
    for j in range (N-K-i+1):
        target = Arr[i : K+i+j]
        print(target)
        a = sFun(target)
        answer.append(a)

print(math.sqrt(min(answer)))