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
    cost, index, Node = heapq.heappop(hq)
    cy = Node.y
    cx = Node.x
    if cy == h-1 and cx == w - 1:
        edNode = Node
        break

    seen[cy][cx] = True

    for y, x in zip(vy, vx):
        ny = cy + y
        nx = cx + x

        if (ny in (-1, h) or nx in (-1, w)) or seen[ny][nx]:
            continue
        
        c = cost + T[ny][nx]
        nextNode = NodeInfo(ny, nx, c, Node)
        heapq.heappush(hq, (c, id(nextNode), nextNode))
    
    if not hq:
        break

print(edNode.cost)