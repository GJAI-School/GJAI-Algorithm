# import sys
# input = sys.stdin.readline

class Queue:
    def __init__(self, length):
        self.length = length+1
        self.array_list = [0 for _ in range(length+1)]
        self.f_idx = 0
        self.r_idx = 0
    
    def push(self, value):
        if self.is_full():
            return -1
        
        self.r_idx = (self.r_idx + 1) % self.length
        self.array_list[self.r_idx] = value
    
    def pop(self):
        if self.size() == 0:
            return -1
        
        self.f_idx = (self.f_idx + 1) % self.length

        pop_value = self.array_list[self.f_idx]
        # self.array_list[self.f_idx] = 0
        return pop_value
    
    def size(self):
        return (self.length + self.r_idx - self.f_idx) % self.length
    
    def is_full(self):
        return (self.r_idx + 1) % self.length == self.f_idx

    def empty(self):
        if self.size() == 0:
            return 1
        
        return 0
    
    def front(self):
        if self.size() == 0:
            return -1

        return self.array_list[self.f_idx+1]

    def back(self):
        if self.size() == 0:
            return -1
        
        return self.array_list[self.r_idx]

def process_queue(queue_list, command):
    cmd = command[0]
    if cmd == "push":
        if queue_list.push(command[1]) is not None:
            print("full list!")
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

    print(queue_list.array_list)
 
n = int(input())
queue_list = Queue(length=4)

for _ in range(n):
    command = input().split()
    process_queue(queue_list, command)