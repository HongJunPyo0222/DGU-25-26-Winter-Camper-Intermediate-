n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


max_score = [[0 for _ in range(n)] for _ in range(n)]

# 1. 시작점 초기화
max_score[0][0] = grid[0][0]

# 2. 첫 번째 행 초기화 (왼쪽에서 오는 것만 가능)
for j in range(1, n):
    max_score[0][j] = max_score[0][j-1] + grid[0][j]

# 3. 첫 번째 열 초기화 (위쪽에서 오는 것만 가능)
for i in range(1, n):
    max_score[i][0] = max_score[i-1][0] + grid[i][0]

# 4. 나머지 칸 채우기 (위쪽 vs 왼쪽 중 큰 값 선택)
for i in range(1, n):
    for j in range(1, n):
        max_score[i][j] = max(max_score[i-1][j], max_score[i][j-1]) + grid[i][j]

# 결과 출력
print(max_score[n-1][n-1])