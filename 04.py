import heapq
h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]
n = int(input())

class NodeInfo:
    def __init__(self, y, x, ticket, cost):
        self.y = y
        self.x = x
        self.ticket = ticket
        self.cost = cost
    
    def __eq__(self, other):
        if other is None or not isinstance(other, NodeInfo):
            return False
        return self.y == other.y and self.x == other.x and self.ticket == other.ticket and self.cost == other.cost
    
    def __hash__(self):
        return hash((self.y, self.x, self.ticket, self.cost))

    def __lt__(self, other):
        if not isinstance(other, NodeInfo):
            return False
        return self.cost < other.cost

    def __gt__(self, other):
        return not self.__lt__(other)

stNode = NodeInfo(0, 0, n, 0)
seen = set()

hq = []
heapq.heapify(hq)
heapq.heappush(hq, stNode)

vy = (1, -1, 0, 0)
vx = (0, 0, 1, -1)
edNode = None

for _ in range(10**9):
    Node = heapq.heappop(hq)
    cy = Node.y
    cx = Node.x
    t = Node.ticket
    cc = Node.cost

    if cy == h-1 and cx == w - 1:
        edNode = Node
        break

    if Node in seen:
        continue
    
    seen.add(Node)

    for dy, dx in zip(vy, vx):
        ny = cy + dy
        nx = cx + dx

        if (ny in (-1, h) or nx in (-1, w)):
            continue
        
        c = cc + T[ny][nx]
        nextNode = NodeInfo(ny, nx, t, c)
        heapq.heappush(hq, nextNode)
        if t > 0:
            nextNode_t = NodeInfo(ny, nx, t - 1, cc)
            heapq.heappush(hq, nextNode_t)

    
    if not hq:
        break

print(edNode.cost)