h, w = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(h)]

# グリッド状の盤面の左上からスタートして、「右、下、右、上、左」と順に移動したときの経路上のマスのコストの合計を求めてください。
ans = T[0][0] + T[0][1] + T[1][1] + T[1][2] + T[0][2] + T[0][1]
print(ans)