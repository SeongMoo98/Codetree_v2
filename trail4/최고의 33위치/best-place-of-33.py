N  = int(input())

matrix = [list(map(int, input().split())) for i in range(N)]


MAX_COUNT = 0

for i in range(N-3+1):
    for j in range(N-3+1):
        count = 0 
        for di in range(3):
            for dj in range(3):
                if matrix[i+di][j+dj] == 1:
                    count += 1
        MAX_COUNT = max(MAX_COUNT, count)

print(MAX_COUNT)

