from collections import deque

n, m = map(int, input().split())
maze_map = [[0] * (m+2)]
visit = [[0] * (m+1) for _ in range(n+1)]

for _ in range(n):
    maze_map.append([0]+list(map(int, input()))+[0])

maze_map.append([0] * (m+2))

pos_calc = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

q = deque()
q.append([1,1])
visit[1][1] = 1

maze_end_flag = False

while not maze_end_flag:
    now_row, now_col = q.popleft()

    for c_row, c_col in pos_calc:
        target_row = now_row+c_row
        target_col = now_col+c_col

        if maze_map[target_row][target_col] == 1 and visit[target_row][target_col] == 0:
            q.append([target_row, target_col])
            visit[target_row][target_col] = visit[now_row][now_col] + 1
        
        if target_row == n and target_col == m:
            maze_end_flag = True

print(visit[n][m])