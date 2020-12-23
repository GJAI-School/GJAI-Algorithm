# 60466175 36   : ZZZZZ
# 447 16        : 1BF
# 237 2         : 11101101
# 52 8          : 64

def make_numeral_char(remainder):
    if remainder >= 10:
        return chr(remainder - 10 + ord('A'))
    
    return str(remainder)

def n_conv(quotient, target_numeral_base):
    if quotient == 0:
        return ""

    divided_quotient, remainder = divmod(quotient, target_numeral_base)
    return n_conv(divided_quotient, target_numeral_base) + make_numeral_char(remainder)

decimal_num, target_numeral_base = map(int, input().split())
print(n_conv(decimal_num, target_numeral_base))