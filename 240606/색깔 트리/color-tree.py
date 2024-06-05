# n = int(input()) # 명령횟수
# node = []


# def node_add(mid, pid, color, max_d): #100
#     # print("노드추가")
#     new_node = [mid, pid, color, max_d]
#     if pid != -1:
#         depth = 1
#         for x in node:
#             if x[0] == pid:
#                 depth += 1
#                 if x[3] < depth:
#                     # print("깊이제한")
#                     return 0

#     node.append(new_node)
#     # return 0


# def change_color(mid, color): #200
#     # print("색깔변경", mid, color)
#     id = mid
#     v = []

#     for x in node:
#         if x[0] == mid: # 루트노드 찾기
#             x[2] = color
#         if x[1] == id: # 자식노드 찾기
#             # print("자식 찾음", x[0])
#             v.append(x[0])
#             x[2] = color
    
#     while(len(v) > 0):
#         id = v.pop()
#         change_color(id, color)
#     # return 0


# def find_color(mid): #300
#     # print("색깔조회")
#     for x in node:
#         if x[0] == mid:
#             return x[2]


# def cal_score(): #400
#     # print("점수확인")
#     score = []
#     def dfs(start, color):
#         # print("start:", start)
#         root = start[0]
#         node_track = []
#         for x in node:
#             # print("root, color 현황:", root, color)
#             if x[1] ==  root:
#                 node_track.append(x)
#                 color.append(x[2])
        
#         if len(node_track) > 0:
#             new = node_track.pop()
#             dfs(new, color)
#         else:
#             # print("color:", color)
#             point = len(set(color))
#             score.append(point**2)
    
#     for i in range(len(node)): 
#         # print(score)
#         dfs(node[i], [node[i][2]])      
#     return sum(score)



# for i in range(n):
#     # print("노드 현황:", node)
#     temp = list(map(int, input().split(" ")))
#     # print(temp)
#     if temp[0] == 100:
#         node_add(temp[1], temp[2], temp[3], temp[4])
#     elif temp[0] == 200:
#         change_color(temp[1], temp[2])
#     elif temp[0] == 300:
#         print(find_color(temp[1]))
#     elif temp[0] == 400:
#         # print("node 현황:", node)
#         print(cal_score())

n = int(input())  # 명령 횟수
node = {}
child_map = {}

def node_add(mid, pid, color, max_d):  # 100
    if pid != -1:
        if pid not in node:
            return
        depth = 1
        curr = pid
        while curr != -1 and depth <= max_d:
            curr = node[curr][1]
            depth += 1
        if depth > max_d:
            return
    node[mid] = [mid, pid, color, max_d]
    if pid != -1:
        if pid not in child_map:
            child_map[pid] = []
        child_map[pid].append(mid)

def change_color(mid, color):  # 200
    stack = [mid]
    while stack:
        curr = stack.pop()
        if curr in node:
            node[curr][2] = color
            if curr in child_map:
                stack.extend(child_map[curr])

def find_color(mid):  # 300
    if mid in node:
        return node[mid][2]
    return None

def cal_score():  # 400
    def dfs(mid):
        stack = [mid]
        colors = set()
        while stack:
            curr = stack.pop()
            if curr in node:
                colors.add(node[curr][2])
                if curr in child_map:
                    stack.extend(child_map[curr])
        return colors

    total_score = 0
    visited = set()
    for mid in node:
        if mid not in visited:
            colors = dfs(mid)
            total_score += len(colors) ** 2
            stack = [mid]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    if curr in child_map:
                        stack.extend(child_map[curr])
    return total_score

for i in range(n):
    temp = list(map(int, input().split(" ")))
    if temp[0] == 100:
        node_add(temp[1], temp[2], temp[3], temp[4])
    elif temp[0] == 200:
        change_color(temp[1], temp[2])
    elif temp[0] == 300:
        print(find_color(temp[1]))
    elif temp[0] == 400:
        print(cal_score())