# Amirmohammad Khosravi      810198386
from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    bestMove = None
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    playerColor = WHITE if max_player else RED
    minOrMaxEval = float('-inf') if max_player else float('inf')
    for move in getAllMoves(position, playerColor, game):
        evaluation = minimax(move, depth-1, not max_player, game)[0]
        minOrMaxEval = max(minOrMaxEval, evaluation) if max_player else min(minOrMaxEval, evaluation)
        if minOrMaxEval == evaluation:
            bestMove = move
    
    return minOrMaxEval, bestMove
    
def simulateMove(piece, move, board, game, skip):
    if skip:
        board.move(piece, move[0], move[1])
        board.remove(skip)
        return board
    board.move(piece, move[0], move[1])
    return board

def getAllMoves(board, color, game):
    allMoves = []
    for piece in board.getAllPieces(color):
        validMoves = board.getValidMoves(piece)
        for move, skip in validMoves.items():
            tempBoard = deepcopy(board)
            allMoves.append(simulateMove(tempBoard.getPiece(piece.row, piece.col), move, tempBoard, game, skip))
    return allMoves
