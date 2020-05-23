import board as bd
import evaluater as ev
import time


# move="12345"
# print(move[0:4])
# print("\n")
print(bd.possibleMoves()) 
# bd.boardPrinter(bd.chessBoard)
# print("\n")
# ev.flipTheBoard()
# bd.boardPrinter(bd.chessBoard)
# moves = bd.possibleMoves()
    
# for i in range(0,len(moves),5):
#     move=moves[i:i+5]
    # print(move,"|","i=",i,sep="")
# bestMove=ev.bestMove("max")
# print(bd.possibleMoves()) 
# print(bestMove)
bd.boardPrinter(bd.chessBoard)
count=5
while(count!=0):
    bd.boardPrinter(bd.chessBoard)
    myMove=input("hamle:")
    ev.makeMove(myMove)
    bd.boardPrinter(bd.chessBoard)
    bd.flipTheBoard()
    print(bd.possibleMoves()) 
    print("\n")
    bestMove=ev.bestMove("max")
    ev.makeMove(bestMove)
    bd.boardPrinter(bd.chessBoard)
    print("\n")
    bd.flipTheBoard()
    bd.boardPrinter(bd.chessBoard)
    print("\n")


    
    
    
    # print(bestMove)
    
    
    
    
    
    # bd.boardPrinter(bd.chessBoard)
    
    # print(bd.possibleMoves()) 
    # bestMove=ev.bestMove("min")
    # print(bestMove)
    # time.sleep(5)
    # bd.flipTheBoard()
    # ev.makeMove(bestMove)
    # bd.flipTheBoard()
    # bd.boardPrinter(bd.chessBoard)
    # time.sleep(5)
    # count-=1
# if(bestMove!=""):
#     ev.makeMove(bestMove)
# bd.boardPrinter(bd.chessBoard)


# print("\n")
# ev.makeMove("56nRP")
# bd.boardPrinter(bd.chessBoard)
# print("\n")
# print(bd.possibleMoves()) 
# bd.boardPrinter(bd.chessBoard)
# print("\n")
# ev.undoMove("56nRP")
# bd.boardPrinter(bd.chessBoard)

