import heapq
h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]


class NodeInfo:
    def __init__(self, y, x, cost):
        self.y = y
        self.x = x
        self.cost = cost
    
    def __eq__(self, other):
        if other is None or not isinstance(other, NodeInfo):
            return False
        return self.y == other.y and self.x == other.x
    
    def __hash__(self):
        return hash((self.y, self.x))

    def __lt__(self, other):
        if not isinstance(other, NodeInfo):
            return False
        return self.cost < other.cost

    def __gt__(self, other):
        return not self.__lt__(other)

vy = (1, -1, 0, 0)
vx = (0, 0, 1, -1)

def prim(stNode):
    seen = set()
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq, stNode)
    cost = 0
    for _ in range(10**9):
        Node = heapq.heappop(hq)
        cy = Node.y
        cx = Node.x
        
        if Node in seen:
            continue
        seen.add(Node)
        cost += Node.cost
        if len(seen) == h * w:
            return cost
        
        for dy, dx in zip(vy, vx):
            ny = cy + dy
            nx = cx + dx

            if (ny in (-1, h) or nx in (-1, w)):
                continue
            
            c = T[cy][cx] * T[ny][nx]
            nextNode = NodeInfo(ny, nx, c)
            heapq.heappush(hq, nextNode)

sNode = NodeInfo(0, 0, 0)
ans = prim(sNode)

print(ans)