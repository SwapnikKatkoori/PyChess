from pieces.piece import Piece


class Knight(Piece):
    color = None
    position = None
    capture_moves = []
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def toString(self):
        if self.color == "Black":
            return "N"
        else:
            return "n"

    def getUpRightTall(self, board):
        column = self.position % 8
        possible_moves_list = []

        if column != 7 and self.position > 14:
            move=self.position-15
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass
        return possible_moves_list

    def getUpRightLong(self,board):
        column = self.position % 8
        possible_moves_list = []

        if column<6 and self.position>7:
            move = self.position - 6
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass
        return possible_moves_list

    def getDownRightTall(self, board):
        column = self.position % 8
        possible_moves_list = []

        if column != 7 and self.position < 48:
            move = self.position + 17
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass
        return possible_moves_list

    def getDownRightLong(self, board):
        column = self.position % 8
        possible_moves_list = []

        if column < 6 and self.position < 55:
            move = self.position + 10
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass
        return possible_moves_list

    def getUpLeftTall(self, board):
        column = self.position % 8
        possible_moves_list = []

        if column != 0 and self.position > 14:
            move = self.position - 17
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass
        return possible_moves_list

    def getUpLeftLong(self,board):
        column = self.position % 8
        possible_moves_list = []

        if column>1 and self.position>7:
            move = self.position - 10
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass

        return possible_moves_list

    def getDownLeftTall(self, board):
        column = self.position % 8
        possible_moves_list = []

        if column != 0 and self.position < 48:
            move = self.position + 15
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass
        return possible_moves_list

    def getDownLeftLong(self, board):
        column = self.position % 8
        possible_moves_list = []
        if column > 1 and self.position < 55:
            move = self.position + 6
            if board.squares[move].piece.toString() == "-":
                possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass
        return possible_moves_list

    def possibleMoves(self, board):
        possible_moves_list = []
        possible_moves_list += self.getUpRightTall(board)
        possible_moves_list += self.getUpRightLong(board)
        possible_moves_list += self.getDownRightTall(board)
        possible_moves_list += self.getDownRightLong(board)

        possible_moves_list += self.getUpLeftTall(board)
        possible_moves_list += self.getUpLeftLong(board)
        possible_moves_list += self.getDownLeftTall(board)
        possible_moves_list += self.getDownLeftLong(board)

        return possible_moves_list

    def getCaptureMoves(self):
        return self.capture_moves

    def clearLists(self):
        self.capture_moves = []