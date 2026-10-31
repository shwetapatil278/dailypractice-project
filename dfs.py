
def dfs(a, b, target):
    stack = [(0, 0, [])]
    visited = set()

    while stack:
        x, y, path = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            return path

        moves = [
            (a, y), (x, b),
            (0, y), (x, 0),
            (x-min(x, b-y), y+min(x, b-y)),
            (x+min(y, a-x), y-min(y, a-x))
        ]

        for move in moves:
            if move not in visited:
                stack.append((*move, path))

    return None

result = dfs(4, 3, 2)
print("DFS solution:")
print()
if result:
    for state in result:
        print(state)
else:
    print("No Solution")
