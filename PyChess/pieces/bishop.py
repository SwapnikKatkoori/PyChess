from pieces.piece import Piece
import math

class Bishop(Piece):
    color = None
    position = None
    possible_moves_list = []
    capture_moves = []

    def __init__(self, color, position):
        self.color = color
        self.position = position

    def toString(self):
        if self.color == "Black":
            return "B"
        else:
            return "b"

    def getUpRight(self,board):
        last_column = self.position % 8
        column = self.position % 8 + 1
        move = self.position - 7
        possible_moves_list=[]

        if last_column != 7 and move >= 0:
            while (column-1) == last_column and move >=0:
                if board.squares[move].piece.toString() == "-":
                    possible_moves_list.append(move)
                    move = move - 7
                    last_column = column
                    column = move % 8
                elif board.squares[move].piece.color != self.color:
                    possible_moves_list.append(move)
                    self.capture_moves.append(move)
                    break
                else:
                    break
        return possible_moves_list

    def getDownRight(self, board):
        last_column = self.position % 8
        column = self.position % 8 + 1
        move = self.position + 9
        possible_moves_list=[]

        if (last_column != 7) and (move <= 63) :
            while (column - 1) == last_column and move<=63:
                print(move)
                if board.squares[move].piece.toString() == "-":
                    possible_moves_list.append(move)
                    move = move + 9
                    last_column = column
                    column = move % 8
                elif board.squares[move].piece.color != self.color:
                    possible_moves_list.append(move)
                    self.capture_moves.append(move)
                    break
                else:
                    break
        return possible_moves_list

    #Check up left and down left after. column and last column should be different
    def getUpLeft(self, board):
        last_column = self.position % 8
        column = self.position % 8 - 1
        move = self.position - 9
        possible_moves_list=[]

        if last_column != 0 and move >= 0:
            while (column + 1) == last_column and move>=0:
                if board.squares[move].piece.toString() == "-":
                    possible_moves_list.append(move)
                    move = move - 9
                    last_column = column
                    column = move % 8
                elif board.squares[move].piece.color != self.color:
                    possible_moves_list.append(move)
                    self.capture_moves.append(move)
                    break
                else:
                    break
        return possible_moves_list

    def getDownLeft(self, board):
        last_column = self.position % 8
        column = self.position % 8 - 1
        move = self.position + 7
        possible_moves_list=[]

        if last_column != 0 and move <= 63:
            while (column + 1) == last_column and move<=63:
                if board.squares[move].piece.toString() == "-":
                    possible_moves_list.append(move)
                    move = move + 7
                    last_column = column
                    column = move % 8
                elif board.squares[move].piece.color != self.color:
                    possible_moves_list.append(move)
                    self.capture_moves.append(move)
                    break
                else:
                    break
        return possible_moves_list

    def possibleMoves(self,board):
        possible_moves_list=[]
        if self.position % 8 != 7:
            possible_moves_list+=self.getUpRight(board)
            possible_moves_list+=self.getDownRight(board)
        if self.position % 8 != 0:
            possible_moves_list+=self.getUpLeft(board)
            possible_moves_list+=self.getDownLeft(board)
        return possible_moves_list

    def getCaptureMoves(self):
        return self.capture_moves

    def clearLists(self):
        self.capture_moves = []