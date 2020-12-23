t = int(input())

for _ in range(t):
    open_cnt = 0

    for p_str in input():
        if p_str == "(":
            open_cnt += 1
        elif p_str == ")":
            open_cnt -= 1

            if open_cnt < 0:
                break

    if open_cnt == 0:
        print("YES")
    else:
        print("NO")
