
board = [["." for _ in range(3)] for _ in range(3)]

def isWinner(board):
    # checking for rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ".":
            return board[i][0]

    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ".":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ".":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ".":
        return board[0][2]

    if "." not in [j for row in board for j in row]:
        return "Tie"

    return None

def minimax(board, depth, isMaximizing):
    result = isWinner(board)
    if result is not None:
        if result == "X":
            return 1
        elif result == "O":
            return -1
        elif result == "Tie":
            return 0

    if isMaximizing:
        bestVal = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ".":
                    board[i][j] = "X"
                    bestVal = max(bestVal, minimax(board, depth+1, not isMaximizing))
                    board[i][j] = "."
        return bestVal

    else:
        bestVal = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ".":
                    board[i][j] = "O"
                    bestVal = min(bestVal, minimax(board, depth+1, not isMaximizing))
                    board[i][j] = " "
        return bestVal

def BestMove(board):
    bestVal = -1000
    bestMove = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                board[i][j] = "X"
                moveVal = minimax(board, 0, False)
                board[i][j] = "."
                if moveVal > bestVal:
                    bestVal = moveVal
                    bestMove = (i, j)
    return bestMove

def play_game():
    while True:
        result = isWinner(board)
        if result is not None:
            if result == "Tie":
                print("GAME TIE !")
            else:
                print(result + " wins!")
            break

        # X's turn
        move = BestMove(board)
        board[move[0]][move[1]] = "X"
        print("X's move:")
        for row in board:
            print(row)

        result = isWinner(board)
        if result is not None:
            if result == "Tie":
                print("Tie game!")
            else:
                print(result + " wins!")
            break

        # O's turn
        print("O's turn:")
        x, y = input("Enter coordinates (x,y): ").split(",")
        x, y = int(x), int(y)
        if board[x][y] == " ":
            board[x][y] = "O"
        else:
            print("Invalid move, try again.")

        for row in board:
            print(row)

play_game()