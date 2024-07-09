def no_carry(a, b):
    while a > 0 and b > 0:
        if (a % 10 + b % 10) >= 10:
            return False
        a //= 10
        b //= 10
    return True

def backtrack(index, count, selected):
    global max_count
    if index == n:
        max_count = max(max_count, count)
        return
    
    # 현재 숫자를 선택하지 않는 경우
    backtrack(index + 1, count, selected)
    
    # 현재 숫자를 선택하는 경우
    can_select = True
    for num in selected:
        if not no_carry(numbers[index], num):
            can_select = False
            break
    
    if can_select:
        selected.append(numbers[index])
        backtrack(index + 1, count + 1, selected)
        selected.pop()

n = int(input())
numbers = [int(input()) for _ in range(n)]

max_count = 0
backtrack(0, 0, [])
print(max_count)