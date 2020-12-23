from collections import deque

def search_dfs(now_node, adj_arr, visit, n):
    print(now_node, end=" ")
    visit[now_node] = True

    for i in range(1, n+1):
        if adj_arr[now_node][i] == 1 and not visit[i]:
            search_dfs(i, adj_arr, visit, n)

def search_bfs(v, adj_arr, visit, n):
    queue = [v]
    visit[v] = True
    f_idx = 0
    r_idx = 1

    while f_idx < r_idx:
        now_node = queue[f_idx]

        print(now_node, end=" ")

        for i in range(1, n+1):
            if adj_arr[now_node][i] == 1 and not visit[i]:
                queue.append(i)
                visit[i] = True
                r_idx += 1

        f_idx += 1

def search_bfs_with_deque(v, adj_arr, visit, n):
    queue = deque([v])
    visit[v] = True

    while len(queue) > 0:
        now_node = queue.popleft()
        print(now_node, end=" ")

        for i in range(1, n+1):
            if adj_arr[now_node][i] == 1 and not visit[i]:
                queue.append(i)
                visit[i] = True


n, m, v = map(int, input().split())
adj_arr = [[0] * (n+1) for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    adj_arr[v1][v2] = 1
    adj_arr[v2][v1] = 1

search_dfs(v, adj_arr, visit, n)
print()

visit = [False] * (n+1)
search_bfs(v, adj_arr, visit, n)
# search_bfs_with_deque(v, adj_arr, visit, n)
print()
