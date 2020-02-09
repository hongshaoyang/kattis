def brt(n: int, lines):
    lines.sort(key=lambda x: x[2])

    best_time, best_team = float('Inf'), []
    for i, runner in enumerate(lines): # choose first runner
        j, runners, time = 0, [i], runner[1]
        while len(runners) < 4: # add the rest of the team
            if j not in runners:
                time += lines[j][2]
                runners.append(j)
            j += 1

        if time < best_time:
            best_time, best_team = time, runners

    print(best_time)
    for r in best_team:
        print(lines[r][0])
            
if __name__ == "__main__":
    n = int(input())
    lines = []
    for i in range(n):
        # generic format hopefully
        line = input().split(" ")
        line[1:] = list(map(float, line[1:]))
        lines.append(line)


    brt(n, lines)