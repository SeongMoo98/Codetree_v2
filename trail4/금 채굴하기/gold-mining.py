# N x N 매트릭스(금이 있으면 1)

# 금을 최대한 많이 채굴
# 마름모 꼴로 단 한 번 채굴 가능
# 마름모 모양을 지키는 한 매트릭스 벗어나도 됨

# 마름모: K번 이내로 상하좌우 인접한 곳으로 이동했을 때 갈 수 있는 모든 영역
# 비용: K^2 + (K+1)^2
# 금의 가격 : M

# >> 손해 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수 출력

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(N)]

ans = 0

for i in range(N):
    for j in range(N):
        # 그리드 경계까지 가장 먼 거리를 넘어서면 금은 더 늘지 않고 비용만 커진다
        max_k = max(i, N - 1 - i) + max(j, N - 1 - j)

        count = matrix[i][j]
        if count * M - 1 >= 0:  # k = 0: cost = 0^2 + 1^2 = 1
            ans = max(ans, count)

        for k in range(1, max_k + 1):
            for dx in range(-k, k + 1):
                dy = k - abs(dx)
                for sign in ((1, -1) if dy != 0 else (1,)):
                    ni, nj = i + dx, j + dy * sign
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 1:
                        count += 1
            cost = k**2 + (k + 1)**2
            if count * M - cost >= 0:  # 손해가 아닌 경우만 후보로
                ans = max(ans, count)

print(ans)

