
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        z = state.index(0)

        for d in [-3, 3, -1, 1]:
            n = z + d

            if 0 <= n < 9 and (abs(d) == 3 or z//3 == n//3):
                new = list(state)
                new[z], new[n] = new[n], new[z]
                new = tuple(new)

                if new not in visited:
                    visited.add(new)
                    queue.append((new, path + [new]))
    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

result = bfs(start, goal)

if result:
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("Total Moves:", len(result)-1)
else:
    print("No Solution")
