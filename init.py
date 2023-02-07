import os
import global_constants as gc
from osztalyok import filehandler, savegame
import main

def main():
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
    else:
        sg = savegame.Savegame(fh.readSavegame(saveFiles[userCh]), saveFiles[userCh])


    sg.playerTransactionsInit()

    main.mainLoop(fh, sg)

    gc.cls()
    print("EXITING APPLICATION...")

main()
