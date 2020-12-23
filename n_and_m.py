# [input]
# 4 2

# [output]
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3

def backt(now_idx, end_idx, n, result_list, used_list):
    if now_idx >= end_idx:
        print(" ".join(map(str, result_list)))
    else:
        for i in range(1,n+1):
            # if i not in result_list:
            if not used_list[i]: # if used_list[i] == False:
                used_list[i] = True
                backt(now_idx+1, end_idx, n, result_list+[i], used_list)
                used_list[i] = False

n, m = map(int, input().split())

used_list = [False] * (n+1)
backt(0, m, n, [], used_list)