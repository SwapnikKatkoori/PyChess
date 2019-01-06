from board.square import Square
from pieces.nullPiece import nullPiece
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.rook import Rook

class Board:
    squares = {}
    black_king= King("Black", 4)
    white_king = King("White", 60)

    def __init__(self):
        pass

    def createBoard(self):
        square_color = ["light", "dark"]
        x = 0
        for i in range(64):
            self.squares[i] = Square(square_color[x % 2], i, nullPiece())
            if i % 8 == 0 and i != 0:
                x+=2
            else:
                x+=1

        self.squares[0] = Square("light", 0, Rook("Black", 0))
        self.squares[1] = Square("dark", 1, Knight("Black", 1))
        self.squares[2] = Square("light", 2, Bishop("Black", 2))
        self.squares[3] = Square("dark", 3, Queen("Black", 3))
        self.squares[4] = Square("light", 4, self.black_king)
        self.squares[5] = Square("dark", 5, Bishop("Black", 5))
        self.squares[6] = Square("light", 6, Knight("Black", 6))
        self.squares[7] = Square("dark", 7, Rook("Black", 7))
        self.squares[8] = Square("dark", 8, Pawn("Black", 8))
        self.squares[9] = Square("light", 9, Pawn("Black", 9))
        self.squares[10] = Square("dark", 10, Pawn("Black", 10))
        self.squares[11] = Square("light", 11, Pawn("Black", 11))
        self.squares[12] = Square("dark", 12, Pawn("Black", 12))
        self.squares[13] = Square("light", 13, Pawn("Black", 13))
        self.squares[14] = Square("dark", 14, Pawn("Black", 14))
        self.squares[15] = Square("light", 15, Pawn("Black", 15))

        self.squares[16] = Square("light", 16, nullPiece())
        self.squares[24] = Square("dark", 24, nullPiece())
        self.squares[32] = Square("light", 32, nullPiece())
        self.squares[40] = Square("dark", 40, nullPiece())

        self.squares[48] = Square("light", 48, Pawn("White", 48))
        self.squares[49] = Square("dark", 49, Pawn("White", 49))
        self.squares[50] = Square("light", 50, Pawn("White", 50))
        self.squares[51] = Square("dark", 51, Pawn("White", 51))
        self.squares[52] = Square("light", 52, Pawn("White", 52))
        self.squares[53] = Square("dark", 53, Pawn("White", 53))
        self.squares[54] = Square("light", 54, Pawn("White", 54))
        self.squares[55] = Square("dark", 55, Pawn("White", 55))
        self.squares[56] = Square("dark", 56, Rook("White", 56))
        self.squares[57] = Square("light", 57, Knight("White", 57))
        self.squares[58] = Square("dark", 58, Bishop("White", 58))
        self.squares[59] = Square("light", 59, Queen("White", 59))
        self.squares[60] = Square("dark", 60, self.white_king)
        self.squares[61] = Square("light", 61, Bishop("White", 61))
        self.squares[62] = Square("dark", 62, Knight("White", 62))
        self.squares[63] = Square("light", 63, Rook("White", 63))

    def printBoard(self):
        count = 0
        for i in range(64):
            print("|", end=self.squares[i].piece.toString())
            count += 1
            if count % 8 == 0:
                print("|","\n")

    def all_possible_moves(self, king_color, position_of_king):
        temp_list = []
        for i in range(64):
            if i != position_of_king:
                piece_to_check = self.squares[i].piece
                if piece_to_check.toString() != "-" and piece_to_check.toString().lower() != "k" and piece_to_check.color != king_color:
                    if piece_to_check.toString().lower() == "p":
                        pawn_captures = piece_to_check.getChecks(self)
                        print("pc:",pawn_captures)
                        temp_list+=pawn_captures
                        piece_to_check.clearLists()
                    else:
                        temp_list+=self.squares[i].piece.possibleMoves(self)
                        self.squares[i].piece.clearLists()

        return temp_list

    def in_check(self,color):
        if color == "White":
            return self.white_king.currently_in_check(self)
        else:
            return self.black_king.currently_in_check(self)