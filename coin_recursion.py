def calc_minimum_cnt(before_money, now_idx, coins_list):#, coins_cnt_list):
    if before_money == 0:
        return 0

    divisor, mod = divmod(before_money, coins_list[now_idx])
    # coins_cnt_list[now_idx] = divisor

    return divisor + calc_minimum_cnt(mod, now_idx-1, coins_list)#, coins_cnt_list)

n, k = map(int, input().split())
coins_list = []
# coins_cnt_list = []

for _ in range(n):
    coins_list.append(int(input()))
    # coins_list.insert(0, int(input()))
    # coins_cnt_list.append(0)

print(calc_minimum_cnt(k, len(coins_list)-1, coins_list))#, coins_cnt_list))
# print("\n".join(map(str, coins_cnt_list[::-1])))