
# https://github.com/Myrausman/TIC-TAC-TOE
# my 2nd semester oop project was tic tac toe game which I implemented in gui pygame
# i wanted to try using the minmax algoritm but as its logics were complicated and i couldnt really understand so i skipped this algo and let the computer play randomly
# through this algo i can modify my project 

class tictactoe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.player = 'X'
        self.computer = 'O'

    def play(self):
        while True:
            if self.player == "O":
                self.print_board()
                move = int(input("Where would you like to place " + self.player + " (1-9)? ")) - 1
                if self.validMove(move):
                    self.board[move] = self.player
                    if self.winner():
                        self.print_board()
                        print(self.player + " wins!")
                        return
                    elif self.board_full():
                        self.print_board()
                        print("Tie!")
                        return
                    self.player, self.computer = self.computer, self.player
                else:
                    print("Invalid move.")
            else:
                move = self.gametree(self.board, self.computer)
                self.board[move] = self.player
                print("Computer places " + self.computer + " at position", move + 1)

                if self.winner():
                    self.print_board()
                    print(self.player + " wins!")
                    return
                elif self.board_full():
                    self.print_board()
                    print("Tie!")
                    return
                self.player, self.computer = self.computer, self.player

    def gametree(self, board, player):
        if self.winner():
            if player == 'X':
                return 1
            else:
                return -1
        elif self.board_full():
            return 0

        best_score = None
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                if player == 'X':
                    score = self.gametree(board, 'o')
                else:
                    score = self.gametree(board, 'x')
                board[i] = ' '

                if best_score is None or (player == 'X' and score > best_score) or (player == 'O' and score < best_score):
                    best_score = score
                    best_move = i

        if best_move is None:
            return 0
        else:
            return best_move
    


    def validMove(self, move):
        if move < 0 or move > 8:
            return False
        if self.board[move] != ' ':
            return False
        return True

    def winner(self):
        for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def board_full(self):
        return not ' ' in self.board

    def print_board(self):
        print(" " + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---+---+---")
        print(" " + self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---+---+---")
        print(" " + self.board[6] + " | " + self.board[7] + " | " + self.board[8])
    
    
game = tictactoe()
game.play()
