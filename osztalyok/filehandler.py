from osztalyok import startingbudget, player, transaction
from os import listdir, remove; from os.path import isfile, exists

class FileHandler:
    def __init__(self) -> None:
        pass


    def readStartingBudget(self, file_path) -> list():
        # lista letrehozasa a kezdoosszegeknek
        startingBudgets = list()
        with open(file_path, 'r', encoding='utf-8') as f:
            for sor in f:
                sor = str(sor).strip().split('||')
                startingBudgets.append(startingbudget.StartingBudget(str(sor[0]), int(sor[1])))

        return startingBudgets


    def readSavegame(self, name) -> list:
        with open(f'./saves/{name}.levdb', 'r', encoding='utf-8') as f:
            
            # Pelda visszakuldott adatra
            # [numberOfPlayers, *players, *transactions]
            # listToReturn indexe: [0] -> jatekosok szama (int), [1] -> list(jatekosok), [2] -> list(tranzakciok)
            # mashol van letrehozva a savegame az adatokkal
            listToReturn = list()
            f = f.read().strip().split('|-|')

            
            tmpList = list()
            tmpList.append(f[0].strip())
            tmpList2 = f[1].strip().split()
            for i in range(len(tmpList2)): tmpList2[i] = tmpList2[i].split("||")
            tmpList.append(tmpList2)
            tmpList2 = f[2].strip().split()
            for i in range(len(tmpList2)): tmpList2[i] = tmpList2[i].split("||")
            tmpList.append(tmpList2)
            
            listToReturn.append(int(tmpList[0]))
            for cPlayer in tmpList[1]:
                print(cPlayer)
                listToReturn.append(player.Player(cPlayer[0], cPlayer[1]))
            
            for cTransaction in tmpList[2]:
                listToReturn.append(transaction.Transaction(cTransaction[0], cTransaction[1], cTransaction[2], cTransaction[3]))


            return listToReturn


    def writeSaveString(self, name, saveString) -> None:
        with open(f'./saves/{name}', 'w', encoding='utf-8') as f:
            f.write(saveString)
            return None


    def save(self, saveData) -> None:
        saveName = saveData[0]
        saveStr = saveData[1]
        with open(f"./saves/{saveName}.levdb", "w", encoding="utf-8") as f:
            f.write(saveStr)
            return None


    def readSaves(self) -> list:
        lstToRtn = []
        for element in listdir("./saves"):
            if isfile(f"./saves/{element}"):
                if element.endswith(".levdb"): lstToRtn.append(element.removesuffix(".levdb"))

        return lstToRtn
        

    def delIfExists(self, saveName) -> None:
        if exists(f"./saves/{saveName}.levdb"):
            remove(f"./saves/{saveName}.levdb")
        return None