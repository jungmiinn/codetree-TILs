import heapq

N = M = P = C = D = 0

temp = list(map(int, input().split(" ")))


N, M, P, C, D = temp
r = list(map(int, input().split(" "))) # 초기 루 위치
game = [[0 for _ in range(N)] for _ in range(N)]
rx, ry = r[0]-1, r[1]-1 # 루 위치 
game[rx][ry] = 31 # 루돌프는 31번

P_arr = [[0, 0] for _ in range(31)] # 산타 위치 저장할 배열 초기화 () out = -1, -1
s_score = [0] * 31 # 산타 점수 저장 1차원으로 그냥 산타 번호에 더하면 될듯
P_number = [] # 산타 번호 저장
faint_P = [[] for _ in range(M)] # 매턴 기절 산타 저장
out_P = [] # 죽은 산타 저장;;;;;


for _ in range(P):
    ip = list(map(int, input().split(" ")))
    P_arr[ip[0]] = [ip[1]-1, ip[2]-1]
    game[ip[1]-1][ip[2]-1] = ip[0] # game 판에 산타 번호로 저장
    P_number.append(ip[0])
    
P_number.sort()

def r_moving(t, r1, r2):
    dis = []
    for i in P_number:
        if i not in out_P:
            cal = (r1-(P_arr[i][0]))**2 + (r2-(P_arr[i][1]))**2
            heapq.heappush(dis, [cal, -(P_arr[i][0]), -(P_arr[i][1]), i]) # 거리, 좌표, 산타번호
    # print("heap:", dis)
    res = heapq.heappop(dis)

    santa_n = res[3] # 선택된 산타 번호
    s1, s2 = -res[1], -res[2] # 선택된 산타 좌표
    # print("선택된 산타:", res[3])

    dirc = [[r1-1, r2], [r1-1, r2+1], [r1, r2+1], [r1+1, r2+1], [r1+1, r2], [r1+1, r2-1], [r1, r2-1], [r1-1, r2-1]]
    mi = 2*(N**2) # 최대값으로 초기화
    di = 0 # 어느방향인지 저장
    nr1 = nr2 = nd = -1
    for d in dirc: # 8방향 돌면서 확인 
        if d[0] >= 0 and d[0] < N and d[1] >= 0 and d[1] < N:
            if mi > ((s1-d[0])**2) + ((s2-d[1])**2): # 최소방향 확인
                mi = ((s1-d[0])**2) + ((s2-d[1])**2)
                nr1, nr2 = d[0], d[1]
                nd = di
        di += 1

    game[r1][r2] = 0
    game[nr1][nr2] = 31 # 게임상 좌표에 루돌프 옮겨주기
    global rx, ry
    rx, ry = nr1, nr2 # 현재위치 갱신
    if mi == 0: # 산타랑 충돌하는 경우
        faint_P[t].append(santa_n) # 기절산타 저장
        crushingRtoS(nr1, nr2, nd, santa_n)


def s_moving(t):
    for i in P_number:
        if i not in out_P and i not in faint_P[t-1] and i not in faint_P[t]: # 아웃 아니고 기절 아닌 산타
            s1, s2 = P_arr[i][0], P_arr[i][1] # 움직일수있는 현재산타의 좌표
            # print("현재 이동 가능한 산타", i)
            dirc = [[s1-1, s2], [], [s1, s2+1], [], [s1+1, s2], [], [s1, s2-1]]
            nowd = (rx-s1)**2 + (ry-s2)**2 # 현재 산타-루돌프 거리
            flag = -1
            crushed = 0
            closest = float('inf')
            for j in [0, 2, 4, 6]:
                if dirc[j][0] >= 0 and dirc[j][0] < N and dirc[j][1] >= 0 and dirc[j][1] < N:  # 범위안에 있는 좌표
                    if game[dirc[j][0]][dirc[j][1]] == 31: # 1칸 이내에 루돌프가 있음   
                        # print("한칸 이내에 루돌프가 있음")
                        game[s1][s2] = 0
                        crushingStoR(dirc[j][0], dirc[j][1], i, j, t) #루돌프랑 박치기 !!!!
                        crushed = 1
                        
            if crushed == 0:
                #루돌프없음
                for k in [0, 2, 4, 6]:
                    if dirc[k][0] >= 0  and dirc[k][0] < N and dirc[k][1] >= 0  and dirc[k][1] < N: # 범위안
                        if game[dirc[k][0]][dirc[k][1]] == 0: #비어잇음
                            temp = (rx-dirc[k][0])**2 + (ry-dirc[k][1])**2 # dir 산타-루돌프 거리
                            if nowd > temp: # 가까워진다?
                                nowd = temp
                                flag = k
                
                if flag != -1:
                    game[s1][s2] = 0 # 현재 좌표 0으로 수정
                    game[dirc[flag][0]][dirc[flag][1]] = i # 옮겨주고
                    P_arr[i] = [dirc[flag][0],dirc[flag][1]] # 산타현재위치 바꿔주고
                        
                



def crushingStoR(p1, p2, n, d, t):
    # 좌표, 산타번호, 방향
    # print(n, "산타가" ,p1, p2, "로 튕겨짐", d, "방향으로", D, "만큼")
    
    s_score[n] += D # 산타 점수 획득
    faint_P[t].append(n)
    dirc = [[p1+D, p2], [], [p1, p2-D], [], [p1-D, p2], [], [p1, p2+D]]
    np1, np2 = dirc[d] #튕겨져 나간 목적지

    if d == 0:
        d = 4
    elif d == 2:
        d = 6
    elif d == 4:
        d = 0
    elif d == 6:
        d = 2

    if np1 >= N or np1 < 0 or np2 >= N or np2 < 0: # 밀려난 산타가 아웃되는 경우
        # game[p1][p2] = 0
        out_P.append(n)
        P_arr[n] = [-1, -1]
        return None


    if game[np1][np2] > 0: # 밀려나는 자리에 다른 산타가 있는 경우
       #튕겨온 산타 정보 갱신
       oldn = game[np1][np2] # 이미 있던 산타번호 저장하고
       game[np1][np2] = n # 게임판에 뉴 산타 번호 넣고
       P_arr[n] = [np1,np2] # 산타 위치 저장 배열 정보 갱신하고
       crushingStoS(oldn, d, np1, np2) # 산타한테 충돌당한 산타 정보, 방향, 좌표

    else:
        # game[p1][p2] = 0
        game[np1][np2] = n # 게임판에 뉴 산타 번호 넣고
        P_arr[n] = [np1,np2] # 산타 위치 저장 배열 정보 갱신하고

def crushingRtoS(p1, p2, d, n): # 루돌프 에게서 튕겨진 산타 정보
    # print(n, "산타가" ,p1, p2, "로 튕겨짐", d, "방향으로", C, "만큼")
    
    s_score[n] += C # 산타 점수 획득

    dirc = [[p1-C, p2], [p1-C, p2+C], [p1, p2+C], [p1+C, p2+C], [p1+C, p2], [p1+C, p2-C], [p1, p2-C], [p1-C, p2-C]]
    
    if dirc[d][0] >= N or dirc[d][0] < 0 or dirc[d][1] >= N or dirc[d][1] < 0: # 밀려난 산타가 아웃되는 경우
        # game[p1][p2] = 0
        out_P.append(n)
        return


    if game[dirc[d][0]][dirc[d][1]] > 0: # 밀려나는 자리에 다른 산타가 있는 경우
       #튕겨온 산타 정보 갱신
       oldn = game[dirc[d][0]][dirc[d][1]] # 이미 있던 산타번호 저장하고
       game[dirc[d][0]][dirc[d][1]] = n # 게임판에 뉴 산타 번호 넣고
       P_arr[n] = [dirc[d][0],dirc[d][1]] # 산타 위치 저장 배열 정보 갱신하고
       crushingStoS(oldn, d, dirc[d][0], dirc[d][1]) # 산타한테 충돌당한 산타 정보, 방향, 좌표

    else:
        game[dirc[d][0]][dirc[d][1]] = n # 게임판에 뉴 산타 번호 넣고
        P_arr[n] = [dirc[d][0],dirc[d][1]] # 산타 위치 저장 배열 정보 갱신하고
    
    
def crushingStoS(n, d, x, y):
    
    # print("산타에게서 밀려난", n,"번 산타")
    dirc = [[x-1, y], [x-1, y+1], [x, y+1], [x+1, y+1], [x+1, y], [x+1, y-1], [x, y-1], [x-1, y-1]]
    nx, ny = dirc[d][0], dirc[d][1] # 밀려날 새로운 좌표


    if nx >= N or nx < 0 or ny >= N or ny < 0: # 밀려난 산타가 아웃되는 경우
        out_P.append(n)
        return None

    if game[nx][ny] > 0: # 산타있음
        oldn = game[nx][ny] # 기존 산타번호 저장
        game[nx][ny] = n # 게임판에 뉴 산타 번호 넣고
        P_arr[n] = [nx, ny] # 산타 위치 저장 배열 정보 갱신하고
        crushingStoS(oldn, d, nx, ny) # 산타한테 충돌당한 산타 정보, 방향, 좌표
    else: # 산타없음
        game[nx][ny] = n # 게임판에 뉴 산타 번호 넣고
        P_arr[n] = [nx, ny] # 산타 위치 저장 배열 정보 갱신하고

res = []

for i in range(M): 
    if len(out_P) == P:
        break

    r_moving(i, rx, ry)
    # print("루돌프 이동후")
    s_moving(i)

    # print()
    # for a in game:
    #     print(a)
    
    for x in P_number:
        if x not in out_P:
            s_score[x] += 1
    
for x in P_number:
    res.append(s_score[x])
print(*res)