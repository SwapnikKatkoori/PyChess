from pieces.piece import Piece


class Rook(Piece):
    color = None
    position = None
    capture_moves = []
    def __init__(self,color, position):
        self.color = color
        self.position = position

    def toString(self):
        if self.color == "Black":
            return "R"
        else:
            return "r"

    def getUp(self, board):
        move = self.position - 8
        possible_moves_list=[]

        while move>=0:
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
                move = move - 8
            elif board.squares[move].piece.color == self.color:
                break
            else:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
                break
        return possible_moves_list

    def getDown(self, board):
        move = self.position + 8
        possible_moves_list=[]

        while move <= 63:
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
                move = move + 8
            elif board.squares[move].piece.color == self.color:
                break
            else:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
                break
        return possible_moves_list

    def getLeft(self, board):
        move = self.position - 1
        number_of_moves = self.position % 8
        possible_moves_list=[]

        for i in range(number_of_moves):
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
                move = move - 1
            elif board.squares[move].piece.color == self.color:
                break
            else:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
                break
        return possible_moves_list

    def getRight(self, board):
        move = self.position + 1
        number_of_moves =7 - (self.position % 8)
        possible_moves_list=[]
        for i in range(number_of_moves):
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
                move = move + 1
            elif board.squares[move].piece.color == self.color:
                break
            else:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
                break
        return possible_moves_list

    def possibleMoves(self, board):
        possible_moves_list = []
        possible_moves_list+=self.getUp(board)
        possible_moves_list +=self.getDown(board)
        possible_moves_list +=self.getLeft(board)
        possible_moves_list +=self.getRight(board)
        return possible_moves_list

    def getCaptureMoves(self):
        return self.capture_moves

    def clearLists(self):
        self.capture_moves = []