result_coins_cnt = 0
coins_list = [500, 100, 50, 10, 5, 1]
coins_cnt_list = []

price = int(input()) # 380
charge_money = 1000-price # 620

for coin in coins_list:
    result_coins_cnt += charge_money // coin
    # result_coins_cnt += int(charge_money/coin)
    charge_money %= coin
    # coins_cnt_list.append(charge_money // coin)

print(result_coins_cnt)