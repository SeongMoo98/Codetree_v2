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

MAX_K = 2 * N  # 이 이상 커지면 그리드 전체를 이미 덮고도 남아 의미 없음
ans = 0

# 1. 중심 좌표 순회
for i in range(N):
    for j in range(N):

        # 2. 반지름 K 순회
        for k in range(MAX_K + 1):

            # 3. 이번 K로 만든 마름모 안의 금 개수 세기
            count = 0
            for x in range(N):
                for y in range(N):
                    if abs(x - i) + abs(y - j) <= k and matrix[x][y] == 1:
                        count += 1

            # 4. 비용 계산
            cost = k**2 + (k + 1)**2

            # 5. 손해가 아니면 채굴 개수 후보로 등록
            if count * M - cost >= 0:
                ans = max(ans, count)

print(ans)
