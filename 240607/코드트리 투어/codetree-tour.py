import heapq
from collections import deque

n = int(input())
cities = []
packages = {} #얘는 딕셔너리


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
        adjacency_list[u].append((v, w))
    
    return adjacency_list


def dijkstra(graph, start, end):
    # 그래프는 인접 리스트 형태로 주어집니다.
    # 예: graph = { 'A': [('B', 1), ('C', 4)], 'B': [('A', 1), ('C', 2), ('D', 5)], ... }
    
    # 초기화
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # 최단 경로 복원
    path, current_node = [], end
    while previous_nodes[current_node] is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.append(start)
    path.reverse()

    return path, distances[end]


def calculate():
    sales = [] #얘를 힙으로
    graph = build_adjacency_list(cities)

    for key in packages:
        pid = packages[key][0]
        rev = packages[key][1]
        d = packages[key][2]
        path, cost = dijkstra(graph, now_s, d)
        if cost == float('inf'):
            heapq.heappush(sales, [101, pid])
        else:
            heapq.heappush(sales, [-(rev-cost), pid])
        # print("path, cost:", path, cost)
    # print(sales)
    return heapq.heappop(sales)



def change_start(s):
    global now_s
    now_s = s

for i in range(n):
    temp = list(map(int, input().split(" ")))
    city_number = 0
    if temp[0] == 100:
        arr = temp[1:]
        city_number = arr[0]
        create(arr)
    elif temp[0] == 200:
        package(temp[1], temp[2], temp[3])
    elif temp[0] == 300:
        delete(temp[1])
    elif temp[0] == 400:
        benefit, pid = calculate()
        if benefit > 0:
            print(-1)
        else:
            print(pid)
            delete(pid)
    elif temp[0] == 500:
        change_start(temp[1])
    # print(packages, now_s)