import os, sys
import global_constants as gc
from osztalyok import filehandler, savegame
import main

gc.ARGV = sys.argv

if '-h' in gc.ARGV or '--help' in gc.ARGV:
    print(gc.MESSAGE)
    print("ROVID HOSSZU    LEIRAS")
    print(" -u   --unsafe  Minden biztonsagi ellenorzest kikapcsol")
    print(" -h   --help    Kiirja ezt az uzenetet")
    sys.exit()


def mainfgv():
    fh = filehandler.FileHandler()
    saveFiles = fh.readSaves()

    ########################
    gc.cls()
    print(gc.MESSAGE)

    print("Valassz mentest:")
    print("0 - Uj mentes letrehozasa")
    for i in range(len(saveFiles)):
        print(gc.spacesback(f"{i+1} - {saveFiles[i]}"))

    userCh = int(input("Valasz: ")) - 1

    if userCh == -1:
        startingBudgets = fh.readStartingBudget("./kezdotokek.levdb")
        gc.cls()
        print(gc.MESSAGE)
        for i in range(len(startingBudgets)):
            print(f"{i+1} - {startingBudgets[i].name}: {startingBudgets[i].money}")
        userCh = int(input("Valasz: ")) - 1
        sg = savegame.createNewSavegame(startingBudgets[userCh].money)
        fh.writehash(sg.saveName, sg.getFinalSaveString())
    else:
        sg = savegame.Savegame(fh.readSavegame(saveFiles[userCh]), saveFiles[userCh])





    sg.playerTransactionsInit()

    if '-u' in gc.ARGV or '--unsafe' in gc.ARGV:
        gc.MESSAGE += "UNSAFE MODE\n"
        gc.cls()
        print("FIGYELEM\nNem biztonsagos modban fut a program.")
        print("A tranzakciok nem lesznek ellenorizve.")
        gc.wait()
    else:
        sg.validateBalance(sg.players, sg.transactions)
        savehash = fh.readhash(sg.saveName)
        if savehash == None:
            gc.cls()
            print("A mentesnek nincs hash-e!\nLehetseges, hogy a mentest modositottak.")
            gc.wait()
        else:
            sg.validateFile(savehash)

    


    main.mainLoop(fh, sg)

    gc.cls()
    print("EXITING APPLICATION...")

mainfgv()
