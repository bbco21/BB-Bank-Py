import os, sys
import global_constants as gc
from osztalyok import filehandler, savegame, settingsmanager
import main

gc.ARGV = sys.argv
sm = settingsmanager.settingsManager()

if '-h' in gc.ARGV or '--help' in gc.ARGV:
    print(gc.MESSAGE)
    print(sm.SAVELOC_TXT + gc.SAVELOCATION + "\n")
    #print("ROVID HOSSZU      LEIRAS")
    #print(" -u   --unsafe    Minden biztonsagi ellenorzest kikapcsol")
    #print(" -h   --help      Kiirja ezt az uzenetet")
    #print(" -s   --settings  Beallitasok megnyitasa es szerkesztese")
    print(sm.HELP_HEADER)
    print(sm.HELP_UNSAFE)
    print(sm.HELP_HELP)
    print(sm.HELP_SETTINGS)
    sys.exit()


def mainfgv():


    fh = filehandler.FileHandler()
    saveFiles = fh.readSaves()

    ########################
    gc.cls()
    print(gc.MESSAGE)

    #print("Valassz mentest:")
    #print("0 - Uj mentes letrehozasa")
    print("-1 - Settings\n")
    print(sm.SELECT_SAVE)
    print(sm.NEW_SAVE)
    for i in range(len(saveFiles)):
        print(gc.spacesbackSaveName(f"{i+1} - {saveFiles[i]}"))

    userCh = int(input(sm.OPTION)) - 1

    if userCh == -2:
        sm.menu()
        gc.cls()
        print(gc.MESSAGE)
        print(sm.SELECT_SAVE)
        print(sm.NEW_SAVE)
        for i in range(len(saveFiles)):
            print(gc.spacesbackSaveName(f"{i+1} - {saveFiles[i]}"))
        userCh = int(input(sm.OPTION)) - 1


    if userCh == -1:
        startingBudgets = fh.readStartingBudget(f"{gc.SAVELOCATION}/kezdotokek.levdb")
        gc.cls()
        print(gc.MESSAGE)
        for i in range(len(startingBudgets)):
            print(f"{i+1} - {startingBudgets[i].name}: {startingBudgets[i].money}")
        userCh = int(input(sm.OPTION)) - 1
        sg = savegame.createNewSavegame(startingBudgets[userCh].money, sm)
        fh.writehash(sg.saveName, sg.getFinalSaveString())
    else:
        sg = savegame.Savegame(fh.readSavegame(saveFiles[userCh]), saveFiles[userCh], sm)





    sg.playerTransactionsInit()

    if '-u' in gc.ARGV or '--unsafe' in gc.ARGV:
        gc.MESSAGE += "UNSAFE MODE\n"
        gc.cls()
        #print("FIGYELEM\nNem biztonsagos modban fut a program.")
        #print("A tranzakciok nem lesznek ellenorizve.")
        #gc.wait()
        gc.wait(sm.UNSAFE_WARN_MSG)
    else:
        sg.validateBalance(sg.players, sg.transactions)
        savehash = fh.readhash(sg.saveName)
        if savehash == None:
            gc.cls()
            #print("A mentesnek nincs hash-e!\nLehetseges, hogy a mentest modositottak.")
            #gc.wait()
            gc.wait(sm.MISSING_HASH_WARN)
        else:
            sg.validateFile(savehash)

    


    main.mainLoop(fh, sg, sm)

    gc.cls()
    print("EXITING APPLICATION...")

mainfgv()
