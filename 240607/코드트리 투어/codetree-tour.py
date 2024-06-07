# import heapq
# from collections import deque

# n = int(input())
# cities = []
# packages = {} #얘는 딕셔너리
# city_number = 0
# now_s = 0
# sales = [] #얘를 힙으로
# starts = [0]

# def create(arr):
#     c = arr[0]
#     v = arr[1]
#     info = arr[2:]
#     for i in range(v):
#         cities.append(info[i*3:(i+1)*3])
    

# def package(cid, rev, dest):
#     packages[cid] = [cid, rev, dest]

# def delete(cid):
#     if cid in packages:
#         del packages[cid]

# def build_adjacency_list(arr):
#     # 모든 노드에 대해 빈 리스트를 초기화합니다.
#     adjacency_list = {}
#     # print("vertex 배열 길이:", arr[0]*3)
#     for i in range(1, len(arr[1:]), 3):
#         # print(i, arr[i], arr[i+1], arr[i+2])
#         u, v, w = arr[i], arr[i+1], arr[i+2]
#         if u not in adjacency_list:
#             adjacency_list[u] = []

#         if v not in adjacency_list:
#             adjacency_list[v] = []
    
#         if adjacency_list[u] == (v, w):
#             continue
#         else:
#             adjacency_list[u].append((v, w))
#             if u == v : 
#                 continue
#             else:
#                 adjacency_list[v].append((u, w))
    
#     return adjacency_list

# def dijkstra(graph, start, target):
#     # 최단 거리 테이블 무한으로 초기화\
#     # print("city number:", city_number)
#     distances = [float('inf')] * city_number
#     distances[start] = 0

#     # 우선순위 큐
#     priority_queue = [(0, start)]
    
#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)
        
#         # 현재 노드가 목적지 노드이면 종료
#         if current_node == target:
#             return distances[current_node]
        
#         # 현재 노드가 처리된 적이 있다면 무시
#         if current_distance > distances[current_node]:
#             continue
        
#         # 인접한 노드들에 대해 거리 계산
#         for neighbor, weight in graph[current_node]:
#             # print("now neighbor:", neighbor)
#             distance = current_distance + weight
#             # 더 짧은 경로를 발견한 경우
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))
                
#                 # 자기 자신으로 가는 간선인 경우 별도로 업데이트
#                 if neighbor == current_node and distance < distances[current_node]:
#                     distances[current_node] = distance
    
#     # 목적지까지의 경로가 없는 경우
#     return distances[target]


# def calculate(graph, s):
#     if s in starts:
#         for x in sales:
#             if x[2] == s:
#                 return heapq.heappop(sales)
#             else:
#                 return 101, -1
#     else:
#         for key in packages:
#             pid, rev, d = packages[key]
#             cost = dijkstra(graph, now_s, d)
#             if cost == float('inf'):
#                 heapq.heappush(sales, [101, pid, s])
#             else:
#                 heapq.heappush(sales, [-(rev-cost), pid, s])
#         if len(sales) == 0:
#             return 101, -1
#         return heapq.heappop(sales)



# def change_start(s):
#     global now_s
#     now_s = s
#     starts.append(s)

# def put_cn(n):
#     global city_number
#     city_number = n

# for i in range(n):
#     temp = list(map(int, input().split(" ")))
#     if temp[0] == 100:
#         arr = temp[2:]
#         put_cn(temp[1])
#         graph = build_adjacency_list(arr)
#         # print(graph)
        
#     elif temp[0] == 200:
#         package(temp[1], temp[2], temp[3])
#     elif temp[0] == 300:
#         delete(temp[1])
#     elif temp[0] == 400:
#         benefit, pid = calculate(graph, now_s)
#         if benefit > 0:
#             print(-1)
#         else:
#             print(pid)
#             delete(pid)
#     elif temp[0] == 500:
#         change_start(temp[1])
#     # print(packages, now_s)
import heapq
import sys

INF = float('inf')  # 무한대 값을 정의합니다.
MAX_N = 2000  # 코드트리 랜드의 최대 도시 개수입니다.
MAX_ID = 30005  # 여행상품 ID의 최대값입니다.

# 입력을 빠르게 받기 위한 설정입니다.
input = sys.stdin.readline

N, M = 0, 0  # 도시의 개수 N과 간선의 개수 M을 초기화합니다.
A = []  # 코드트리 랜드의 간선을 인접 행렬로 저장합니다.
D = []  # 다익스트라 알고리즘을 통해 시작도시부터 각 도시까지의 최단경로를 저장합니다.
isMade = [] # 여행상품이 만들어진적 있는지 저장합니다.
isCancel = []  # 여행상품이 취소되었는지 저장합니다.
S = 0  # 여행 상품의 출발지입니다.

# 여행 상품을 정의합니다
class Package:
    def __init__(self, id, revenue, dest, profit):
        self.id = id #고유 식별자 ID
        self.revenue = revenue # 매출
        self.dest = dest # 도착도시
        self.profit = profit # 여행사가 벌어들이는 수익
        
    def __lt__(self, other):
        # 우선순위 큐 정렬 기준을 정의합니다.
        if self.profit == other.profit:
            return self.id < other.id # profit이 같으면 id가 작은 순으로
        return self.profit > other.profit # profit이 클수록 우선 순위 높게

pq = []  # 우선순위 큐 초기화

# dijkstra 알고리즘을 통해 시작도시 S에서 각 도시로 가는 최단거리를 구합니다.
def dijkstra():
    global D
    D = [INF] * N
    visit = [False] * N
    D[S] = 0
    
    for _ in range(N):
        v = -1
        minDist = INF
        for j in range(N):
            if not visit[j] and minDist > D[j]:
                v = j
                minDist = D[j]
        if v == -1:
            break
        visit[v] = True
        for j in range(N):
            if A[v][j] != INF and D[j] > D[v] + A[v][j]:
                D[j] = D[v] + A[v][j]

# 코드트리랜드를 입력받고
# 주어진 코드트리 랜드를 인접행렬에 저장합니다
def buildLand(n, m, arr):
    global A, N, M
    N, M = n, m
    A = [[INF]*N for _ in range(N)]
    for i in range(N):
        A[i][i] = 0  # 도시 자신에게 가는 비용은 0입니다.
    for i in range(M):
        u, v, w = arr[i*3], arr[i*3+1], arr[i*3+2]
        # 양방향 간선에 대해 두 도시간 여러 간선이 주어질 수 있으므로 min 값으로 저장합니다
        A[u][v] = min(A[u][v], w)
        A[v][u] = min(A[v][u], w)

# 여행 상품을 추가합니다
# 추가된 여행상품은 priority queue안에도 들어가야합니다.
def addPackage(id, revenue, dest):
    isMade[id] = True;
    profit = revenue - D[dest]
    heapq.heappush(pq, Package(id, revenue, dest, profit))

# id에 해당하는 여행상품이 취소되었음을 기록합니다
def cancelPackage(id):
    # 만들어진적 있는 여행상품에 대해서만 취소할 수 있습니다.
    if isMade[id]:
        isCancel[id] = True

# 최적의 여행상품을 판매합니다
def sellPackage():
    while pq:
        p = pq[0]
        # 최적이라고 생각한 여행 상품이 판매 불가능 하다면 while문을 빠져나가 -1을 반환합니다.
        if p.profit < 0:
            break
        heapq.heappop(pq)
        if not isCancel[p.id]:
            return p.id # 해당 여행 상품이 취소되지 않았다면 정상 판매되므로 id를 반환합니다
    return -1

# 변경할 시작도시를 입력받고 변경됨에 따른 기존 여행상품 정보들을 수정합니다.
def changeStart(param):
    global S
    S = param
    dijkstra()  # 새로운 출발지에 대해 다익스트라 알고리즘을 다시 실행합니다.
    temp_packages = []
    # 기존의 여행상품들을 packages에 기록하며 priority queue에서 삭제합니다
    while pq:
        temp_packages.append(heapq.heappop(pq))
    # 기존의 여행 상품들의 profit을 수정하여 새로이 priority queue에 넣습니다
    for p in temp_packages:
        addPackage(p.id, p.revenue, p.dest)

def main():
    global isCancel, isMade
    Q = int(input())
    isMade = [False] * MAX_ID # 여행상품 생성 전적 상태 배열 초기화
    isCancel = [False] * MAX_ID  # 여행상품 취소 상태 배열 초기화
    # 총 Q개의 쿼리를 입력받습니다
    for _ in range(Q):
        query = list(map(int, input().split()))
        T = query[0]
        
        # 쿼리의 종류에 따라 필요한 함수들을 호출하여 처리합니다
        if T == 100:
            buildLand(query[1], query[2], query[3:])
            dijkstra()
        elif T == 200:
            id, revenue, dest = query[1], query[2], query[3]
            addPackage(id, revenue, dest)
        elif T == 300:
            id = query[1]
            cancelPackage(id)
        elif T == 400:
            print(sellPackage())
        elif T == 500:
            changeStart(query[1])

if __name__ == "__main__":
    main()