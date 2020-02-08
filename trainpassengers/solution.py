import sys

class Solution:
    def trainpassengers(self, C: int, n:int, lines):
        curr = 0
        for i, station in enumerate(lines):
            left, entered, stay = station
            if i == 0 and (left > 0):
                return "impossible"
            new = curr + entered - left
            if new > C or new < 0 or (stay > 0 and new < C):
                return "impossible"
            curr = new
        if stay > 0 or curr > 0 or entered > 0:
            return "impossible"
        return "possible"
        


if __name__ == "__main__":
    C, n = map(int, sys.stdin.readline().split(" "))
    lines = []
    for i in range(n):
        # generic format hopefully
        lines.append(tuple(map(int, sys.stdin.readline().split(" "))))

    result = Solution().trainpassengers(C, n, lines)
    print(result)