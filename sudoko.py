
def possible(b, r, c):
    used = set(b[r]) | {b[i][c] for i in range(9)}
    used |= {b[i][j] for i in range(r//3*3, r//3*3+3)
                      for j in range(c//3*3, c//3*3+3)}
    return set(range(1, 10)) - used

def solve(b):
    while True:
        empty = [(possible(b, r, c), r, c)
                 for r in range(9) for c in range(9) if b[r][c] == 0]
        if not empty:
            return True
        choices, r, c = min(empty, key=lambda x: len(x[0]))
        if not choices:
            return False
        if len(choices) > 1:
            break
        b[r][c] = choices.pop()

    for n in sorted(choices):
        copy = [row[:] for row in b]
        copy[r][c] = n
        if solve(copy):
            b[:] = copy
            return True
    return False

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve(board):
    for row in board:
        print(*row)
else:
    print("No solution")
