from osztalyok import transaction, player, filehandler, settingsmanager
import global_constants as gc
import sys, hashlib

# a savegame osztaly kezeli az egesz jatekot
class Savegame:
    def __init__(self, saveList, saveName, sm: settingsmanager.settingsManager) -> None:
        self.saveName = saveName
        self.saveList = list(saveList)
        self.numberOfPlayers = int(self.saveList[0])
        self.players = list()
        self.transactions = list()
        self.sm = sm

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

    # Visszakuldi a vegleges mentesi stringet ami kiirhato a mentesfajlba
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

    # Visszater a mentes dataval ami tartalmazza a mentes nevet es a vegleges mentesi stringet
    def getSaveData(self) -> tuple:
        saveData = (self.saveName, self.getFinalSaveString())
        return saveData

    # Ket jatekos kozotti utalast valositja meg
    def makeTransaction(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        #print("Utalo jatekos:")
        print(self.sm.TRANSFERING_PLAYER)
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        #playerFromIndex = int(input("Valasz: ")) - 1
        playerFromIndex = int(input(self.sm.OPTION)) - 1

        gc.cls()
        print(gc.MESSAGE)
        #print("Fogado jatekos:")
        print(self.sm.RECEIVING_PLAYER)
        for i in range(len(self.players)):
            tmp = []
            for x in range(len(self.players)):
                if self.players[x] != self.players[playerFromIndex]:
                    tmp.append(self.players[x])
        for i in range(len(tmp)):
            print(f"{i+1} - {gc.spacesback(tmp[i].name)}")
        #playerTo = tmp[int(input("Valasz: ")) - 1]
        playerTo = tmp[int(input(self.sm.OPTION)) - 1]
        for i in range(len(self.players)):
            if self.players[i] == playerTo:
                playerToIndex = i
                break

        gc.cls()
        print(gc.MESSAGE)
        transactionMoney = self.moneyInput()
        
        if transactionMoney <= 0:
            #print("0 osszegu vagy kisebb tranzakcio nem valosithato meg!")
            #gc.wait()
            gc.wait(self.sm.ZERO_OR_LESS_TRANS_ERROR)
            return None
        if self.players[playerFromIndex].money-transactionMoney >= gc.MIN_MONEY:
            self.players[playerFromIndex].money -= transactionMoney
            self.players[playerToIndex].money += transactionMoney
            self.addTransaction(transaction.Transaction("u", self.players[playerFromIndex].name, self.players[playerToIndex].name, transactionMoney))
            return None
        else:
            gc.cls()
            print(gc.MESSAGE)
            #input("NEM ALL RENDELKEZESRE ELEGENDO EGYENLEG AZ UTALO FEL SZAMLAJAN!\nNyomj ENTER-t a folytatashoz...")
            gc.wait(self.sm.NOT_ENOUGH_FUNDS)
            return None

    # Barmikor amikor penzosszeget kell bekerni, azt ezen a fuggvenyen at lehet megtenni
    # Ellenorzi a roviditeseket, mint pl: k, m es ennek megfelelo integer ertekkel ter vissza
    def moneyInput(self) -> int:
        #inputStr = str(input("Osszeg: "))
        inputStr = str(input(self.sm.MONEY_IN))
        if inputStr.isdecimal():
            return int(inputStr)
        else:
            lastChar = inputStr[len(inputStr) - 1]
            if lastChar == "m":
                inputStr = inputStr[:-1]
                return int(float(inputStr) * 1_000_000)
            elif lastChar == "k":
                inputStr = inputStr[:-1]
                return int(float(inputStr) * 1_000)
            else:
                #input("Hibas a bemenet szintaxisa. Tranzakcio vegrehajtasa 0 osszeggel.\nProbald ujra a tranzakciot.")
                gc.wait(self.sm.MONEY_IN_SYNTAX_ERROR)
                return 0

    # Ha egy jatekos penzt kap ez a fgv letrehozza a tranzakciot es hozzaadja sajat magahoz illetve a kotodo jatekoshoz
    def givePlayerMoney(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        #print("Penz hozzaadasa:")
        print(self.sm.MONEY_GIVING)
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        #playerToIndex = int(input("Valasz: ")) - 1
        playerToIndex = int(input(self.sm.OPTION)) - 1

        gc.cls()
        print(gc.MESSAGE)
        moneyToGive = self.moneyInput()

        self.players[playerToIndex].money += moneyToGive
        if moneyToGive > 0:
            self.addTransaction(transaction.Transaction("h", "bank", self.players[playerToIndex].name, moneyToGive))
        else:
            gc.cls()
            #print("0 vagy negativ erteku tranzakcio nem valosithato meg!")
            #gc.wait()
            gc.wait(self.sm.ZERO_OR_LESS_TRANS_ERROR)
        return None

    # Ha egy jatekostol el kell venni penzt nem utalas celjabol ez a fgv leelenorzi, hogy megvalosithato-e a tranzakcio
    # es ha igen akkor letrehozza azt majd hozzaadja sajat magahoz es a kotodo jatekoshoz
    def removePlayerMoney(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        #print("Penz elvetele:")
        print(self.sm.MONEY_REMOVING)
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        #playerFromIndex = int(input("Valasz: ")) - 1
        playerFromIndex = int(input(self.sm.OPTION)) - 1

        gc.cls()
        print(gc.MESSAGE)
        moneyToRemove = self.moneyInput()

        if self.players[playerFromIndex].money-moneyToRemove >= gc.MIN_MONEY:
            if moneyToRemove > 0:
                self.players[playerFromIndex].money -= moneyToRemove
                self.addTransaction(transaction.Transaction("e", self.players[playerFromIndex].name, "bank", moneyToRemove))
            else:
                gc.cls()
                #print("0 vagy negativ erteku tranzakcio nem valosithato meg!")
                #gc.wait()
                gc.wait(self.sm.ZERO_OR_LESS_TRANS_ERROR)
            return None
        else:
            #input("NEM ALL RENDELKEZESRE ELEGENDO OSSZEG!\nNyomj ENTER-t a folytatashoz...")
            gc.wait(self.sm.NOT_ENOUGH_FUNDS)
            return None

    # Amennyiben egy jatekos athalad a startmezon a GC-ben meghatarozott osszeggel letrehoz egy tranzakciot, teljesiti azt
    # es hozzaadja sajat magahoz es a kotodo jatekoshoz
    def playerStartMoney(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        for i in range(len(self.players)):
            print(f"{i+1} - {gc.spacesback(self.players[i].name)}")
        #userCh = int(input("Valasz: ")) - 1
        userCh = int(input(self.sm.OPTION)) - 1

        self.players[userCh].money += gc.START_MONEY
        self.addTransaction(transaction.Transaction("S", "bank", self.players[userCh].name, gc.START_MONEY))

        return None

    # Egy tranzakciot hozzaad azokhoz a jatekosokhoz, akik szerepelnek benne
    def addTransaction(self, transaction) -> None:
        transaction_from = transaction.transaction_from
        transaction_to = transaction.transaction_to
        if transaction_from != "bank":
            for player in self.players:
                if player.name == transaction_from:
                    player.addTransaction(transaction)
        if transaction_to != "bank":
            for player in self.players:
                if player.name == transaction_to:
                    player.addTransaction(transaction)

        self.transactions.append(transaction)
        return None

    # Letrehoz egy tranzakciot majd meghivja vele az addTransaction fgv-t
    def createTransaction(self, tr_type, tr_from, tr_to, tr_money) -> None:
        self.addTransaction(transaction.Transaction(tr_type, tr_from, tr_to, tr_money))
        return None

    # Visszater egy formazott stringgel ami tartalmazza a jatekosok nevet es vagyonat
    def getPlayersInfo(self) -> str:
        strToRtn = ""
        for player in self.players:
            strToRtn += str(player.name) + " " + f"{int(player.money):_}" + "\n"
        return gc.spacesback(strToRtn)

    # Visszater egy listaval aminek minden tranzakcio adatai kulon-kulon tuplekent talalhatoak meg benne
    def getTransactionsList(self) -> list:
        transactionsList = []
        for transaction in self.transactions:
            transactionsList.append((transaction.transaction_type, transaction.transaction_from, transaction.transaction_to, transaction.transaction_money))
        return transactionsList

    # Kiprinteli a tranzakciokat
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
                #print(f"ISMERETLEN TRANZAKCIO ({transaction})")
                print(self.sm.UNKNOWN_TRANSACTION + '(' + str(transaction) + ')')
        #print(f"Osszesen [ {len(self.transactions)} ] tranzakcio")
        print(self.sm.ALL_TRANSACTION_PART1 + str(len(self.transactions)) + self.sm.ALL_TRANSACTION_PART2)
        return None

    # Ezt a fgv-t csak a jatek elejen kell meghivni
    # Minden tranzakciot hozzaad a benne resztvevo jatekosokhoz
    def playerTransactionsInit(self):
        for transaction in self.transactions:
            if transaction.transaction_from == "bank":
                pass
            else:
                for player in self.players:
                    if player.name == transaction.transaction_from:
                        player.addTransaction(transaction)
            if transaction.transaction_to == "bank":
                pass
            else:
                for player in self.players:
                    if player.name == transaction.transaction_to:
                        player.addTransaction(transaction)

    # Az ideiglenes menteshez szerzi be a save datat es modositja a mentes nevet egy alsovonal segitsegevel
    def getTmpSaveData(self) -> tuple:
        originalSaveData = self.getSaveData()
        alteredSaveData = (str(self.saveName + "_"), originalSaveData[1])
        return alteredSaveData

    # A mentesfajlbol beolvasott tranzakciok osszegenek kiszamolasa jatekosonkent es annak validalasa
    def validateBalance(self, players, transactions):
        for player in players:
            balance = 0
            for tr in transactions:
                if tr.transaction_to == player.name:
                    balance += int(tr.transaction_money)
                if tr.transaction_from == player.name:
                    balance -= int(tr.transaction_money)

            if player.money != balance:
                gc.cls()
                #print("A tranzakciok validalasa sikertelen!\nEzt valoszinuleg a mentesi fajl helytelen modositasa okozta.")
                #gc.wait()
                gc.wait(self.sm.FAILED_TRANSACTION_VALIDATION)
                sys.exit()

    # Ez a fgv osszehasonlitja a betoltendo fajl hashet a mentettel
    # amennyiben nem egyeznek, a program kilep (security measures)
    def validateFile(self, hash):
        selfhash = hashlib.sha512(str(self.getFinalSaveString() + gc.S).encode('utf-8')).hexdigest()
        if hash != selfhash:
            gc.cls()
            #print("A fajl validalasa sikertelen!\nEzt valoszinuleg a mentesi fajl helytelen modositasa okozta.")
            #gc.wait()
            gc.wait(self.sm.FAILED_FILE_VALIDATION)
            sys.exit()

    # Ez a fgv csupan tesztelesi celokat szolgal
    def addTonsOfTransactions(self, num):
        num = num * 100_000
        for _ in range(num):
            self.createTransaction('h', 'a', 'b', 1)


# Beker minden adatot ami elengedhetetlen egy savegame objektum letrehozasahoz majd letrehozza es visszater vele
def createNewSavegame(startingBudget, sm: settingsmanager.settingsManager) -> Savegame:
    sm = settingsmanager.settingsManager()
    gc.cls()
    print(gc.BANNER)

    #saveName = gc.removespaceSaveName(input("Mentes neve: "))
    #numberOfPlayers = int(input("Jatekosok szama: "))
    saveName = gc.removespaceSaveName(input(sm.NAME_OF_THE_SAVE))
    numberOfPlayers = int(input(sm.NUMBER_OF_PLAYERS))
    saveList = [numberOfPlayers]

    for i in range(numberOfPlayers):
        #saveList.append(player.Player(gc.removespace(input(f"{i+1}. jatekos neve: ")), startingBudget))
        saveList.append(player.Player(gc.removespace(input(f"{i+1}. {sm.NAME_OF_THE_PLAYER}")), startingBudget))

    for i in range(numberOfPlayers):
        saveList.append(transaction.Transaction("K", "bank", saveList[i+1].name, startingBudget))

    return Savegame(saveList, saveName, sm)
    