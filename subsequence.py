# 5 0
# -7 -3 -2 5 8

def make_subseq(now_idx, total_sum, num_list, s, used_list):
    if now_idx >= len(num_list):
        if total_sum == s:
            # print(f"{used_list}: {total_sum}")
            return 1
        
        return 0
    else:
        used_cnt = make_subseq(now_idx+1, total_sum+num_list[now_idx], num_list, s, used_list+[num_list[now_idx]])
        unused_cnt = make_subseq(now_idx+1, total_sum, num_list, s, used_list)
        
        return used_cnt+unused_cnt

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = make_subseq(0, 0, num_list, s, [])

if s == 0:
    cnt -= 1

print(cnt)