N = int(input())
Ice = [int(input()) for _ in range(N)]

def counting(arr):
    cnt = 0
    for i in range(N-1):
        if arr[i] <= 0 and arr[i+1] > 0:
            cnt += 1

    if arr[0] > 0:
        cnt += 1
    return cnt

# 초기 섬의 개수 계산
newIce = Ice[:]
current_islands = counting(newIce)
max_islands = current_islands

# 모든 얼음의 높이를 한 번에 1씩 감소시키며 섬의 개수를 계산
for i in range(1, max(Ice) + 1):
    for j in range(N):
        newIce[j] -= 1

    # 각 높이에서 섬의 개수 업데이트
    current_islands = counting(newIce)
    max_islands = max(max_islands, current_islands)

print(max_islands)