from collections import deque
h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]

seen = [[False for i in range(w)] for j in range(h)]

deq = deque()
deq.append((0, 0, (0, -1, -1)))

dp = [[[100000, -1, -1] for i in range(w)] for j in range(h)]
dp[0][0][0] = T[0][0]

vy = (1, -1, 0, 0)
vx = (0, 0, 1, -1)

for _ in range(10**9):
    cy, cx, t = deq.popleft()
    cost, py, px = t
    seen[cy][cx] = True

    for y, x in zip(vy, vx):
        ny = cy + y
        nx = cx + x

        if not (ny in (-1, h) or nx in (-1, w)) and not seen[ny][nx]:
            if cost + T[ny][nx] < dp[ny][nx][0]:
                dp[ny][nx] = [dp[cy][cx][0] + T[ny][nx], cy, cx]

            deq.append((ny, nx, tuple(dp[ny][nx])))
    
    if not deq:
        break

py, px = h-1, w-1
print(dp[py][px][0])
for _ in range(10**9):
    print('--')
    for i in range(h):
        s = ''
        for j in range(w):
            if i == py and j == px:
                s += '*' + str(T[i][j])
            else:
                s += ' ' + str(T[i][j])
        print(s)
    if py == 0 and px == 0:
        break

    cost, py, px = dp[py][px]
