from collections import deque
# import sys

class Teque():
    def __init__(self, n):
        self.front = deque([], n)
        self.back = deque([], n)
        self.len = 0


    def push_front(self, num):
        self.len += 1

        if len(self.front) == len(self.back):
            self.front.appendleft(num)
        elif len(self.front) < len(self.back):
            self.front.appendleft(num)
        else:
            self.front.appendleft(num)
            # adjust
            self.back.appendleft(self.front.pop())

    def push_back(self, num):
        self.len += 1

        if len(self.front) == len(self.back):
            self.back.append(num)
        elif len(self.front) < len(self.back):
            self.back.append(num)
            # adjust
            self.front.append(self.back.popleft())
        else:
            self.back.append(num)


    def push_middle(self, num):
        self.len += 1

        if len(self.front) == len(self.back):
            self.front.append(num)
        elif len(self.front) < len(self.back):
            self.front.append(num)
        else:
            self.back.appendleft(num)

    def get(self, num) -> int:
        if num < len(self.front):
            return self.front[num]
        else:
            return self.back[num - len(self.front)]

if __name__ == "__main__":
    n = int(input())

    teque = Teque(n)

    for _ in range(n):
        op, num = input().split(" ")
        if op == "push_back":
            teque.push_back(int(num))
        elif op == "push_front":
            teque.push_front(int(num))
        elif op == "push_middle":
            teque.push_middle(int(num))
        else:
            print(teque.get(int(num)))

    print(teque.front)
    print(teque.back)