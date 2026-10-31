
def solve(row, queens):
    if row == 8:
        for q in queens:
            print(" ".join("Q" if i == q else "." for i in range(8)))
        return True

    for col in range(8):
        if all(col != c and abs(row-r) != abs(col-c)
               for r, c in enumerate(queens)):
            if solve(row+1, queens+[col]):
                return True
    return False

solve(0, [])
