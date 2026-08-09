# N <= 500,000
# 1. 맨 앞의 정수 제거
# 2. 남은 수열의 맨 앞의 정수를 맨 뒤로 이동
from collections import deque 
N = int(input())

q = deque(range(1, N+1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])


