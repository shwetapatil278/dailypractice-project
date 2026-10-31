
from collections import deque

def bfs(grid, start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(grid) and
                0 <= ny < len(grid[0]) and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = bfs(grid, start, goal)
print("Shortest Path:", path)
