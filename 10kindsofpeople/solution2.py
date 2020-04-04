from sys import stdin
from collections import deque

class Solution:

    def __init__(self, world):
        self.world = world
        self.component = [[None for _ in range(C)] for _ in range(R)]
        self.preprocess()
        # print(self.component)

    def preprocess(self):
        counter = 1
        for i in range(R):
            for j in range(C):
                if self.component[i][j]:
                    continue
                self.dfs(counter, i, j)
                counter += 1

    def solution(self, r1, c1, r2, c2):
        return "neither" if self.component[r1][c1] != self.component[r2][c2] else ["binary", "decimal"][int(self.world[r1][c1])]
        
    def dfs(self, ctr, i, j):
        stack = deque([(i,j),], R*C)
        self.visited = set()

        while len(stack) > 0:
            node = stack.pop()
            if node not in self.visited:
                # print("\tvisit:", node)
                i, j = node
                self.component[i][j] = ctr
                self.visited.add(node)
                nodes = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for n in nodes:
                    if self.ok(n[0], n[1]) and self.world[i][j] == self.world[n[0]][n[1]]:
                        stack.append(n)

    # check if (i,j) can be visited
    def ok(self, i, j):
        in_range = (0 <= i <= R-1) and (0 <= j <= C-1)

        not_visited = (i,j) not in self.visited
        return in_range and not_visited

if __name__ == "__main__":
    R, C = map(int, stdin.readline().split(" "))
    world = [[None for _ in range(C)] for _ in range(R)]
    for i in range(R):
        line = stdin.readline()
        for j in range(C):
            world[i][j] = line[j]

    N = int(stdin.readline())
    s = Solution(world)
    for _ in range(N):
        r1, c1, r2, c2 = map(int, stdin.readline().split(" "))
        print(s.solution(r1-1, c1-1, r2-1, c2-1))