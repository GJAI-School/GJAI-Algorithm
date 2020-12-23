n = int(input())
meet_list = []

for _ in range(n):
    # start_time, end_time = map(int, input().split())
    # meet_list.append({"start_time": start_time, "end_time": end_time})
    meet_list.append(list(map(int, input().split())))

meet_list.sort(key=lambda meet: [meet[1], meet[0]])
# meet_list.sort(key=lambda meet: [meet["end_time"], meet["start_time"]])

result_meet_cnt = 1
booked_end_time = meet_list[0][1]

for idx in range(1, len(meet_list)):
    if meet_list[idx][0] >= booked_end_time:
        print(meet_list[idx])
        booked_end_time = meet_list[idx][1]
        result_meet_cnt += 1

print(result_meet_cnt)