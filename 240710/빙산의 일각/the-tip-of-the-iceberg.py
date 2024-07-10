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

# 이벤트를 저장할 리스트 (높이, 인덱스)
events = []

# 각 높이에 대해 이벤트 추가
for i in range(N):
    height = Ice[i]
    events.append((height, i))

# 이벤트를 높이 기준으로 내림차순 정렬
events.sort(reverse=True)

# 현재 활성 상태를 저장하는 배열
active = [False] * N
current_islands = 0
max_islands = 0

# 이벤트를 처리하면서 섬의 개수를 계산
for height, index in events:
    if active[index]:  # 이미 활성화된 경우 패스
        continue

    # 현재 얼음을 활성화
    active[index] = True
    
    # 새로운 섬인지 확인
    if (index == 0 or not active[index - 1]) and (index == N - 1 or not active[index + 1]):
        current_islands += 1
    # 기존 섬과 합쳐지는 경우 확인
    if (index > 0 and active[index - 1]) and (index < N - 1 and active[index + 1]):
        current_islands -= 1
    
    # 최대 섬 개수 업데이트
    max_islands = max(max_islands, current_islands)

print(max_islands)