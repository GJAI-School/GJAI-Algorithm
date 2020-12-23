def b_search(total_list, find_target_value, start_idx, end_idx):
    if start_idx > end_idx:
        return -1
    
    target_idx = int((start_idx + end_idx) / 2)
    
    if find_target_value < total_list[target_idx]:
        return b_search(total_list, find_target_value, start_idx, target_idx-1)
    elif find_target_value > total_list[target_idx]:
        return b_search(total_list, find_target_value, target_idx+1, end_idx)
    
    return target_idx

n = int(input())
num_list = sorted(list(map(int, input().split())))

m = int(input())
for find_num in list(map(int, input().split())):
    if b_search(num_list, find_num, 0, len(num_list)-1) >= 0:
        print("1")
    else:
        print("0")
