decimal_num, target_numeral_base = map(int, input().split())

char_num_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result_list = []

quotient = decimal_num

while quotient > 0:
    quotient, remainder = divmod(quotient, target_numeral_base)
    result_list.append(char_num_map[remainder])

    # if remainder >= 10:
    #     result_list.append(chr(remainder - 10 + ord('A')))
    # else:
    #     result_list.append(str(remainder))

print("".join(result_list[::-1]))
