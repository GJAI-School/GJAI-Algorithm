before_str, cipher_num = input().split()
cipher_num = int(cipher_num)

def get_decimal_num(idx_char):
    if idx_char.isnumeric():
        return int(idx_char)
    
    return ord(idx_char) - ord('A') + 10

def decimal_conv(now_idx, before_str, cipher_num):
    if now_idx == len(before_str):
        return 0

    sum_val = get_decimal_num(before_str[now_idx]) * (cipher_num ** (len(before_str)-1-now_idx))
    return sum_val + decimal_conv(now_idx+1, before_str, cipher_num)

print(decimal_conv(0, before_str, cipher_num))