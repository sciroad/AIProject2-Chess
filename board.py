capitalKingPosition = 60
lowerKingPosition = 4
kingMoved = False
leftRookMoved = False
rightRookMoved = False
chessBoard = [["r", "n", "b", "q", "k", "b", "n", "r"],
              ["p", "p", "p", "p", "p", "p", "p", "p"],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              ["P", "P", "P", "P", "P", "P", "P", "P"],
              ["R", "N", "B", "Q", "K", "B", "N", "R"]]

pawnWhite = [[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
             [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
             [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
             [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
             [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
             [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
             [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
             [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]
knightWhite = [[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
               [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
               [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
               [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
               [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
               [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
               [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
               [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
bishopWhite = [[-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
               [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
               [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
               [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
               [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
               [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
               [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
               [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
rookWhite = [[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
             [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
             [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
             [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
             [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
             [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
             [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
             [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]]
QueenWhite = [[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
              [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
              [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
              [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
              [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
              [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
              [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
              [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]
kingWhite = [[-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
             [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
             [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
             [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
             [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
             [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
             [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
             [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]]

pieceValues = {
    "P": 10,
    "N": 30,
    "B": 30,
    "R": 50,
    "Q": 90,
    "K": 900
}

capitalCan = ["r", "n", "b", "q", "k", "p", " "]
lowerCan = ["R", "N", "B", "Q", "K", "P", " "]


def possibleMoves():
    moves = ""
    for i in range(0, 64):
        r = i//8
        c = i % 8
        piece = chessBoard[r][c]
        if(piece == "K"):
            moves += possibleK(i)
        elif(piece == "B"):
            moves += possibleB(i)
        elif(piece == "N"):
            moves += possibleN(i)
        elif(piece == "Q"):
            moves += possibleQ(i)
        elif(piece == "R"):
            moves += possibleR(i)
        elif(piece == "P"):
            moves += possibleP(i)

    return moves

# move+=str(r)+str(c)+str((r+i))+str((c+j))+oldPiece
# y1 x1 y2 x2 {oldPiece} ödüllü ise


def possibleK(position):  # working perfect
    move = ""
    r = position//8
    c = position % 8
    oldPiece = ""
    global capitalKingPosition
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(i == 0 and j == 0):
                continue
            try:
                if(chessBoard[r+i][c+j] in capitalCan):
                    if((r+i) < 0 or (c+j) < 0):
                        break
                    oldPiece = chessBoard[r+i][c+j]  # Yenilen Parça
                    # King eski konumu boş artık arrayde
                    chessBoard[r][c] = " "
                    chessBoard[r+i][c+j] = "K"  # King yeni konumu arrayde
                    capitalKingPosition = position + \
                        (i*8) + j  # King yeni konumu 0-63
                    if(kingSafe()):
                        move += str(r)+str(c)+str((r+i))+str((c+j))+oldPiece

                        # print(str(r)+str(c)+str((r+i))+str((c+j))+oldPiece)
                    # King eski konumu boş artık arrayde
                    chessBoard[r][c] = "K"
                    chessBoard[r+i][c+j] = oldPiece  # King yeni konumu arrayde
                    capitalKingPosition = position
                pass
            except:
                pass
            # print(chessBoard[r+i][c+j] in capitalCan)

    return move


def possibleB(position):  # working perfect
    move = ""
    r = position//8
    c = position % 8
    oldPiece = ""
    counter = 1
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):

            try:
                while(chessBoard[r+counter*i][c+counter*j] in capitalCan):
                    if((c+counter*j) < 0 or(r+counter*i) < 0):
                        break
                    oldPiece = chessBoard[r+counter*i][c+counter*j]
                    chessBoard[r][c] = " "
                    chessBoard[r+counter*i][c+counter*j] = "B"
                    if(kingSafe()):
                        move += str(r)+str(c)+str((r+counter*i)) + \
                            str((c+counter*j))+oldPiece
                    chessBoard[r+counter*i][c+counter*j] = oldPiece
                    chessBoard[r][c] = "B"
                    if(oldPiece != " "):
                        break
                    counter += 1
            except:
                pass
            counter = 1

    return move


def possibleN(position):  # working perfect
    move = ""
    r = position//8
    c = position % 8
    oldPiece = ""
    for i in range(-1, 2, 2):
        for j in range(-2, 3, 4):
            try:

                if(chessBoard[r+i][c+j] in capitalCan):
                    if((r+i) < 0 or(c+j) < 0):
                        break
                    oldPiece = chessBoard[r+i][c+j]
                    chessBoard[r+i][c+j] = "N"
                    chessBoard[r][c] = " "
                    if(kingSafe()):
                        move += str(r)+str(c)+str((r+i))+str((c+j))+oldPiece
                    chessBoard[r+i][c+j] = oldPiece
                    chessBoard[r][c] = "N"

            except:
                pass
            try:
                if(chessBoard[r+j][c+i] in capitalCan):
                    if((r+j) < 0 or(c+i) < 0):
                        break
                    oldPiece = chessBoard[r+j][c+i]
                    chessBoard[r+j][c+i] = "N"
                    chessBoard[r][c] = " "
                    if(kingSafe()):
                        move += str(r)+str(c)+str((r+j))+str((c+i))+oldPiece
                    chessBoard[r+j][c+i] = oldPiece
                    chessBoard[r][c] = "N"

            except:
                pass
    return move


def possibleQ(position):  # working perfect
    move = ""
    r = position//8
    c = position % 8
    oldPiece = ""
    counter = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(i == 0 and j == 0):
                continue
            try:
                while(chessBoard[r+counter*i][c+counter*j] in capitalCan):
                    if((c+counter*j) < 0 or(r+counter*i) < 0):
                        break
                    # print("i=",i," j=",j, " counter=",counter)
                    oldPiece = chessBoard[r+counter*i][c+counter*j]
                    chessBoard[r][c] = " "
                    chessBoard[r+counter*i][c+counter*j] = "Q"
                    if(kingSafe()):
                        move += str(r)+str(c)+str((r+counter*i)) + \
                            str((c+counter*j))+oldPiece
                    chessBoard[r][c] = "Q"
                    chessBoard[r+counter*i][c+counter*j] = oldPiece
                    counter += 1
                    if(oldPiece != " "):
                        break

            except:
                pass
            counter = 1
    return move


def possibleR(position):  # working perfect
    move = ""
    r = position//8
    c = position % 8
    oldPiece = ""
    counter = 1
    for i in range(-1, 2, 2):
        try:
            while(chessBoard[r+counter*i][c] in capitalCan):
                if((r+counter*i) < 0):
                    break
                oldPiece = chessBoard[r+counter*i][c]
                chessBoard[r][c] = " "
                chessBoard[r+counter*i][c] = "R"
                if(kingSafe()):
                    move += str(r)+str(c)+str((r+counter*i))+str((c))+oldPiece
                chessBoard[r+counter*i][c] = oldPiece
                chessBoard[r][c] = "R"
                if(oldPiece != " "):
                    break
                counter += 1
        except:
            pass
        counter = 1
        try:
            while(chessBoard[r][c+counter*i] in capitalCan):
                if((c+counter*i) < 0):
                    break
                oldPiece = chessBoard[r][c+counter*i]
                chessBoard[r][c] = " "
                chessBoard[r][c+counter*i] = "R"
                if(kingSafe()):
                    move += str(r)+str(c)+str((r))+str((c+counter*i))+oldPiece
                chessBoard[r][c+counter*i] = oldPiece
                chessBoard[r][c] = "R"
                if(oldPiece != " "):
                    break
                counter += 1
        except:
            pass
        counter = 1
    return move
# x1 x2 {oldPiece} {newPiece} {P}


def possibleP(position):
    move = ""
    r = position//8
    c = position % 8
    oldPiece = ""
    if(r > 1):
        try:
            if(chessBoard[r-1][c] == " "):  # bir ileri ödülsüz
                chessBoard[r][c] = " "
                chessBoard[r-1][c] = "P"
                if(kingSafe()):
                    move += str(r)+str(c)+str((r-1))+str((c))+" "
                chessBoard[r-1][c] = " "
                chessBoard[r][c] = "P"
        except:
            pass
        try:
            # sağ çapraz ödülsüz
            if(chessBoard[r-1][c+1] in capitalCan and chessBoard[r-1][c+1] != " "):
                oldPiece = chessBoard[r-1][c+1]
                chessBoard[r][c] = " "
                chessBoard[r-1][c+1] = "P"
                if(kingSafe()):
                    move += str(r)+str(c)+str((r-1))+str((c+1))+oldPiece
                chessBoard[r-1][c+1] = oldPiece
                chessBoard[r][c] = "P"
        except:
            pass
        if(c > 0):
            try:
                # sol çapraz ödülsüz
                if(chessBoard[r-1][c-1] in capitalCan and chessBoard[r-1][c-1] != " "):
                    oldPiece = chessBoard[r-1][c-1]
                    chessBoard[r][c] = " "
                    chessBoard[r-1][c-1] = "P"
                    if(kingSafe()):
                        move += str(r)+str(c)+str((r-1))+str((c-1))+oldPiece
                    chessBoard[r-1][c-1] = oldPiece
                    chessBoard[r][c] = "P"
            except:
                pass
    if(r == 1):
        try:
            if(chessBoard[r-1][c] == " "):  # bir ileri ödüllü
                for i in ["R", "Q", "N", "B"]:
                    chessBoard[r][c] = " "
                    chessBoard[r-1][c] = i
                    if(kingSafe()):
                        move += str(c)+str(c)+" "+i+"P"
                    chessBoard[r-1][c] = " "
                    chessBoard[r][c] = "P"
        except:
            pass
        try:
            # sağ çapraz ödüllü
            if(chessBoard[r-1][c+1] in capitalCan and chessBoard[r-1][c+1] != " "):
                for i in ["R", "Q", "N", "B"]:
                    oldPiece = chessBoard[r-1][c+1]
                    chessBoard[r][c] = " "
                    chessBoard[r-1][c+1] = i
                    if(kingSafe()):
                        move += str(c)+str(c+1)+oldPiece+i+"P"
                    chessBoard[r-1][c+1] = oldPiece
                    chessBoard[r][c] = "P"
        except:
            pass
        if(c > 0):
            try:
                # sol çapraz ödüllü
                if(chessBoard[r-1][c-1] in capitalCan and chessBoard[r-1][c-1] != " "):
                    for i in ["R", "Q", "N", "B"]:
                        oldPiece = chessBoard[r-1][c-1]
                        chessBoard[r][c] = " "
                        chessBoard[r-1][c-1] = i
                        if(kingSafe()):
                            move += str(c)+str(c-1)+oldPiece+i+"P"
                        chessBoard[r-1][c-1] = oldPiece
                        chessBoard[r][c] = "P"
            except:
                pass

    if(r > 5):  # iki ileri başlangıç
        try:
            if(chessBoard[r-2][c] == " "):
                chessBoard[r][c] = " "
                chessBoard[r-2][c] = "P"
                if(kingSafe()):
                    move += str(r)+str(c)+str((r-2))+str((c))+" "
                chessBoard[r-2][c] = " "
                chessBoard[r][c] = "P"
        except:
            pass
    # if(r==1): #sağ çapraz ödüllü
    return move

def checkLeftRook(position):



    return False

def checkRightRook(position):
    


def kingSafe():
    global capitalKingPosition
    r = capitalKingPosition//8
    c = capitalKingPosition % 8
    counter = 1
    #Bishop and Queen
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            try:
                while(chessBoard[r+counter*i][c+counter*j] == " "):
                    if((c+counter*j) < 0 or(r+counter*i) < 0):
                        break
                    counter += 1
                ch = chessBoard[r+counter*i][c+counter*j]
                if(ch == "b" or ch == "q"):
                    return False
            except:
                pass
            counter = 1

    #Rook and Queen
    for i in range(-1, 2, 2):
        try:
            while(chessBoard[r+counter*i][c] == " "):
                if((r+counter*i) < 0):
                    break
                counter += 1
                # print("i=",i," counter=",counter)
            ch = chessBoard[r+counter*i][c]
            # print("ch=",ch)
            if(ch == "r" or ch == "q"):
                return False
        except:
            pass
        counter = 1
        try:
            while(chessBoard[r][c+counter*i] == " "):
                if((c+counter*i) < 0):
                    break
                counter += 1
            ch = chessBoard[r][c+counter*i]
            if(ch == "r" or ch == "q"):
                return False
        except:
            pass
        counter = 1

    # {N}Knigt
    for i in range(-1, 2, 2):
        for j in range(-2, 3, 4):
            try:
                if(chessBoard[r+i][c+j] == "n"):
                    if((r+i) < 0 or(c+j) < 0):
                        break
                    return False
            except:
                pass
            try:
                if(chessBoard[r+j][c+i] == "n"):
                    if((r+i) < 0 or(c+j) < 0):
                        break
                    return False
            except:
                pass

    # Pawn
    try:
        if(chessBoard[r-1][c+1] == "p"):  # king sağ çapraz
            if(r > 0):
                return False
    except:
        pass
    try:
        if(chessBoard[r-1][c-1] == "p"):  # king sol çapraz
            if(r > 0 and c > 0):
                return False
    except:
        pass

    return True


def boardPrinter(chessBoard):
    for i in range(0, 8):
        print(chessBoard[i])

# flip board and evaluate

# Calculate the score for each piece


def flipTheBoard():
    global chessBoard
    for i in range(0, 64):
        r = i//8
        c = i % 8
        if chessBoard[r][c].islower():
            chessBoard[r][c] = chessBoard[r][c].upper()
        else:
            chessBoard[r][c] = chessBoard[r][c].lower()
    # for i in range(0, 32):
    #     r = i//8
    #     c = i % 8
    #     temp = chessBoard[7-r][7-c]
    #     chessBoard[7-r][7-c] = chessBoard[r][c]
    #     chessBoard[r][c] = temp
    chessBoard = chessBoard[::-1]


def calculateScore():
    score = 0
    for i in range(0, 64):
        r = i//8
        c = i % 8
        piece = chessBoard[r][c]
        if(piece == "K"):
            score += kingEval(i)
        elif(piece == "B"):
            score += bishopEval(i)
        elif(piece == "N"):
            score += knightEval(i)
        elif(piece == "Q"):
            score += queenEval(i)
        elif(piece == "R"):
            score += rookEval(i)
        elif(piece == "P"):
            score += pawnEval(i)
    flipTheBoard()
    for i in range(0, 64):
        r = i//8
        c = i % 8
        piece = chessBoard[r][c]
        if(piece == "K"):
            score -= kingEval(i)
        elif(piece == "B"):
            score -= bishopEval(i)
        elif(piece == "N"):
            score -= knightEval(i)
        elif(piece == "Q"):
            score -= queenEval(i)
        elif(piece == "R"):
            score -= rookEval(i)
        elif(piece == "P"):
            score -= pawnEval(i)
    flipTheBoard()
    return score


def kingEval(i):
    r = i//8
    c = i % 8
    score = pieceValues["K"]+kingWhite[r][c]
    return score


def bishopEval(i):
    r = i//8
    c = i % 8
    score = pieceValues["B"]+kingWhite[r][c]
    return score


def knightEval(i):
    r = i//8
    c = i % 8
    score = pieceValues["N"]+kingWhite[r][c]
    return score


def queenEval(i):
    r = i//8
    c = i % 8
    score = pieceValues["Q"]+kingWhite[r][c]
    return score


def rookEval(i):
    r = i//8
    c = i % 8
    score = pieceValues["R"]+kingWhite[r][c]
    return score


def pawnEval(i):
    r = i//8
    c = i % 8
    score = pieceValues["P"]+kingWhite[r][c]
    return score
