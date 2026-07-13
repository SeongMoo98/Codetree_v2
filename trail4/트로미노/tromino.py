# 트로미노
# N x M 격자에 자연수 존재
# 두 개의 블럭 중 한 개의 블록을 격자에 벗어나지 않게 칸 안에 적힌 숫자이 합이 최대
# 블럭은 회전 가능

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]

ans = 0 

# 1. 일자
for i in range(N):
    for j in range(M-3+1):
        ans = max(ans, sum(grid[i][j:j+3]))

# 2. 세로
for j in range(M):
    for i in range(N-3+1):
        ans = max(ans, grid[i][j] + grid[i+1][j] + grid[i+2][j])

# 3. ㄱ자
for i in range(N-1):
    for j in range(M-1):
        ans = max(ans, grid[i][j] + grid[i+1][j] + grid[i+1][j+1])
        ans = max(ans, grid[i][j] + grid[i][j+1] + grid[i+1][j])
        ans = max(ans, grid[i][j] + grid[i][j+1] + grid[i+1][j+1])
        ans = max(ans, grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1])


print(ans)
