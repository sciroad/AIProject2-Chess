import board as bd
# Evaluate all moves and choose the best move
bestOption = ""
globalDepth = 3
moveColumn = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,
              "H": 7, "1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}


def convertMove(move):
    convertedMove=""

    if(move=="R---C" and move =="L---C"):
        return move
    elif(len(move)==5 ):
        y1=(8-int(move[1]))
        x1=moveColumn[move[0]]
        y2=(8-int(move[3]))
        x2=moveColumn[move[2]]
        if(bd.chessBoard[y1][x1]=="P" and y1==1):
            convertedMove+=str(y1)
            convertedMove+=str(y2)
            convertedMove+=str(bd.chessBoard[x2][y2])
            convertedMove+=str(move[4])
            convertedMove+="P"
    elif(len(move)==4):
        y1=(8-int(move[1]))
        x1=moveColumn[move[0]]
        y2=(8-int(move[3]))
        x2=moveColumn[move[2]]
        convertedMove+=str(y1)
        convertedMove+=str(x1)
        convertedMove+=str(y2)
        convertedMove+=str(x2)
        convertedMove+=bd.chessBoard[y2][x2]
        
    return convertedMove

# Making a move and undo the given move

# edit for checking king,rooks ever moved
def moveValid(move):
    convertedMove=convertMove(move)
    possibleMoves=bd.possibleMoves()
    for i in range(0, len(possibleMoves), 5):
        if(possibleMoves[i:i+5]==convertedMove):
            return True
    return False

def makeTheBestMove():
    move=bestMove()
    makeMove(move)

def makeMove(move):
    # print(move)
    if (move[4]=="C"):
        
        r=bd.capitalKingPosition//8
        c=bd.capitalKingPosition%8
        if(move[0]=="R"):
            bd.chessBoard[r][c]=" "
            bd.chessBoard[r][c+2]="K"
            bd.chessBoard[r][c+3]=" "
            bd.chessBoard[r][c+1]="R"

            bd.capitalKingPosition=(r*8)+c+2

            bd.castlingState[0][2]+=1
            bd.castlingState[0][1]+=1

            bd.capitalRightRook-=2
        else:
            print(move)
            bd.chessBoard[r][c]=" "
            bd.chessBoard[r][c-2]="K"
            bd.chessBoard[r][c-4]=" "
            bd.chessBoard[r][c-1]="R"
            bd.capitalKingPosition=(r*8)+c-2
            bd.castlingState[0][0]+=1
            bd.castlingState[0][1]+=1
            bd.capitalLeftRook+=3
    elif(move[4] != "P"):  # y1 x1 y2 x2 {oldPiece}
        y1 = int(move[0])
        x1 = int(move[1])
        y2 = int(move[2])
        x2 = int(move[3])
        if(bd.chessBoard[y1][x1]=="R"):
            if(((y1*8)+x1)==bd.capitalLeftRook):
                bd.castlingState[0][0]+=1
                bd.capitalLeftRook=y2*8+x2
            else:
                bd.castlingState[0][2]+=1
                bd.capitalRightRook=y2*8+x2
        elif(bd.chessBoard[y1][x1]=="K"):
            bd.castlingState[0][1]+=1
            bd.capitalKingPosition=y2*8+x2
        bd.chessBoard[y2][x2] = bd.chessBoard[y1][x1]
        bd.chessBoard[y1][x1] = " "
        
    else:                               # x1 x2 {oldPiece} {newPiece} {P}
        x1 = int(move[0])
        x2 = int(move[1])
        newPiece = move[3]
        bd.chessBoard[0][x2] = newPiece
        bd.chessBoard[1][x1] = " "
        
def undoMove(move):
    if (move[4]=="C"):
        r=bd.capitalKingPosition//8
        c=bd.capitalKingPosition%8
        if(move[0]=="R"):
            bd.chessBoard[r][c]=" "
            bd.chessBoard[r][c-2]="K"
            bd.chessBoard[r][c-1]=" "
            bd.chessBoard[r][c+1]="R"
            bd.capitalKingPosition=(r*8)+c-2
            bd.capitalRightRook+=2
            bd.castlingState[0][2]-=1
            bd.castlingState[0][1]-=1
        else:
            bd.chessBoard[r][c]=" "
            bd.chessBoard[r][c+2]="K"
            bd.chessBoard[r][c+1]=" "
            bd.chessBoard[r][c-2]="R"
            bd.capitalKingPosition=(r*8)+c+2
            bd.capitalLeftRook-=3
            bd.castlingState[0][0]-=1
            bd.castlingState[0][1]-=1
    elif(move[4] != "P"):
        y1 = int(move[0])
        x1 = int(move[1])
        y2 = int(move[2])
        x2 = int(move[3])
        if(bd.chessBoard[y1][x1]=="R"):
            if(((y1*8)+x1)==bd.capitalLeftRook):
                bd.castlingState[0][0]-=1
                bd.capitalLeftRook=y1*8+x1
            else:
                bd.castlingState[0][2]-=1
                bd.capitalRightRook=y1*8+x1
        elif(bd.chessBoard[y2][x2]=="K"):
            bd.castlingState[0][1]-=1
            bd.capitalKingPosition=y1*8+x1
        bd.chessBoard[y1][x1] = bd.chessBoard[y2][x2]
        bd.chessBoard[y2][x2] = move[4]
        
    else:                               # x1 x2 {oldPiece} {newPiece} {P}
        x1 = int(move[0])
        x2 = int(move[1])
        bd.chessBoard[0][x2] = move[2]
        bd.chessBoard[1][x1] = "P"


def bestMove():
    global bestOption
    bestOption=""
    x = (max(-100000000, 100000000, globalDepth))
    return bestOption
    # else:
    #     bd.flipTheBoard()
    #     x = min(-100000000, 100000000, globalDepth)
    #     bd.flipTheBoard()
    #     return bestOption


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

    for i in range(0, len(moves), 5):
        nextMove = moves[i:i+5]
        makeMove(nextMove)
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

"""
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
"""