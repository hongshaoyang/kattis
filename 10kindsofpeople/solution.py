from sys import stdin
from collections import deque

class Solution:

    def __init__(self, world):
        self.visited = set()
        self.found = False
        self.world = world
        self.stack = deque([], R*C)
        
    # solution using dfs2
    def solution(self, r1, c1, r2, c2):
        is_binary = (self.world[r1][c1] == "0")
        self.stack.append((r1, c1))
        if self.dfs2(r2, c2, is_binary):
            return "binary" if is_binary else "decimal"
        return "neither"
        

    # recursive dfs, will hit stack limit, BAD!
    def dfs(self, i, j, r2, c2, is_binary):
        self.visited.add((i, j))
        if i == r2 and j == c2:
            self.found = True
            return
        nodes = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for dir in nodes:
            if self.ok(dir[0], dir[1], is_binary):
                self.dfs(dir[0], dir[1], r2, c2, is_binary)

    # version 2: store a stack of nodes to visit
    def dfs2(self, r2, c2, is_binary):
        while len(self.stack) > 0:
            node = self.stack.pop()
            if node == (r2, c2):
                return True
            if node not in self.visited:
                self.visited.add(node)
                i, j = node
                nodes = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for dir in nodes:
                    if self.ok(dir[0], dir[1], is_binary):
                        self.stack.append(dir)
        return False

    # check if (i,j) can be visited
    def ok(self, i, j, is_binary):
        in_range = (0 <= i <= R-1) and (0 <= j <= C-1)
        if not in_range:
            return False
        zone = self.world[i][j] == ("0" if is_binary else "1")
        not_visited = (i,j) not in self.visited
        return zone and not_visited

if __name__ == "__main__":
    R, C = map(int, stdin.readline().split(" "))
    world = [[None for _ in range(C)] for _ in range(R)]
    for i in range(R):
        line = stdin.readline()
        for j in range(C):
            world[i][j] = line[j]

    N = int(stdin.readline())
    for _ in range(N):
        r1, c1, r2, c2 = map(int, stdin.readline().split(" "))
        print(Solution(world).solution(r1-1, c1-1, r2-1, c2-1))