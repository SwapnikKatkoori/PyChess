from pieces.piece import Piece
import math

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
    #possible error on line 35, check for pawn
    def get_initial_moves(self,board):
        column = self.position%8
        row = math.floor(self.position/7)
        initial_moves_list=[]
        if column != 7 and self.position>7:
            initial_moves_list.append(self.position-7)
        if column !=7:
            initial_moves_list.append(self.position+1)
        if column !=7 and self.position<55:
            initial_moves_list.append(self.position+9)
        if column!=0:
            initial_moves_list.append(self.position-1)
        if row !=0 and self.position-7>0:
            initial_moves_list.append(self.position-8)
        if self.position<55:
            initial_moves_list.append(self.position+8)
        if column!=0 and self.position>7 and self.position-7>0:
            initial_moves_list.append(self.position-9)
        if column!=0 and self.position<55:
            initial_moves_list.append(self.position+7)

        return initial_moves_list

    def inCheck(self,board,position):
        #check up and down

        up_move = position-8
        temp_count = 0
        while up_move > 0:
            piece=board.squares[up_move].piece
            print("cutting here 1 ", position)
            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                up_move -= 8
                continue

            if piece.color != self.color and (piece.toString().lower()=="q" or piece.toString().lower()=="r"):
                if temp_count == 0:
                    self.capture_moves.append(up_move)
                return True
            if (piece.color == self.color and piece.toString != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="n" or piece.toString().lower()=="k" or piece.toString().lower()=="b":
                if temp_count == 0 and piece.toString()!="_" and piece.color!=self.color:
                    self.capture_moves.append(up_move)
                break
            temp_count+=1
            up_move-=8

        down_move = position+8
        temp_count = 0
        while down_move<64:
            piece = board.squares[down_move].piece
            print("cutting here 2 ", position)

            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                down_move += 8
                continue
            if piece.color != self.color and (piece.toString().lower() == "q" or piece.toString().lower() == "r"):
                if temp_count == 0:
                    self.capture_moves.append(down_move)
                return True
            if (piece.color == self.color and piece.toString() != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="n" or piece.toString().lower()=="k" or piece.toString().lower()=="b":
                if temp_count == 0 and piece.toString()!="_" and piece.color!=self.color:
                    self.capture_moves.append(down_move)
                break
            print(piece.toString())
            temp_count +=1
            down_move +=8

        right_move = position+1
        temp_count = 0
        while (right_move-1)%8 < 7:
            print(right_move)
            print("cutting here 3 ", position)

            piece = board.squares[right_move].piece
            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                right_move += 1
                continue
            if piece.color != self.color and (piece.toString().lower() == "q" or piece.toString().lower() == "r"):
                if temp_count == 0:
                    self.capture_moves.append(right_move)
                return True
            if (piece.color == self.color and piece.toString != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="n" or piece.toString().lower()=="k" or piece.toString().lower()=="b":
                if temp_count == 0 and piece.toString()!="_" and piece.color!=self.color:
                    self.capture_moves.append(right_move)
                break
            temp_count +=1
            right_move += 1

        left_move = position - 1
        temp_count = 0
        while (left_move+1) % 8 > 0:
            print("cutting here 4", position)

            piece = board.squares[left_move].piece
            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                left_move -= 1
                continue
            if piece.color != self.color and (piece.toString().lower() == "q" or piece.toString().lower() == "r"):
                if temp_count==0:
                    self.capture_moves.append(left_move)
                return True
            if (piece.color == self.color and piece.toString != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="k" or piece.toString().lower()=="n" or piece.toString().lower()=="b":
                break
            temp_count +=1
            left_move -= 1

        up_right_move = position - 7
        temp_count = 0
        while position%8 < 7 and up_right_move>0:
            piece = board.squares[up_right_move].piece
            print("cutting here 5 ", position, up_right_move, piece.toString())
            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                temp_count += 1
                up_right_move -= 7
                continue
            if piece.color != self.color and (piece.toString().lower() == "q" or piece.toString().lower() == "b"):
                print("problem 1", position, up_right_move)
                if temp_count==0:
                    self.capture_moves.append(up_right_move)
                return True
            if temp_count == 0 and piece.color != self.color and piece.toString().lower() == "p" and self.color=="White":
                print("problem 2 ", position)
                if temp_count == 0:
                    self.capture_moves.append(up_right_move)
                return True
            if (piece.color == self.color and piece.toString != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="r" or piece.toString().lower()=="n" or piece.toString().lower()=="k":
                if temp_count == 0 and piece.toString()!="_" and piece.color!=self.color:
                    self.capture_moves.append(up_right_move)
                break
            if up_right_move%8 >=7:
                break
            temp_count+=1
            up_right_move -= 7

        down_right_move = position + 9
        temp_count = 0
        while position < 55 and down_right_move<=63:
            print("cutting here 6 ", position)
            piece = board.squares[down_right_move].piece
            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                temp_count += 1
                down_right_move += 9
                continue
            if piece.color != self.color and (piece.toString().lower() == "q" or piece.toString().lower() == "b"):
                if temp_count == 0:
                    self.capture_moves.append(down_right_move)
                return True
            if temp_count == 0 and piece.color != self.color and piece.toString().lower() == "p" and self.color=="Black":
                if temp_count == 0:
                    self.capture_moves.append(down_right_move)
                return True
            if (piece.color == self.color and piece.toString != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="n" or piece.toString().lower()=="k" or piece.toString().lower()=="r":
                if temp_count == 0 and piece.toString()!="_" and piece.color!=self.color:
                    self.capture_moves.append(down_right_move)
                break
            if down_right_move %8 >=7:
                break
            temp_count += 1
            down_right_move += 9

        down_left_move = position + 7
        temp_count = 0
        while position < 57 and down_left_move<=63:
            print("cutting here 7 ", position)

            piece = board.squares[down_left_move].piece
            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                temp_count += 1
                down_left_move += 7
                continue
            if piece.color != self.color and (piece.toString().lower() == "q" or piece.toString().lower() == "b"):
                print("problem 7 ", position, down_left_move)

                if temp_count == 0:
                    self.capture_moves.append(down_left_move)
                return True
            if temp_count == 0 and piece.color != self.color and piece.toString().lower() == "p" and self.color=="Black":
                print("problem 7 ", position, down_left_move)

                if temp_count == 0:
                    self.capture_moves.append(down_left_move)
                return True
            if (piece.color == self.color and piece.toString != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="n" or piece.toString().lower()=="k" or piece.toString().lower()=="r":
                if temp_count == 0 and piece.toString()!="_" and piece.color!=self.color:
                    self.capture_moves.append(down_left_move)
                break
            if down_left_move%8<=0:
                break
            temp_count += 1
            down_left_move += 7

        up_left_move = position - 9
        temp_count = 0
        while position > 7 and up_left_move>=0:
            piece = board.squares[up_left_move].piece
            print("cutting here 8 ", position, up_left_move)

            if piece.toString().lower() == self.toString().lower():
                if piece.toString()!=self.toString() and temp_count == 0:
                    return True
                temp_count += 1
                up_left_move -= 9
                continue

            if piece.color != self.color and (piece.toString().lower() == "q" or piece.toString().lower() == "b"):
                if temp_count == 0:
                    self.capture_moves.append(up_left_move)
                return True
            if temp_count == 0 and piece.color != self.color and piece.toString().lower() == "p" and self.color=="White":
                if temp_count == 0:
                    self.capture_moves.append(up_left_move)
                return True
            if (piece.color == self.color and piece.toString != self.toString()) or piece.toString().lower()=="p" or piece.toString().lower()=="n" or piece.toString().lower()=="k" or piece.toString().lower()=="r":
                if temp_count == 0 and piece.toString()!="_" and piece.color!=self.color:
                    self.capture_moves.append(up_left_move)
                break
            if up_left_move%8<=0:
                break
            temp_count+=1
            up_left_move -= 9

        up_right_tall = position - 15
        if position%8 != 7 and position > 14:
            if board.squares[up_right_tall].piece.toString().lower()=="n" and board.squares[up_right_tall].piece.color != self.color:
                return True

        up_right_long = position - 6
        if position%8 < 6 and position > 7:
            if board.squares[up_right_long].piece.toString().lower()=="n" and board.squares[up_right_long].piece.color != self.color:
                return True

        down_right_tall = position + 17
        if position % 8 != 7 and position < 48:
            if board.squares[down_right_tall].piece.toString().lower() == "n" and board.squares[down_right_tall].piece.color != self.color:
                return True

        down_right_long = position + 10
        if position % 8 < 6 and position < 55:
            if board.squares[down_right_long].piece.toString().lower() == "n" and board.squares[down_right_long].piece.color != self.color:
                return True

        up_left_tall = position - 17
        if position % 8 != 0 and position > 16:
            if board.squares[up_left_tall].piece.toString().lower() == "n" and board.squares[up_left_tall].piece.color != self.color:
                return True

        up_left_long = position - 10
        if position % 8 > 1 and position > 7:
            if board.squares[up_left_long].piece.toString().lower() == "n" and board.squares[up_left_long].piece.color != self.color:
                return True

        down_left_tall = position + 15
        if position % 8 != 0 and self.position < 48:
            if board.squares[down_left_tall].piece.toString().lower() == "n" and board.squares[down_left_tall].piece.color != self.color:
                return True

        down_left_long = position + 6
        if position % 8 > 1 and position < 55:
            if board.squares[down_left_long].piece.toString().lower() == "n" and board.squares[down_left_long].piece.color != self.color:
                return True


        return False

    def possibleMoves(self,board):
        possible_moves=[]
        initial_moves = self.get_initial_moves(board)
        for i in initial_moves:
            if not self.inCheck(board,i) and board.squares[i].piece.color!=self.color:
                print(i)
                possible_moves.append(i)
        return possible_moves

    def currently_in_check(self,board):
        return self.inCheck(board,self.position)
    def getCaptureMoves(self):
        return self.capture_moves

    def clearLists(self):
        self.possible_moves_list = []
        self.capture_moves = []
