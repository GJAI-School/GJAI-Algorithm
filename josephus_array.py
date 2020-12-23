# 7 3

n, k = map(int, input().split())
num_list = list(range(1, n+1))
# num_list = [i for i in range(1, n+1)]

idx = k-1
print("<", end="")
while len(num_list) > 1:
    print(num_list.pop(idx), end=", ")
    idx += (k-1)
    idx %= len(num_list)
    # idx = (idx+k-1) % len(num_list)

print(f"{num_list.pop(idx)}>")