# 7 3
from collections import deque

n, k = map(int, input().split())
num_list = deque(range(1, n+1))

result_str = ""

while len(num_list) > 0:
    num_list.rotate(-(k-1))
    result_str += f"{num_list.popleft()}, "

print(f"<{result_str.rstrip(', ')}>")