# 1 ~ 100 숫자로 이루어진 N x N 격자

# 격자 내에 있는 기울어진 사각형을 살펴보려한다
# 기울어진 사각형
# 격자 내에 있는 한 지점으로부터 대각선으로 움직이며
# 반시계 방향으로 순회했을 때 지나왔던 지점들의 집합
# (격자 밖으로 넘어가서는 안된다)

# 기울어진 직사각형들 중 해당 직사각형을 이루는 지점에 적힌 숫자들의 최대 합

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0

def is_range(ci, cj):
    return 0 <= ci < N and 0 <= cj < N

def get_score(ci, cj, w, h):
    dis, djs = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [w, h, w, h]

    temp = 0

    for di, dj, move_num in zip(dis, djs, move_nums):
        for _ in range(move_num):
            ni, nj = ci + di, cj + dj

            if not is_range(ni, nj):
                return 0
            
            temp += matrix[ni][nj]
            ci, cj = ni, nj

    return temp

for i in range(N):
    for j in range(N):
        for w in range(1, N):
            for h in range(1, N):
                ans = max(ans, get_score(i, j, w, h))

print(ans)
