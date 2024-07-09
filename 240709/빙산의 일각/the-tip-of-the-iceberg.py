N = int(input())
Ice = [int(input()) for _ in range(N)]

maxH = max(Ice)

def counting(arr):
    cnt = 0
    for i in range(N-1):
        if (arr[i] > 0 and arr[i+1] < 0) or (arr[i] < 0 and arr[i+1] > 0):
            cnt += 1
    return cnt

for i in range(1, maxH+1):
    newIce = Ice[:]
    for j in range(N):
        newIce[j] -= j
    print(newIce)
    #print(counting(newIce))