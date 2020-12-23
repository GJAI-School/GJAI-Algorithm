before_str, cipher_num = input().split()
cipher_num = int(cipher_num)

# [dictionary]
#
# key_dict = []
#
# for i in range(0, 10):
#     key_dict[str(i)] = i
#
# for i in range(0, 26):
#     key_dict[chr(ord('A')+i)] = 10+i
#
decimal_result = 0
key_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 
'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 
'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

for i in range(0, len(before_str)):
    idx_char = before_str[len(before_str)-1-i]
    decimal_result += key_dict[idx_char] * (cipher_num ** i)

# [string map index]
decimal_result = 0
char_num_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(before_str)):
    idx_char = before_str[len(before_str)-1-i]
    decimal_result += char_num_map.find(idx_char) * (cipher_num ** i)

# [ascii code (ord method)]
decimal_result = 0

for i in range(0, len(before_str)):
    idx_char = before_str[len(before_str)-1-i]

    # if ord('0') <= ord(idx_char) <= ord('9')
    if idx_char.isnumeric():
        decimal_result += int(idx_char) * (cipher_num ** i)
    else:
        decimal_result += (ord(idx_char)-ord('A')+10) * (cipher_num ** i)

#
print(decimal_result)