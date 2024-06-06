import heapq
from collections import deque

n = int(input())
cities = []
packages = {} #얘는 딕셔너리
city_number = 0
now_s = 0

def create(arr):
    c = arr[0]
    v = arr[1]
    info = arr[2:]
    for i in range(v):
        cities.append(info[i*3:(i+1)*3])
    

def package(cid, rev, dest):
    packages[cid] = [cid, rev, dest]

def delete(cid):
    if cid in packages:
        del packages[cid]

def build_adjacency_list(edges):
    # 모든 노드에 대해 빈 리스트를 초기화합니다.
    adjacency_list = {}
    for u, v, w in edges:
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
    
    # 엣지를 추가합니다.
    for u, v, w in edges:
        if adjacency_list[u] in (v, w):
            continue
        else:
            adjacency_list[u].append((v, w))
            if u == v : 
                continue
            else:
                adjacency_list[v].append((u, w))
    
    return adjacency_list

def dijkstra(graph, start, target):
    # 최단 거리 테이블 무한으로 초기화
    distances = [float('inf')] *city_number
    distances[start] = 0

    # 우선순위 큐
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 현재 노드가 목적지 노드이면 종료
        if current_node == target:
            return distances[current_node]
        
        # 현재 노드가 처리된 적이 있다면 무시
        if current_distance > distances[current_node]:
            continue
        
        # 인접한 노드들에 대해 거리 계산
        for neighbor, weight in graph[current_node]:
            # print("now neighbor:", neighbor)
            distance = current_distance + weight
            # 더 짧은 경로를 발견한 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
                # 자기 자신으로 가는 간선인 경우 별도로 업데이트
                if neighbor == current_node and distance < distances[current_node]:
                    distances[current_node] = distance
    
    # 목적지까지의 경로가 없는 경우
    return distances[target]


def calculate(graph):
    sales = [] #얘를 힙으로
    
    for key in packages:
        pid, rev, d = packages[key]
        cost = dijkstra(graph, now_s, d)
        if cost == float('inf'):
            heapq.heappush(sales, [101, pid])
        else:
            heapq.heappush(sales, [-(rev-cost), pid])
    if len(sales) == 0:
        return 101, -1
    return heapq.heappop(sales)



def change_start(s):
    global now_s
    now_s = s

for i in range(n):
    temp = list(map(int, input().split(" ")))
    if temp[0] == 100:
        arr = temp[1:]
        city_number = arr[0]
        create(arr)
        graph = build_adjacency_list(cities)
        
    elif temp[0] == 200:
        package(temp[1], temp[2], temp[3])
    elif temp[0] == 300:
        delete(temp[1])
    elif temp[0] == 400:
        # print(graph)
        benefit, pid = calculate(graph)
        if benefit > 0:
            print(-1)
        else:
            print(pid)
            delete(pid)
    elif temp[0] == 500:
        change_start(temp[1])
    # print(packages, now_s)