from collections import deque

def logn_calc(n):
    max_pow = 1

    while max_pow < n:
        max_pow *= 2

    return n * 2 - max_pow
    
def deque_calc(n):
    d_list = deque([i for i in range(1, n+1)])

    # for _ in range(n-1):
    while len(d_list) > 1: # O(N)
        d_list.popleft()
        d_list.rotate(-1)
    
    return d_list.popleft()

n = int(input())

print(logn_calc(n))
# print(deque_calc(n))