def b_search(total_list, find_target_value):
    start_idx = 0
    end_idx = len(total_list)-1 # N-1
    
    while start_idx <= end_idx:
        target_idx = (start_idx + end_idx) // 2
        
        if find_target_value < total_list[target_idx]:
            end_idx = target_idx-1
        elif find_target_value > total_list[target_idx]:
            start_idx = target_idx+1
        else:
            return target_idx
    
    return -1

n = int(input())
num_list = sorted(list(map(int, input().split())))

m = int(input())
for find_num in list(map(int, input().split())):
    if b_search(num_list, find_num) >= 0:
        print("1")
    else:
        print("0")