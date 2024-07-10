N = int(input())
Ice = [int(input()) for _ in range(N)]

maxH = max(Ice)

def counting(arr):
    cnt = 0
    for i in range(N-1):
        if arr[i] <= 0 and arr[i+1] > 0:
            cnt += 1

    if arr[0] > 0:
        cnt += 1
    return cnt


save = []
newIce = Ice[:]
for i in range(1, maxH+1):
    for j in range(N):
        newIce[j] -= 1
    save.append(counting(newIce))

print(max(save))