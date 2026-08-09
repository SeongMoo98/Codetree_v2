# N 명의 사람이 모두 제거될때까지 진행
# 1번부터 순서대로 K번째 사람을 제거
# 한 사람이 제거되면 남은 사람들로 원을 이루고,
# 제거된 사람의 위치를 기준으로 다시 K 번쨰 사람을 제거

# 제거되는 사람의 번호를 순서대로 나열

from collections import deque

N, K = map(int, input().split())

q = deque(list(range(1, N+1)))
res = []

while q:
    for _ in range(K-1):
        q.append(q.popleft())
    res.append(q.popleft())

print(" ".join(map(str, res)))





