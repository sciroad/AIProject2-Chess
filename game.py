import board as bd
import evaluater as ev
def startGame():
    player = True  # white true-1 false-2
    gameInfo = "Tüm hamleleri büyük harfle yazınız\n"
    gameInfo+="Vezir kanadına rook(L---C)\n"
    gameInfo+="Şah kanadına rook(R---C)\n"
    gameInfo+="eğer oynadığınız taş piyon ise ve ödül alıyor ise ödülüde devamında giriniz(Örnek:'A7A8Q' şeklinde oynanırsa a sütununda ki piyon son satıra geçerek Queen(Vezir) ödülünü almıştır.)\n"
    gameInfo+="bunlar dışında her hamlenizi 'E1D1' şeklinde yazarak giriniz.\nHamle:"
    bd.boardPrinter(bd.chessBoard)
    while(not bd.checkMate() or not bd.draw()):

        if(player):
            hamle = input(gameInfo)
            while(not(ev.moveValid(hamle))):
                print("Hamle geçersiz veya böyle bir hamle yapamazsınız.")  
                hamle=input(gameInfo)
            ev.makeMove(ev.convertMove(hamle))
        else:
            bd.flipTheBoard()
            ev.makeTheBestMove()
            bd.flipTheBoard()
        player= not player
        bd.boardPrinter(bd.chessBoard)
    if(bd.checkMate()):
        if(player):
            print("Siyahlar Kazandı.")
        else:
            print("Beyazlar Kazandı.")
    else:
        print("Maç berabere bitti.")