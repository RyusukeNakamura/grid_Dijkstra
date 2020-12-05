# from collections import deque
import heapq

h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]

seen = [[False for i in range(w)] for j in range(h)]
hq = []
heapq.heapify(hq)

heapq.heappush(hq, (0, 0, 0))
dp = [[100000 for i in range(w)] for j in range(h)]
dp[0][0] = T[0][0]
vy = (1, -1, 0, 0)
vx = (0, 0, 1, -1)

for _ in range(10**9):
    cost, cy, cx = heapq.heappop(hq)
    seen[cy][cx] = True

    for y, x in zip(vy, vx):
        ny = cy + y
        nx = cx + x

        if not (ny in (-1, h) or nx in (-1, w)) and not seen[ny][nx]:
            if cost+T[ny][nx] < dp[ny][nx]:
                dp[ny][nx] = cost + T[ny][nx]
                heapq.heappush(hq, (dp[ny][nx], ny, nx))
    
    if not hq:
        break

print(dp[h-1][w-1]) 