N = int(input())
A = [int(input()) for _ in range(N)]
Aset = set(A)
M = 0

def checking(arr):
    cnt = 1
    max_cnt = 1
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    max_cnt = max(max_cnt, cnt)
    return max_cnt


for n in Aset:
    Acopy = []
    for a in A:
        if a != n:
            Acopy.append(a)
    cnt = checking(Acopy)
    M = max(M, cnt)

print(M)