#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 12:51:39 2018

@author: swapnikkatkoori1
"""

import pygame
import math
from pieces.nullPiece import nullPiece
from board.board import Board
from AI.AI import AI

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

chessBoard = Board()
boardCoordinatesToPos= {}
chessBoard.createBoard()
chessBoard.printBoard()
quitGame = False
light = (143,155,175)
dark = (102,0,204)
piecesOnBoard = []
selected_piece_string = "-"
selected_piece_pos = ()
selected_square_color = ""
is_a_capture = False
capture_square_color = None


def fillBCTP():
    pos = 0
    for i in range(1,9):
        for x in range(1,9):
            boardCoordinatesToPos[(i,x)] = pos
            pos+=1
    print(boardCoordinatesToPos)
def createBoard():
    x=0
    y=0
    pos = 0
    for i in range(8):
        x=0
        for j in range(8):
            if (i+j)%2==0:
                pygame.draw.rect(screen,light,[x,y,100,100])
            else:
                pygame.draw.rect(screen, dark, [x, y, 100, 100])

            if chessBoard.squares[pos].piece.toString() != "-":
                pieceString = chessBoard.squares[pos].piece.color[0].lower() + chessBoard.squares[pos].piece.toString().lower()
                pieceToPlace = pygame.image.load("./GUIart/" + pieceString + ".png")
                pieceToPlace = pygame.transform.scale(pieceToPlace, (100, 100))
                screen.blit(pieceToPlace, (x,y))
            x+=100
            pos+=1

        y+=100

def updatePiecePosition(x, y, new_x, new_y, piece, square_color, is_a_capture, capture_square_color,turn):
    if square_color == "light":
        square_color = light
    else:
        square_color = dark
    updateBoard(x,y,new_x, new_y)
    if chessBoard.in_check(turn):
        updateBoard(new_x, new_y, x, y)
        return False
    pieceToPlace = pygame.image.load("./GUIart/" + piece + ".png")
    pieceToPlace = pygame.transform.scale(pieceToPlace, (100, 100))
    pygame.draw.rect(screen, square_color, [x, y, 100, 100])
    if is_a_capture:
        if capture_square_color == "light":
            capture_square_color = light
        else:
            capture_square_color = dark
        pygame.draw.rect(screen, capture_square_color, [new_x, new_y, 100, 100])

    screen.blit(pieceToPlace,(new_x,new_y))
    return True
def updateBoard(x, y, new_x, new_y):


    initial_position = getPos(int(y/100)+1,int(x/100)+1)

    new_position = getPos(int(new_y/100)+1, int(new_x/100)+1)

    print("new_position :",new_position, (new_x/100)+1, (new_y/100)+1)
    chessBoard.squares[new_position].piece = chessBoard.squares[initial_position].piece
    chessBoard.squares[new_position].piece.position = new_position
    chessBoard.squares[initial_position].piece = nullPiece()


def getPos(row, column):
    return boardCoordinatesToPos[(row, column)]

def posToCoordinates(position):
    column = position % 8
    row = math.floor(position/8)
    x = column * 100
    y  = row *100
    return (x,y)
createBoard()
fillBCTP()


turn = "White"
player_color = "White"
gameAi = AI(chessBoard)
while not quitGame:
    x=0
    y=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()
        if turn != player_color:
            while(turn!=player_color):
                random_move_tup = gameAi.getBestMoveWithCapture(turn)
                print("rand move",random_move_tup[0].position,random_move_tup[1])
                coordinates_from = posToCoordinates(random_move_tup[0].position)
                print("from",coordinates_from)
                coordinates_to= posToCoordinates(random_move_tup[1])
                print("to:",coordinates_to)
                piece_string = random_move_tup[0].color[0].lower()+random_move_tup[0].toString()[0].lower()
                square_color = chessBoard.squares[random_move_tup[0].position].color
                to_square_color = chessBoard.squares[random_move_tup[1]].color
                if chessBoard.squares[random_move_tup[1]].piece.toString() != "-" and chessBoard.squares[random_move_tup[1]].piece.color != random_move_tup[0].color:
                    is_a_capture = True
                else:
                    is_a_capture=False
                if updatePiecePosition(coordinates_from[0],coordinates_from[1], coordinates_to[0], coordinates_to[1], piece_string, square_color, is_a_capture, to_square_color, turn):
                    turn = player_color

        if event.type == pygame.MOUSEBUTTONDOWN:
            clickedPosition = event.pos
            column = math.ceil(clickedPosition[0] / 100)
            row = math.ceil(clickedPosition[1] / 100)
            squareClicked = getPos(row, column)

            if selected_piece_string != "-":
                selected_piece.clearLists()

                if squareClicked in selected_piece.possibleMoves(chessBoard) and selected_piece.color == turn:
                    if squareClicked in selected_piece.getCaptureMoves():
                        is_a_capture = True
                        capture_square_color = chessBoard.squares[squareClicked].color
                    else:
                        is_a_capture = False
                    x = (selected_piece_pos[0]-1)*100
                    y = (selected_piece_pos[1]-1)*100
                    new_x = (column-1)*100
                    new_y = (row-1)*100
                    if updatePiecePosition(x, y, new_x,new_y,selected_piece_string, selected_square_color, is_a_capture, capture_square_color, turn):
                        if turn =="White":
                            turn = "Black"
                        else:
                            turn = "White"
                selected_piece_string = "-"

            else:
                if chessBoard.squares[squareClicked].piece.toString() != "-":
                    selected_square_color = chessBoard.squares[squareClicked].color
                    selected_piece = chessBoard.squares[squareClicked].piece
                    selected_piece_string = chessBoard.squares[squareClicked].piece.color[0].lower() + chessBoard.squares[squareClicked].piece.toString().lower()
                    selected_piece_pos = (column, row)

    pygame.display.update()


