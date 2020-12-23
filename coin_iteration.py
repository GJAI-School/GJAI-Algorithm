n, k = map(int, input().split())
coins_list = []
min_result_cnt = 0
# coins_cnt_list = []

for _ in range(n):
    coins_list.append(int(input()))
    # coins_list.insert(0, int(input()))

for coin in reversed(coins_list):
    coin_cnt = k // coin
    min_result_cnt += coin_cnt
    # coins_cnt_list.append(str(coin_cnt))
    k %= coin

print(min_result_cnt)
# print("\n".join(coins_cnt_list[::-1]))