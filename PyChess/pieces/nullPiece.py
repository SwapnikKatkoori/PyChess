from pieces.piece import Piece


class nullPiece(Piece):
    color = None
    position = None

    def __init__(self):
        pass

    def toString(self):
        return "-"