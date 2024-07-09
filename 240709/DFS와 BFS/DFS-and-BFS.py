from collections import deque

N, M, S = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

for row in adj_list:
    row.sort()

vdfs = [0] * (N + 1)
vbfs = [0] * (N + 1)

def dfs(now, path):
    vdfs[now] = 1
    path.append(now)
    for v in adj_list[now]:
        if vdfs[v] == 0:
            dfs(v, path)
    return path

def bfs(start):
    queue = deque([start])
    path = []
    vbfs[start] = 1
    while queue:
        now = queue.popleft()
        path.append(now)
        for v in adj_list[now]:
            if vbfs[v] == 0:
                vbfs[v] = 1
                queue.append(v)
    return path



res_dfs = dfs(S, [])
res_bfs = bfs(S)

print(*res_dfs)
print(*res_bfs)