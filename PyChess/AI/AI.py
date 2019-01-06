import random

class AI:
    move_dictionary = {}
    def __init__(self,board):
        self.board = board
    def getRandomMove(self,turn):
        self.move_dictionary={}
        for i in range (64):
            piece = self.board.squares[i].piece
            if piece.toString()!="-" and piece.color == turn:
                possible_moves = piece.possibleMoves(self.board)
                print(possible_moves)
                if possible_moves!=[]:
                    self.move_dictionary[i] = possible_moves
        print(self.move_dictionary)
        random_square = random.choice(list(self.move_dictionary.keys()))
        random_move = random.choice(self.move_dictionary[random_square])
        return (self.board.squares[random_square].piece, random_move)

    def getBestMoveWithCapture(self,turn):
        self.move_dictionary={}
        point_dictionary = {"p": 10, "b":30, "n":30, "r":50, "q":90, "k":900}
        best_move = -999999
        best_move_tup=()
        for i in range (64):
            piece = self.board.squares[i].piece
            if piece.toString()!="-" and piece.color == turn:
                possible_moves = piece.possibleMoves(self.board)
                print(possible_moves)
                if possible_moves!=[]:
                    self.move_dictionary[i] = possible_moves
        for key in self.move_dictionary:
            for move in self.move_dictionary[key]:
                piece_to_move = self.board.squares[key].piece
                capture_piece = self.board.squares[move].piece
                if capture_piece.toString()!= "-" and capture_piece.color!=piece_to_move.color:
                    move_value = point_dictionary[capture_piece.toString().lower()]
                    if move_value>best_move:
                        best_move = move_value
                        best_move_tup = (piece_to_move, move)

        if best_move_tup==():
            return self.getRandomMove(turn)
        else:
            print(best_move_tup)
            return (best_move_tup[0], best_move_tup[1])