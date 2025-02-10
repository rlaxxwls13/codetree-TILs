import heapq

N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Write your code here!

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -heapq.heappop(self.items)

    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -self.items[0]

pq = PriorityQueue()

for i in range(N):
    if commands[i][0] == "push":
        pq.push(commands[i][1])
    elif commands[i][0] == "size":
        print(pq.size())
    elif commands[i][0] == "empty":
        if pq.empty():
            print(1)
        else:
            print(0)
    elif commands[i][0] == "pop":
        print(pq.pop())
    elif commands[i][0] == "top":
        print(pq.top())