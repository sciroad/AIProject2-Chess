import board as bd
# Evaluate all moves and choose the best move
bestOption = ""
globalDepth = 3


def bestMove(side):
    if(side == "max"):
        x = (max(-100000000, 100000000, globalDepth))
        return bestOption
    else:
        bd.flipTheBoard()
        x = min(-100000000, 100000000, globalDepth)
        bd.flipTheBoard()
        return bestOption
# Making a move and undo the given move


def makeMove(move):
    if(move[4] != "P"):  # y1 x1 y2 x2 {oldPiece}
        y1 = int(move[0])
        x1 = int(move[1])
        y2 = int(move[2])
        x2 = int(move[3])
        bd.chessBoard[y2][x2] = bd.chessBoard[y1][x1]
        bd.chessBoard[y1][x1] = " "
    else:                               # x1 x2 {oldPiece} {newPiece} {P}
        x1 = int(move[0])
        x2 = int(move[1])
        newPiece = move[3]
        bd.chessBoard[0][x2] = newPiece
        bd.chessBoard[1][x1] = " "


def undoMove(move):
    if(move[4] != "P"):
        y1 = int(move[0])
        x1 = int(move[1])
        y2 = int(move[2])
        x2 = int(move[3])
        bd.chessBoard[y1][x1] = bd.chessBoard[y2][x2]
        bd.chessBoard[y2][x2] = move[4]
    else:                               # x1 x2 {oldPiece} {newPiece} {P}
        x1 = int(move[0])
        x2 = int(move[1])
        bd.chessBoard[0][x2] = move[2]
        bd.chessBoard[1][x1] = "P"


def min(alpha, beta, depth):
    global bestOption
    global globalDepth
    bd.flipTheBoard()
    score = (bd.calculateScore())
    bd.flipTheBoard()
    # print("score=",score)
    if(depth == 0):
        return score
    moves = bd.possibleMoves()
    # print(moves,"depth=",depth)
    for i in range(0, len(moves), 5):
        nextMove = moves[i:i+5]
        makeMove(nextMove)
        # bd.boardPrinter(bd.chessBoard)
        bd.flipTheBoard()
        childScore = max(alpha, beta, depth-1)
        bd.flipTheBoard()
        undoMove(nextMove)
        if(alpha > beta):
            return beta
        if(beta > childScore):
            beta = childScore
            if(depth == globalDepth):
                bestOption = nextMove
                # print("depth=", depth, " min ", nextMove, childScore)

    return beta


def max(alpha, beta, depth):
    global bestOption
    global globalDepth
    score = bd.calculateScore()
    if(depth == 0):
        return score
    moves = bd.possibleMoves()
    # if(depth==3):
    #     print(moves,"depth=",depth)
    for i in range(0, len(moves), 5):
        nextMove = moves[i:i+5]
        makeMove(nextMove)
        # bd.boardPrinter(bd.chessBoard)
        bd.flipTheBoard()
        
        childScore = min(alpha, beta, depth-1)
        bd.flipTheBoard()
        undoMove(nextMove)
        if(depth == globalDepth):
            print("depth=", depth, " max ", nextMove, childScore)
        if(alpha > beta):
            return alpha
        if(alpha < childScore):
            alpha = childScore
            if(depth == globalDepth):
                bestOption = nextMove
                # print("--depth=",depth," max ",nextMove,childScore)

    return alpha


# def min(alpha, beta, depth,move):
#     global bestOption
#     score=bd.calculateScore()
#     if(depth==0): return move,score
#     moves = bd.possibleMoves()
#     # print(moves,"depth=",depth)
#     for i in range(0,len(moves),5):
#         nextMove=moves[i:i+5]
#         makeMove(nextMove)
#         bd.flipTheBoard()
#         childMove,childScore=max(alpha,beta,depth-1,nextMove)
#         bd.flipTheBoard()
#         undoMove(nextMove)
#         if(beta>childScore):
#             beta=childScore
#             bestOption=childMove
#             move=childMove
#             # print("depth=",depth," min ",childMove,childScore)
#         if(alpha>beta): return move,beta

#     return move,beta


# def max(alpha, beta, depth,move):
#     global bestOption
#     score=bd.calculateScore()
#     if(depth==0): return move,score
#     moves = bd.possibleMoves()
#     if(depth==3):
#         print(moves,"depth=",depth)
#     for i in range(0,len(moves),5):
#         nextMove=moves[i:i+5]
#         makeMove(nextMove)
#         bd.flipTheBoard()
#         childMove,childScore=min(alpha,beta,depth-1,nextMove)
#         bd.flipTheBoard()
#         undoMove(nextMove)
#         if(alpha<childScore):
#             alpha=childScore
#             bestOption=childMove
#             move=childMove
#             # print("depth=",depth," max ",childMove,childScore)
#         if(alpha>beta): return move,alpha

#     return move,alpha


# def min(alpha, beta, depth):
#     if(depth == 0):
#         return bd.calculateScore()
#     bestMove = ""
#     moves = bd.possibleMoves()
#     for i in range(0, len(moves), 5):
#         nextMove = moves[i:i+5]
#         makeMove(nextMove)
#         bd.flipTheBoard()
#         childScore = max(alpha, beta, depth-1)
#         bd.flipTheBoard()
#         undoMove(nextMove)
#         if(beta > childScore):
#             alpha = childScore
#             bestMove = nextMove
#         if(alpha > beta):
#             return beta
#     return beta


# def max(alpha, beta, depth):
#     if(depth == 0):
#         return bd.calculateScore
#     bestMove = ""
#     moves = bd.possibleMoves()
#     for i in range(0, len(moves), 5):
#         nextMove = moves[i:i+5]
#         makeMove(nextMove)
#         bd.flipTheBoard()
#         childScore = min(alpha, beta, depth-1)
#         bd.flipTheBoard()
#         undoMove(nextMove)
#         if(alpha < childScore):
#             alpha = childScore
#             bestMove = nextMove
#         if(alpha > beta):
#             return alpha

#     return bestMove,alpha
