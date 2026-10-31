
import heapq

def heuristic(state, goal):
    return sum(a != b for a, b in zip(state, goal) if a != 0)

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)

        z = state.index(0)
        for d in [-3, 3, -1, 1]:
            n = z + d
            if 0 <= n < 9 and (abs(d) == 3 or z // 3 == n // 3):
                s = list(state)
                s[z], s[n] = s[n], s[z]
                s = tuple(s)
                if s not in visited:
                    heapq.heappush(pq, (g + 1 + heuristic(s, goal),
                                        g + 1, s, path + [state]))

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

print("A* Search Solution:")

for step in astar(start, goal):
    for i in range(0, 9, 3):
        print(step[i:i+3])
    print()
