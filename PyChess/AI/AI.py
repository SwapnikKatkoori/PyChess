import random
import copy
from pieces.nullPiece import nullPiece


class AI:
    move_dictionary = {}
    def __init__(self,board):
        self.board = board
        self.best_move = None
        self.count=0
        self.best_list = []
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

    def getBestMove(self):
        pass
    def boardEval(self,board):
        point_dictionary = {"p": 10, "b": 30, "n": 30, "r": 50, "q": 90, "k": 900,
                            "P": -10, "B": -30, "N": -30, "R": -50, "Q": -90, "K": -900, "-": 0}
        total_points = 0
        for i in range(64):
            total_points+=point_dictionary[board.squares[i].piece.toString()]

        return total_points
    def fillMoveDictionary(self,board,turn):
        move_dictionary = {}
        for i in range(64):
            piece = board.squares[i].piece
            if piece.toString() != "-" and piece.color == turn:
                possible_moves = piece.possibleMoves(board)
                if possible_moves != []:
                    move_dictionary[i] = possible_moves
        return move_dictionary
    def minimax(self, board, depth, maximizingplayer, turn):
        move_dictionary=self.fillMoveDictionary(board,turn)
        self.best_list = []
        if depth==0:
            return self.boardEval(board),0

        if maximizingplayer:
            best_move = -9999999
            for key in move_dictionary:
                for move in move_dictionary[key]:
                    captured_piece = board.squares[move].piece
                    board.squares[move].piece = board.squares[key].piece
                    board.squares[move].piece.position = move
                    board.squares[key].piece = nullPiece()
                    best_move=max(best_move, self.minimax(board,depth-1,not maximizingplayer,"Black")[0])
                    self.best_list.append([key,move, best_move])
                    board.squares[key].piece = board.squares[move].piece
                    board.squares[key].piece.position=key
                    board.squares[move].piece=captured_piece
                    board.printBoard()
            print(self.best_list)
            return best_move,board.squares[key].piece,move
        else:
            best_move = 9999999
            for key in move_dictionary:
                for move in move_dictionary[key]:
                    captured_piece = board.squares[move].piece
                    board.squares[move].piece = board.squares[key].piece
                    board.squares[move].piece.position = move
                    board.squares[key].piece = nullPiece()
                    last_best = best_move
                    best_move = min(best_move, self.minimax(board, depth-1, not maximizingplayer,"White")[0])
                    self.best_list.append([key,move,best_move])
                    board.squares[key].piece = board.squares[move].piece
                    board.squares[key].piece.position = key
                    board.squares[move].piece = captured_piece
                    board.printBoard()
            print(self.best_list)

            return best_move,board.squares[self.best_list[1][0]].piece,self.best_list[1][1]