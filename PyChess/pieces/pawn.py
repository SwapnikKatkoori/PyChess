from pieces.piece import Piece


class Pawn(Piece):
    color = None
    position = None
    has_moved = False
    capture_moves = []
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def toString(self):
        if self.color == "Black":
            return "P"
        else:
            return "p"

    def getUp(self, board):
        up_one = self.position - 8
        up_two = self.position - 16
        possible_moves_list =[]
        if up_one >= 0 and board.squares[up_one].piece.toString() == "-":
            possible_moves_list.append(up_one)
        if not self.has_moved:
            if up_two >= 0 and board.squares[up_two].piece.toString() == "-" and board.squares[up_one].piece.toString() == "-":
                possible_moves_list.append(up_two)
        return possible_moves_list

    def getDown(self, board):
        up_one = self.position + 8
        up_two = self.position + 16
        possible_moves_list = []
        if up_one <= 63 and board.squares[up_one].piece.toString() == "-":
            possible_moves_list.append(up_one)
        if not self.has_moved:
            if up_two <= 63 and board.squares[up_two].piece.toString() == "-" and board.squares[up_one].piece.toString() == "-":
                possible_moves_list.append(up_two)
        return possible_moves_list
    def getChecks(self,board):
        right_captures = self.getRightCapture(board)
        left_captures = self.getLeftCapture(board)
        self.clearLists()
        print("right caps", right_captures)
        all_captures = right_captures + left_captures
        return all_captures
    def getCaptures(self, board):
        possible_moves_list = []
        possible_moves_list+=self.getRightCapture(board)
        possible_moves_list+=self.getLeftCapture(board)
        return possible_moves_list
    def getRightCapture(self,board):
        column = self.position % 8
        white_move = self.position - 7
        black_move = self.position + 9
        the_check_moves = []
        possible_moves_list = []
        if column!=7 and black_move<=63 and white_move>=0:
            if self.color == "White" and board.squares[white_move].piece.toString() != "-":
                if board.squares[white_move].piece.color != self.color:
                    possible_moves_list.append(white_move)
                    self.capture_moves.append(white_move)
            else:
                the_check_moves.append(white_move)

            if self.color == "Black" and board.squares[black_move].piece.toString() != "-":
                if board.squares[black_move].piece.color != self.color:
                    possible_moves_list.append(black_move)
                    self.capture_moves.append(black_move)
            else:
                the_check_moves.append(black_move)
        return possible_moves_list
        return the_check_moves
    def getLeftCapture(self, board):
        column = self.position % 8
        white_move = self.position - 9
        black_move = self.position + 7
        the_check_moves = []
        possible_moves_list = []
        if column != 0 and black_move <= 63 and white_move >= 0:
            if self.color == "White" and board.squares[white_move].piece.toString() != "-":
                if board.squares[white_move].piece.color != self.color:
                    possible_moves_list.append(white_move)
                    self.capture_moves.append(white_move)
            else:
                the_check_moves.append(white_move)
            if self.color == "Black" and board.squares[black_move].piece.toString() != "-":
                if board.squares[black_move].piece.color != self.color:
                    possible_moves_list.append(black_move)
                    self.capture_moves.append(black_move)
            else:
                the_check_moves.append(black_move)

        return possible_moves_list
    def possibleMoves(self, board):
        possible_moves_list =[]
        if self.color == "White":
            if self.position < 48:
                self.has_moved = True
            possible_moves_list+=self.getUp(board)
        else:
            if self.position > 15:
                self.has_moved = True
            possible_moves_list+=self.getDown(board)

        possible_moves_list+=self.getCaptures(board)
        return possible_moves_list

    def getCaptureMoves(self):
        return self.capture_moves

    def clearLists(self):
        self.capture_moves = []