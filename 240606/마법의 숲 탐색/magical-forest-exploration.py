ip = list(map(int, input().split(" ")))
forest = [[0 for i in range(ip[1])] for j in range(ip[0])]
exit_info = {}
parking_info = {}

def moving_inside(i, res):
    res = res
    x, y = exit_info[i] #[x, y]
    checking = [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]
    for x in checking:
        a, b = x[0], x[1]
        if a >= 0 and a < ip[0] and b >= 0 and b < ip[1]:
            if forest[a][b] > 0  and forest[a][b] != i:
                if forest[a][b] in res:
                    return res
                else:
                    res.append(forest[a][b])
                    moving_inside(forest[a][b], res)
    return res




def putdown(s1, s2, ex, i):
    acc = 0
    flag = True
    now1 = s1
    now2 = s2
    while True:
        if now1 + 2 == ip[0]:
            break
        else:
            if forest[now1+2][now2] == 0:
                now1 += 1
            else:
                break
    while flag:
        # 아래 방향으로 이동할 때 배열 범위 체크
        if now1 + 2 == ip[0]:
            flag = False
            break
        else:
            # 왼쪽 방향 (반시계 90 회전)
            if (now2 - 2 >= 0  and 
                forest[now1][now2 - 2] == 0 and 
                forest[now1 - 1][now2 - 1] == 0 and 
                forest[now1 + 1][now2 - 1] == 0):  
                now2 -= 1
                ex = 3 if ex == 0 else ex - 1
                if (now1 + 2 < ip[0] and
                    forest[now1 + 2][now2] == 0 and 
                    forest[now1 + 1][now2 - 1] == 0):
                    now1 += 1
                    now2 -= 1
                    print("좌로회전")
                    ex = 3 if ex == 0 else ex - 1
                else:
                    flag = False
                    break
            # 오른쪽 방향 (시계 90 회전)
            elif (now2 + 2 < ip[1] and 
                  forest[now1][now2 + 2] == 0 and 
                  forest[now1 - 1][now2 + 1] == 0 and 
                  forest[now1 + 1][now2 + 1] == 0):
                now2 += 1
                ex = 0 if ex == 3 else ex + 1
                if (now1 + 2 < ip[0] and 
                    forest[now1 + 2][now2] == 0 and 
                    forest[now1 + 1][now2 + 1] == 0 ):
                    now1 += 1
                    now2 += 1
                    ex = 0 if ex == 3 else ex + 1
                    print("우로회전")
                else:
                    print("여기니?")
                    flag = False
                    break
            else:
                if now1 - 1 < 0:
                    print("진입불가 리셋")
                    return 0
                print("양쪽으로도 회전 불가")
                flag = False
                break

    acc += now1+2
    forest[now1][now2] = i
    forest[now1 - 1][now2] = i
    forest[now1 + 1][now2] = i
    forest[now1][now2 - 1] = i
    forest[now1][now2 + 1] = i
    door = [[now1-1, now2], [now1, now2+1], [now1+1, now2], [now1, now2-1]]
    forest[door[ex][0]][door[ex][1]] = -i # 출구표시

    exit_info[i] = [door[ex][0],door[ex][1]] # 출구 메모
    parking_info[i] = [[now1, now2], [now1-1, now2], [now1, now2+1], [now1+1, now2], [now1, now2-1]]
    ret = set(moving_inside(i, []))  # 갈수있는 골렘 번호
    # print(parking_info)
    if len(ret) > 0:
        mx = 0
        for i in ret:
            if mx <  max(parking_info[i][0]):
                mx = max(parking_info[i][0])
        return mx + 2
    else:
        return acc


score = 0
for i in range(ip[2]):
    print(i+1, "번째")
    comm = list(map(int, input().split(" ")))
    res = putdown(-2, comm[0] - 1, comm[1], i+1)
    print("res:", res)
    if res == 0: #reset 
        forest = [[0 for i in range(ip[1])] for j in range(ip[0])]
        parking_info = {}
        exit_info = {}
    else:
        score += res
    
print(score)