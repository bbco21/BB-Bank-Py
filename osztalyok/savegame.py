from osztalyok import transaction, player, filehandler
import global_constants as gc

class Savegame:
    def __init__(self, saveList, saveName) -> None:
        self.saveName = saveName
        self.saveList = list(saveList)
        self.numberOfPlayers = int(self.saveList[0])
        self.players = list()
        self.transactions = list()

        for i in range(len(self.saveList)):
            if i > 0 and i < (self.numberOfPlayers + 1):
                self.players.append(self.saveList[i])
            elif i > 0:
                self.transactions.append(self.saveList[i])
        del self.saveList


    def teszt(self):
        # Ez egy teszt fuggveny aminek mar nem vagom, h mi a lenyege, de nem merem kitorolni
        print(self.numberOfPlayers)
        for player in self.players: print(player.name)
        for transaction in self.transactions: print(transaction.transaction_from, "->", transaction.transaction_money, transaction.transaction_to)


    def getFinalSaveString(self) -> str:
        # fss = final save string
        fss = ""
        fss += str(self.numberOfPlayers); fss += "\n|-|\n"
        for player in self.players:
            fss += player.name; fss += "||"
            fss += str(player.money); fss += "\n"
        fss += "|-|\n"
        for transaction in self.transactions:
            fss += transaction.getSaveString(); fss += "\n"
        return fss.strip()


    def getSaveData(self) -> tuple:
        saveData = (self.saveName, self.getFinalSaveString())
        return saveData


    def makeTransaction(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        print("Utalo jatekos:")
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        playerFromIndex = int(input("Valasz: ")) - 1

        gc.cls()
        print(gc.MESSAGE)
        print("Fogado jatekos:")
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        playerToIndex = int(input("Valasz: ")) - 1

        gc.cls()
        print(gc.MESSAGE)
        transactionMoney = int(input("Utalando osszeg: "))
        
        if self.players[playerFromIndex].money-transactionMoney >= gc.MIN_MONEY:
            self.players[playerFromIndex].money -= transactionMoney
            self.players[playerToIndex].money += transactionMoney
            self.addTransaction(transaction.Transaction("u", self.players[playerFromIndex].name, self.players[playerToIndex].name, transactionMoney))
            return None
        else:
            gc.cls()
            print(gc.MESSAGE)
            input("NEM ALL RENDELKEZESRE ELEGENDO EGYENLEG AZ UTALO FEL SZAMLAJAN!\nNyomj ENTER-t a folytatashoz...")
            return None


    def givePlayerMoney(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        print("Penz hozzaadasa:")
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        playerToIndex = int(input("Valasz: ")) - 1

        gc.cls()
        print(gc.MESSAGE)
        moneyToGive = int(input("Hozzaaadando penz osszege: "))

        self.players[playerToIndex].money += moneyToGive

        self.addTransaction(transaction.Transaction("h", "bank", self.players[playerToIndex].name, moneyToGive))
        return None


    def removePlayerMoney(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        print("Penz elvetele:")
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        playerFromIndex = int(input("Valasz: ")) - 1

        gc.cls()
        print(gc.MESSAGE)
        moneyToRemove = int(input("Levonando osszeg: "))

        if self.players[playerFromIndex].money-moneyToRemove >= gc.MIN_MONEY:
            self.players[playerFromIndex].money -= moneyToRemove
            self.addTransaction(transaction.Transaction("e", self.players[playerFromIndex].name, "bank", moneyToRemove))
            return None
        else:
            input("NEM ALL RENDELKEZESRE ELEGENDO OSSZEG!\nNyomj ENTER-t a folytatashoz...")
            return None


    def playerStartMoney(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        userCh = int(input("Valasz: ")) - 1

        self.players[userCh].money += gc.START_MONEY
        self.addTransaction(transaction.Transaction("S", "bank", self.players[userCh].name, gc.START_MONEY))

        return None


    def addTransaction(self, transaction) -> None:
        self.transactions.append(transaction)
        return None


    def createTransaction(self, tr_type, tr_from, tr_to, tr_money) -> None:
        self.addTransaction(transaction.Transaction(tr_type, tr_from, tr_to, tr_money))
        return None


    def getPlayersInfo(self) -> str:
        strToRtn = ""
        for player in self.players:
            strToRtn += str(player.name) + " " + str(player.money) + "\n"
        return gc.spacesback(strToRtn)


    def getTransactionsList(self) -> list:
        transactionsList = []
        for transaction in self.transactions:
            transactionsList.append((transaction.transaction_type, transaction.transaction_from, transaction.transaction_to, transaction.transaction_money))
        return transactionsList


    def printTransactions(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        for transaction in self.getTransactionsList():
            if transaction[0] == "u":
                print(f"{gc.spacesback(transaction[1])} -> {gc.spacesback(transaction[2])} {int(transaction[3]):_}")
            elif transaction[0] == "h" or transaction[0] == "S" or transaction[0] == "K":
                print(f"{gc.spacesback(transaction[2])} <- + {int(transaction[3]):_}")
            elif transaction[0] == "e":
                print(f"{gc.spacesback(transaction[1])} -> - {int(transaction[3]):_}")
            else:
                print(f"ISMERETLEN TRANZAKCIO ({transaction})")
        return None


    def playerTransactionsInit(self):
        for transaction in self.transactions:
            for player in self.players:
                if transaction.transaction_from == player.name or transaction.transaction_to == player.name:
                    player.addTransaction(transaction)


    def getTmpSaveData(self) -> tuple:
        originalSaveData = self.getSaveData()
        alteredSaveData = (str(self.saveName + "_"), originalSaveData[1])
        return alteredSaveData


def createNewSavegame(startingBudget) -> Savegame:
    gc.cls()
    print(gc.BANNER)

    saveName = gc.removespace(input("Mentes neve: "))
    numberOfPlayers = int(input("Jatekosok szama: "))
    saveList = [numberOfPlayers]

    for i in range(numberOfPlayers):
        saveList.append(player.Player(gc.removespace(input(f"{i+1}. jatekos neve: ")), startingBudget))

    for i in range(numberOfPlayers):
        saveList.append(transaction.Transaction("K", "bank", saveList[i+1].name, startingBudget))

    return Savegame(saveList, saveName)
    