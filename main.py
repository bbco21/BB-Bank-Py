import global_constants as gc
import sys

if __name__ == "__main__":
    gc.cls()
    print("Kerlek az init.py-t futtasd!")
    sys.exit()

def mainLoop(fileHandler, savegame) -> None:
    while True:
        # FOMENU letrehozasa
        # Muveletek a fomenuben

        fileHandler.save(savegame.getTmpSaveData())
        gc.cls()
        print(gc.MESSAGE)

        playersInfo = savegame.getPlayersInfo()
        print(savegame.getPlayersInfo())

        print("1 - Utalas ket jatekos kozott")
        print("2 - Penz hozzaadasa jatekoshoz")
        print("3 - Penz elvetele jatekostol")
        print("4 - START mezo")
        print("5 - Tranzakciok megtekintese")
        print("0 - Kilepes")
        userCh = int(input("Valasz: "))

        if userCh == 0:
            gc.cls()
            print(gc.MESSAGE)
            print("1 - Mentes es kilepes")
            print("2 - Kilepes mentes nelkul")
            userCh = int(input("Valasz: "))

            if userCh == 1:
                fileHandler.save(savegame.getSaveData())
                fileHandler.delIfExists(savegame.getTmpSaveData()[0])
                return None
            elif userCh == 2:
                fileHandler.delIfExists(savegame.getTmpSaveData()[0])
                return None
            else:
                input("NINCS ILYEN OPCIO!\nNyomd meg az ENTER-t a folytatashoz...")
        elif userCh == 1:
            savegame.makeTransaction()
        elif userCh == 2:
            savegame.givePlayerMoney()
        elif userCh == 3:
            savegame.removePlayerMoney()
        elif userCh == 4:
            savegame.playerStartMoney()
        elif userCh == 5:
            gc.cls()
            print(gc.MESSAGE)
            print("0 - Osszes tranzakcio megjelenitese")
            for i in range(len(savegame.players)):
                print(f"{i+1} - {gc.spacesback(savegame.players[i].name)}")
            userCh = int(input("Valasz: ")) - 1

            if userCh == -1:
                savegame.printTransactions()
                gc.wait()
            elif userCh > -1 and userCh <= len(savegame.players):
                savegame.players[userCh].printTransactions()
                # gc.cls()
                # print(gc.MESSAGE)
                # print(savegame.players[userCh].getPrintableStr())
                gc.wait()
            else:
                input("NINCS ILYEN SORSZAMU JATEKOS!\nNyomj ENTER-t a folytatashoz...")
        elif userCh == 9:
            for i in range(50000):
                savegame.createTransaction('h', 'a', 'b', 1)
        else:
            input("NINCS ILYEN OPCIO!\nNyomj ENTER-t a folytatashoz...")
            
