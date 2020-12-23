from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split())
q_list = deque([i for i in range(1, n+1)])

result = 0

for target_num in target_list:
    # move_cnt = -q_list.index(target_num)
    
    # if int(len(q_list)/2) < abs(move_cnt):
    #     move_cnt += len(q_list)
    
    # q_list.rotate(move_cnt)
    # result += abs(move_cnt)
    
    pull_cnt = q_list.index(target_num)
    push_cnt = len(q_list) - pull_cnt

    if pull_cnt < push_cnt:
        result += pull_cnt
        q_list.rotate(-pull_cnt)
    else:
        result += push_cnt
        q_list.rotate(push_cnt)
    
    q_list.popleft()

print(result)