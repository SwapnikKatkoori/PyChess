from pieces.piece import Piece


class Queen(Piece):
    color = None
    position = None
    possible_moves_list = []
    capture_moves = []
    def __init__(self,color, position):
        self.color = color
        self.position = position

    def toString(self):
        if self.color == "Black":
            return "Q"
        else:
            return "q"
    def getUpRight(self,board):
        last_column = self.position % 8
        column = self.position % 8 + 1
        move = self.position - 7
        possible_moves_list = []
        if last_column != 7 and move >= 0:
            while (column-1) == last_column and move>=0:
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
        possible_moves_list = []

        if last_column != 7 and move <= 63 :
            while (column - 1) == last_column and move<=63:
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

    def getUpLeft(self, board):
        last_column = self.position % 8
        column = self.position % 8 - 1
        move = self.position - 9
        possible_moves_list = []

        if last_column != 0 and move >= 0:
            while (column + 1) == last_column and move >= 0:
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
        possible_moves_list = []

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

    def getUp(self, board):
        move = self.position - 8
        possible_moves_list = []

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
        possible_moves_list = []

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
        possible_moves_list = []

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
        number_of_moves = 7 - (self.position % 8)
        possible_moves_list = []

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
    def possibleMoves(self,board):
        possible_moves_list=[]
        if self.position % 8 != 7:
            possible_moves_list+=self.getUpRight(board)
            possible_moves_list+=self.getDownRight(board)
        if self.position % 8 != 0:
            possible_moves_list+=self.getUpLeft(board)
            possible_moves_list+=self.getDownLeft(board)
        possible_moves_list+=self.getUp(board)
        possible_moves_list+=self.getDown(board)
        possible_moves_list+=self.getLeft(board)
        possible_moves_list+=self.getRight(board)
        return possible_moves_list

    def getCaptureMoves(self):
        return self.capture_moves
    def clearLists(self):
        possible_moves_list = []
        self.capture_moves = []