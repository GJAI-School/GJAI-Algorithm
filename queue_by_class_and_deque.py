# import sys
# input = sys.stdin.readline
from collections import deque

class Queue:
    def __init__(self, length):
        self.array_list = deque()
    
    def push(self, value):
        self.array_list.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.array_list.popleft()
        
        return -1

        # try:
        #     return self.array_list.popleft()
        # except IndexError:
        #     return -1
    
    def size(self):
        return len(self.array_list)
    
    def empty(self):
        # return int(self.size() <= 0)
        if self.size() > 0:
            return 0
        
        return 1
    
    def front(self):
        if self.size() > 0:
            return self.array_list[0]
        
        return -1

    def back(self):
        if self.size() > 0:
            return self.array_list[self.size()-1]
        
        return -1

def process_queue(queue_list, command):
    cmd = command[0]
    if cmd == "push":
        queue_list.push(command[1])
    elif cmd == "pop":
        print(queue_list.pop())
    elif cmd == "size":
        print(queue_list.size())
    elif cmd == "empty":
        print(queue_list.empty())
    elif cmd == "front":
        print(queue_list.front())
    elif cmd == "back":
        print(queue_list.back())
 
n = int(input())
queue_list = Queue(length=n)

for _ in range(n):
    command = input().split()
    process_queue(queue_list, command)