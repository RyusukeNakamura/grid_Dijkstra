from collections import deque
h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]

seen = [[False for i in range(w)] for j in range(h)]
deq = deque()
deq.append((0, 0))
dp = [[100000 for i in range(w)] for j in range(h)]
dp[0][0] = T[0][0]
vy = (1, -1, 0, 0)
vx = (0, 0, 1, -1)

for _ in range(10**9):
    cy, cx = deq.popleft()
    seen[cy][cx] = True

    for y, x in zip(vy, vx):
        ny = cy + y
        nx = cx + x

        if not (ny in (-1, h) or nx in (-1, w)) and not seen[ny][nx]:
            deq.append((ny, nx))
            dp[ny][nx] = min(dp[ny][nx], dp[cy][cx] + T[ny][nx])
    
    if not deq:
        break

print(dp[h-1][w-1]) 