from pieces.piece import Piece


class King(Piece):
    color = None
    position = None
    possible_moves_list = []
    capture_moves = []
    in_check = False
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def toString(self):
        if self.color == "Black":
            return "K"
        else:
            return "k"

    def getUpRight(self,board):
        last_column = self.position % 8
        column = self.position % 8 + 1
        move = self.position - 7

        if last_column != 7 and move >= 0:
            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)

            else:
                pass


    def getDownRight(self, board):
        last_column = self.position % 8
        column = self.position % 8 + 1
        move = self.position + 9

        if last_column != 7 and move <= 63 :
            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)

            else:
                pass

    def getUpLeft(self, board):
        last_column = self.position % 8
        column = self.position % 8 - 1
        move = self.position - 9

        if last_column != 0 and move >= 0:

            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)
            elif board.squares[move].piece.color != self.color:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)
            else:
                pass

    def getDownLeft(self, board):
        last_column = self.position % 8
        move = self.position + 7

        if last_column != 0 and move <= 63:
            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)

            elif board.squares[move].piece.color != self.color:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)

            else:
                pass
    def getUp(self, board):
        move = self.position - 8
        if move >=0:
            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)
            elif board.squares[move].piece.color == self.color:
                pass
            else:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)




    def getDown(self, board):
        move = self.position + 8
        if move <= 63:
            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)
            elif board.squares[move].piece.color == self.color:
                pass
            else:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)



    def getLeft(self, board):
        move = self.position - 1
        column = self.position % 8
        if column > 0:
            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)
                move = move - 1
            elif board.squares[move].piece.color == self.color:
                pass
            else:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)



    def getRight(self, board):
        move = self.position + 1
        column = self.position % 8
        if column < 7:
            if board.squares[move].piece.toString() == "-":
                self.possible_moves_list.append(move)
            elif board.squares[move].piece.color == self.color:
                pass
            else:
                self.possible_moves_list.append(move)
                self.capture_moves.append(move)

    def inCheck(self,board):
        #check the diagonal and see if a bishop, pawn, or Queen is attacking
    def possibleMoves(self, board):
        if self.position % 8 != 7:
            self.getUpRight(board)
            self.getDownRight(board)
        if self.position % 8 != 0:
            self.getUpLeft(board)
            self.getDownLeft(board)
        self.getUp(board)
        self.getDown(board)
        self.getLeft(board)
        self.getRight(board)
        return self.possible_moves_list

    def getCaptureMoves(self):
        return self.capture_moves

    def clearLists(self):
        self.possible_moves_list = []
        self.capture_moves = []

    def getUpRight(self, board):
        last_column = self.position % 8
        column = self.position % 8 + 1
        move = self.position - 7
        count = 0
        temp_list = []
        if last_column != 7 and move >= 0:
            while (column - 1) == last_column and move >= 0:
                if board.squares[move].piece.toString() == "-":
                    temp_list.append(move)
                    move = move - 7
                    last_column = column
                    column = move % 8
                    count += 1
                elif board.squares[move].piece.color != self.color and count == 0:
                    print(move)
                    temp_list.append(move)
                    self.capture_moves.append(move)
                    break
                elif board.squares[move].piece.color != self.color:
                    piece_at_spot = board.squares[move].piece.toString().lower()
                    if piece_at_spot == "q" or piece_at_spot == "b":
                        temp_list = []
                        self.in_check = True
                        self.diagonal_left_checked = True
                    break
                else:
                    break

        return temp_list

    def getDownRight(self, board):
        last_column = self.position % 8
        column = self.position % 8 + 1
        move = self.position + 9
        count = 0
        temp_list = []

        if last_column != 7 and move <= 63:
            while (column - 1) == last_column and move <= 63:
                if board.squares[move].piece.toString() == "-":
                    temp_list.append(move)
                    move = move + 9
                    last_column = column
                    column = move % 8
                    count += 1
                elif board.squares[move].piece.color != self.color and count == 0:
                    temp_list.append(move)
                    self.capture_moves.append(move)
                    break
                elif board.squares[move].piece.color != self.color:
                    piece_at_spot = board.squares[move].piece.toString().lower()
                    if piece_at_spot == "q" or piece_at_spot == "b":
                        temp_list = []
                        self.in_check = True
                        self.diagonal_right_checked = True
                        # if self.color == "Black" and piece_at_spot == "p":
                        #     temp_list = []
                        #     self.in_check = True
                        # break

                    break
                else:
                    break

        return temp_list

    def getUpLeft(self, board):
        last_column = self.position % 8
        column = self.position % 8 - 1
        move = self.position - 9
        count = 0
        temp_list = []
        if last_column != 0 and move >= 0:
            while (column + 1) == last_column and move >= 0:
                if board.squares[move].piece.toString() == "-":
                    temp_list.append(move)
                    move = move - 9
                    last_column = column
                    column = move % 8
                    count += 1
                elif board.squares[move].piece.color != self.color and count == 0:
                    temp_list.append(move)
                    self.capture_moves.append(move)
                    break
                elif board.squares[move].piece.color != self.color:
                    piece_at_spot = board.squares[move].piece.toString().lower()
                    if piece_at_spot == "q" or piece_at_spot == "b":
                        temp_list = []
                        self.in_check = True
                        self.diagonal_right_checked = True
                    break
                else:
                    break

        return temp_list

    def getDownLeft(self, board):
        last_column = self.position % 8
        column = self.position % 8 - 1
        move = self.position + 7
        count = 0
        temp_list = []

        if last_column != 0 and move <= 63:
            while (column + 1) == last_column and move <= 63:
                if board.squares[move].piece.toString() == "-":
                    temp_list.append(move)
                    move = move + 7
                    last_column = column
                    column = move % 8
                    count += 1
                elif board.squares[move].piece.color != self.color and count == 0:
                    temp_list.append(move)
                    self.capture_moves.append(move)
                    break
                elif board.squares[move].piece.color != self.color:
                    piece_at_spot = board.squares[move].piece.toString().lower()
                    if piece_at_spot == "q" or piece_at_spot == "b":
                        temp_list = []
                        self.in_check = True
                        self.diagonal_left_checked = True
                    break
                else:
                    break
        return temp_list

    def getUp(self, board):
        move = self.position - 8
        count = 0
        temp_list = []
        while move >= 0:
            if board.squares[move].piece.toString() == "-":
                temp_list.append(move)
                move = move - 8
                count += 1
            elif board.squares[move].piece.color != self.color and count == 0:
                temp_list.append(move)
                self.capture_moves.append(move)
                break
            elif board.squares[move].piece.color != self.color:
                piece_at_spot = board.squares[move].piece.toString().lower()
                if piece_at_spot == "q" or piece_at_spot == "r":
                    temp_list = []
                    self.in_check = True
                    self.vertical_checked = True
                break


            else:
                break

        return temp_list

    def getDown(self, board):
        move = self.position + 8
        count = 0
        temp_list = []
        while move <= 63:
            if board.squares[move].piece.toString() == "-":
                temp_list.append(move)
                move = move + 8
                count += 1
            elif board.squares[move].piece.color != self.color and count == 0:
                temp_list.append(move)
                self.capture_moves.append(move)
                break
            elif board.squares[move].piece.color != self.color:
                piece_at_spot = board.squares[move].piece.toString().lower()
                if piece_at_spot == "q" or piece_at_spot == "r":
                    temp_list = []
                    self.in_check = True
                    self.vertical_checked = True
                break

            else:

                break

        return temp_list

    def getLeft(self, board):
        move = self.position - 1
        count = 0
        temp_list = []
        number_of_moves = self.position % 8
        for i in range(number_of_moves):
            if board.squares[move].piece.toString() == "-":
                temp_list.append(move)
                move = move - 1
                count += 1
            elif board.squares[move].piece.color != self.color and count == 0:
                temp_list.append(move)
                self.capture_moves.append(move)
                break
            elif board.squares[move].piece.color != self.color:
                piece_at_spot = board.squares[move].piece.toString().lower()
                if piece_at_spot == "q" or piece_at_spot == "r":
                    temp_list = []
                    self.in_check = True
                    self.horizontal_checked = True
                break

            else:
                break

        return temp_list

    def getRight(self, board):
        move = self.position + 1
        count = 0
        temp_list = []
        number_of_moves = 7 - (self.position % 8)
        for i in range(number_of_moves):
            if board.squares[move].piece.toString() == "-":
                temp_list.append(move)
                move = move + 1
                count += 1
            elif board.squares[move].piece.color != self.color:
                temp_list.append(move)
                self.capture_moves.append(move)
                break
            elif board.squares[move].piece.color != self.color:
                piece_at_spot = board.squares[move].piece.toString().lower()
                if piece_at_spot == "q" or piece_at_spot == "r":
                    temp_list = []
                    self.in_check = True
                    self.horizontal_checked = True
                break

            else:
                break

        return temp_list

    def remove_checked_moves(self, board, possible_moves):
        all_possible_moves = board.all_possible_moves(self.color, self.position)
        for i in possible_moves:
            if i in all_possible_moves:
                if i not in self.capture_moves:
                    print("i: ", i)
                    possible_moves.remove(i)
        return possible_moves

    def possibleMoves(self, board):
        temp_list = []
        if self.position % 8 != 7:
            if not self.diagonal_left_checked:
                up_right = self.getUpRight(board)
                if len(up_right) > 0:
                    temp_list += [up_right[0]]
            if not self.diagonal_right_checked:
                down_right = self.getDownRight(board)
                if len(down_right) > 0:
                    temp_list += [down_right[0]]
        if self.position % 8 != 0:
            if not self.diagonal_right_checked:
                up_left = self.getUpLeft(board)
                if len(up_left) > 0:
                    temp_list += [up_left[0]]
            if not self.diagonal_left_checked:
                down_left = self.getDownLeft(board)
                if len(down_left) > 0:
                    temp_list += [down_left[0]]
        if not self.vertical_checked:
            get_up = self.getUp(board)
            print(get_up)
            if len(get_up) > 0:
                temp_list += [get_up[0]]

        if not self.vertical_checked:
            get_down = self.getDown(board)
            if len(get_down) > 0:
                temp_list += [get_down[0]]
        if not self.horizontal_checked:
            get_left = self.getLeft(board)
            if len(get_left) > 0:
                temp_list += [get_left[0]]
        if not self.horizontal_checked:
            get_right = self.getRight(board)
            if len(get_right) > 0:
                temp_list += [get_right[0]]

        temp_list = self.remove_checked_moves(board, temp_list)
        self.horizontal_checked = False
        self.diagonal_right_checked = False
        self.diagonal_left_checked = False
        self.vertical_checked = False
        return temp_list

    def getCaptureMoves(self):
        return self.capture_moves

    def clearLists(self):
        self.possible_moves_list = []
        self.capture_moves = []




