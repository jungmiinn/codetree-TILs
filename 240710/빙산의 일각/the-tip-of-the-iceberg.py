# N = int(input())
# Ice = [int(input()) for _ in range(N)]

# def counting(arr):
#     cnt = 0
#     for i in range(N-1):
#         if arr[i] <= 0 and arr[i+1] > 0:
#             cnt += 1

#     if arr[0] > 0:
#         cnt += 1
#     return cnt

# # 초기 섬의 개수 계산
# newIce = Ice[:]
# current_islands = counting(newIce)
# max_islands = current_islands

# # 모든 얼음의 높이를 한 번에 1씩 감소시키며 섬의 개수를 계산
# for i in range(1, max(Ice) + 1):
#     for j in range(N):
#         newIce[j] -= 1

#     # 각 높이에서 섬의 개수 업데이트
#     current_islands = counting(newIce)
#     max_islands = max(max_islands, current_islands)

# print(max_islands)

N = int(input())
Ice = [int(input()) for _ in range(N)]

# 각 높이에 대해 시작과 끝을 저장할 리스트
events = []

# 각 위치의 높이에 대해 시작과 끝 이벤트 추가
for i in range(N):
    height = Ice[i]
    events.append((height, i, 1))  # 높이, 인덱스, 시작 이벤트
    events.append((0, i, -1))      # 높이가 0이 되는 시점, 인덱스, 끝 이벤트

# 이벤트를 높이 기준으로 정렬
events.sort(reverse=True)

max_islands = 0
current_islands = 0
active = [0] * N  # 현재 활성 상태를 저장하는 배열

# 이벤트를 처리
for height, index, typ in events:
    if typ == 1:  # 시작 이벤트
        active[index] = 1
        if (index == 0 or active[index - 1] == 0) and (index == N - 1 or active[index + 1] == 0):
            current_islands += 1
        if (index > 0 and active[index - 1] == 1) and (index < N - 1 and active[index + 1] == 1):
            current_islands -= 1
    else:  # 끝 이벤트
        if active[index] == 1:
            active[index] = 0
            if (index == 0 or active[index - 1] == 0) and (index == N - 1 or active[index + 1] == 0):
                current_islands -= 1
            if (index > 0 and active[index - 1] == 1) and (index < N - 1 and active[index + 1] == 1):
                current_islands += 1

    max_islands = max(max_islands, current_islands)

print(max_islands)