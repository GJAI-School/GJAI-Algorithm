import sys
input = sys.stdin.readline

def combine(num_list, start_idx, mid_idx, end_idx):
    l_idx = start_idx # start_idx ~ mid_idx
    r_idx = mid_idx+1 # mid_idx+1 ~ end_idx

    sorted_list = []

    while l_idx <= mid_idx and r_idx <= end_idx:
        # if l_idx > mid_idx:
        #     # sorted_list.append(num_list[r_idx])
        #     # r_idx += 1
        #     sorted_list += num_list[r_idx:end_idx+1]
        #     r_idx = end_idx + 1
        # elif r_idx > end_idx:
        #     # sorted_list.append(num_list[l_idx])
        #     # l_idx += 1
        #     sorted_list += num_list[l_idx:mid_idx+1]
        #     l_idx = mid_idx + 1
        if num_list[l_idx] < num_list[r_idx]:
            sorted_list.append(num_list[l_idx])
            l_idx += 1
        else:
            sorted_list.append(num_list[r_idx])
            r_idx += 1

    sorted_list += num_list[r_idx:end_idx+1]
    sorted_list += num_list[l_idx:mid_idx+1]

    num_list[start_idx:end_idx+1] = sorted_list

def merge_sort(num_list, start_idx, end_idx):
    if start_idx < end_idx:
        mid_idx = (start_idx + end_idx) // 2

        merge_sort(num_list, start_idx, mid_idx)
        merge_sort(num_list, mid_idx+1, end_idx)

        combine(num_list, start_idx, mid_idx, end_idx)
        # print(num_list)
    
    # return None

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

merge_sort(num_list, 0, len(num_list)-1)