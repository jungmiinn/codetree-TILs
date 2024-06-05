ip = list(map(int, input().split(" ")))
forest = [[0 for i in range(ip[1])] for j in range(ip[0])]

def moving_inside(e1, e2, i):
    # exit = [[e1-1, e2], [e1, e2+1], [e1+1, e2], [e1, e2-1]]
    # ex1, ex2 = exit[ex][0], exit[ex][1]
    def connected_g(nowg):

        dirc = [[e1-1, e2], [e1, e2+1], [e1+1, e2], [e1, e2-1]]
        av = [] # 이동가능한 골렘 번호

        for x in dirc:
            if forest[x[0]][x[1]] > 0 and forest[x[0]][x[1]] != i:
                av.append(forest[x[0]][x[1]])

    if len(av) == 0:
        return 0
    else:
        for g in av:
            nowg = g
            for a in range(ip[0]):
                for b in range(ip[1]):
                    if forest[a][b] == -nowg

    

def putdown(s1, s2, ex, i):
    acc = 0
    flag = True
    now1 = s1
    now2 = s2
    
    while flag:
        # 아래 방향으로 이동할 때 배열 범위 체크
        if now1 + 1 >= ip[0]-1:
            print("stop1")
            flag = False
            break
        
        if (now1 + 2 < ip[0] and
            forest[now1 + 2][now2] == 0 and 
            forest[now1 + 1][now2 - 1] == 0 and 
            forest[now1 + 1][now2 + 1] == 0):  # 아래방향
            now1 += 1
        else:
            # 왼쪽 방향 (반시계 90 회전)
            if (now2 - 2 >= 0  and 
                forest[now1][now2 - 2] == 0 and 
                forest[now1 - 1][now2 - 1] == 0 and 
                forest[now1 + 1][now2 - 1] == 0):  
                now2 -= 1
                if (now1 + 2 < ip[0] and
                    forest[now1 + 2][now2] == 0 and 
                    forest[now1 + 1][now2 - 1] == 0):
                    now1 += 1
                    now2 -= 1
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
                if (now1 + 2 < ip[0] and 
                    forest[now1 + 2][now2] == 0 and 
                    forest[now1 + 1][now2 + 1] == 0 ):
                    now1 += 1
                    now2 += 1
                    ex = 0 if ex == 3 else ex + 1
                else:
                    flag = False
                    break
            else:
                if now1 - 1 < 0:
                    return 0

                flag = False
                break
    
    acc += now1+2
    forest[now1][now2] = i
    forest[now1 - 1][now2] = i
    forest[now1 + 1][now2] = i
    forest[now1][now2 - 1] = i
    forest[now1][now2 + 1] = i
    door = [[now1-1][now2], [now1][now2+1], [now1+1][now2], [now1][now2-1]]
    forest[door[ex][0]][door[ex][1]] = -i # 출구표시
    moving_inside(door[ex][0], door[ex][1], i)  # 출구랑 몇 번째 골렘인지

    return acc


score = 0
for i in range(ip[2]):
    comm = list(map(int, input().split(" ")))
    res = putdown(-2, comm[0] - 1, comm[1], i)
    print("res:", res)
    if res == 0:
        forest = [[0 for i in range(ip[1])] for j in range(ip[0])]
    else:
        score += res