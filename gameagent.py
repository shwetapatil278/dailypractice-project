
board = [' '] * 9

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def winner():
    lines = [(0,1,2),(3,4,5),(6,7,8),
             (0,3,6),(1,4,7),(2,5,8),
             (0,4,8),(2,4,6)]
    for a,b,c in lines:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return 'D' if ' ' not in board else None

def minimax(ai):
    w = winner()
    if w:
        return {'O': 1, 'X': -1, 'D': 0}[w]

    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if ai else 'X'
            scores.append(minimax(not ai))
            board[i] = ' '
    return max(scores) if ai else min(scores)

while not winner():
    print_board()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos not in range(9) or board[pos] != ' ':
        print("Invalid move!")
        continue

    board[pos] = 'X'

    if not winner():
        best_score = -float('inf')
        best_move = 0

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '

                if score > best_score:
                    best_score = score
                    best_move = i

        board[best_move] = 'O'

print_board()
print("Result:", {'X': 'You Win!', 'O': 'AI Wins!', 'D': 'Draw!'}[winner()])
