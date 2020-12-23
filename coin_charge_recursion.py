price = int(input())
charge_money = 1000 - price
coins_list = [500,100,50,10,5,1]
coins_cnt_list = []

def calc_coin_cnt(charge_money, now_idx, coins_list): #, coins_cnt_list):
    if now_idx == len(coins_list):
        return 0

    # coins_cnt_list.append(charge_money // coins_list[now_idx])
    return charge_money // coins_list[now_idx] + calc_coin_cnt(charge_money % coins_list[now_idx], now_idx+1, coins_list)#, coins_cnt_list)

print(calc_coin_cnt(charge_money, 0, coins_list))#, coins_cnt_list))
# print(coins_cnt_list)
