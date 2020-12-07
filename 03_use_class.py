import heapq
h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]
n = int(input())

class NodeInfo:
    def __init__(self, y, x, cost, preNode):
        self.y = y
        self.x = x
        self.cost = cost
        self.preNode = preNode

stNode = NodeInfo(0, 0, 0, None)
seen = [[False for i in range(w)] for j in range(h)]

hq = []
heapq.heapify(hq)
heapq.heappush(hq, (0, 0, stNode))

vy = (1, -1, 0, 0)
vx = (0, 0, 1, -1)
edNode = None

for _ in range(10**9):
    cc, index, Node = heapq.heappop(hq)
    cy = Node.y
    cx = Node.x
    if cy == h-1 and cx == w - 1:
        edNode = Node
        break

    seen[cy][cx] = True

    for dy, dx in zip(vy, vx):
        ny = cy + dy
        nx = cx + dx

        if (ny in (-1, h) or nx in (-1, w)) or seen[ny][nx]:
            continue
        
        c = cc + T[ny][nx]
        nextNode = NodeInfo(ny, nx, c, Node)
        heapq.heappush(hq, (c, id(nextNode), nextNode))
    
    if not hq:
        break

print(edNode.cost)
pNode = edNode
for _ in range(10**9):
    print('--')
    py, px = pNode.y, pNode.x

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

    pNode = pNode.preNode
