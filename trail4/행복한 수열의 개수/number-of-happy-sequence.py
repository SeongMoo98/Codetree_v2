# 1 <= N <= 100
# 행복한 수열 = 연속하여 M개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
# 각 행/열 마다 봤을 때 나오는 N개의 수열 중 행복한 수열의 개수를 세서 출력

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0

if N == 1:
    ans = 2
else:
    # 행방향
    for i in range(N):
        count = 1
        for j in range(1, N):
            if matrix[i][j-1] == matrix[i][j]: count += 1
            else: count = 1 

            if count >= M:
                ans += 1
                break
    # 열방향
    for j in range(N):
        count = 1
        for i in range(1, N):
            if matrix[i-1][j] == matrix[i][j]: count += 1
            else: count = 1 

            if count >= M:
                ans += 1
                break
            

print(ans)