# import sys
# input = sys.stdin.readline 

from collections import deque

class StackAndQueue:
    def __init__(self, n, data_type="stack"):
        self.array = deque()
        self.data_type = data_type
    
    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.size() == 0:
            return -1

        if self.is_stack():
            return self.array.pop()
        
        return self.array.popleft()

    def size(self):
        return len(self.array)

    def is_stack(self):
        return self.data_type == "stack"

    def empty(self):
        if self.size() == 0:
            return 1

        return 0

    def front(self):
        if self.is_stack() or self.size() == 0:
            return -1

        return self.array[0]

    def back(self):
        if self.is_stack() or self.size() == 0:
            return -1
            
        return self.array[-1]

    def top(self):
        if not self.is_stack() or self.size() == 0:
            return -1

        return self.array[-1]
    
    def get_last_val(self):
        return self.array[0]

def process(instance, command):
    cmd = command
    if cmd[0] == "push":
        instance.push(cmd[1])
    elif cmd[0] == "pop":
        print(instance.pop())
    elif cmd[0] == "size":
        print(instance.size())
    elif cmd[0] == "empty":
        print(instance.empty())
    elif cmd[0] == "front":
        print(instance.front())
    elif cmd[0] == "back":
        print(instance.back())
    elif cmd[0] == "top":
        print(instance.top())

n = int(input())
s_instance = StackAndQueue(n)

for _ in range(n):
    command = input().split()
    process(s_instance, command)