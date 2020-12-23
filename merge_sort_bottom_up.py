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

def bottom_up_merge_sort(num_list):
    size = 1

    while size < len(num_list):
        start_idx = 0

        while start_idx < len(num_list):
            end_idx = min(start_idx + size * 2 - 1, len(num_list)-1)
            mid_idx = min(start_idx + size - 1, end_idx)

            combine(num_list, start_idx, mid_idx, end_idx)
            print(num_list)

            start_idx = end_idx + 1

        size *= 2

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

bottom_up_merge_sort(num_list)