import global_constants as gc

class Player():
    def __init__(self, name, startingBudget) -> None:
        self.name = name
        self.money = int(startingBudget)
        self.transactions = []
    

    def addTransaction(self, transaction) -> None:
        self.transactions.append(transaction)
        

    def getPrintableStr(self) -> str:
        strToReturn = ""
        for tr in self.transactions:
            if tr.transaction_type == "u":
                strToReturn += f"{tr.transaction_from} -> {tr.transaction_to} {int(tr.transaction_money):_}\n"
            elif tr.transaction_type == "e":
                strToReturn += f"{tr.transaction_from} -> - {int(tr.transaction_money):_}\n"
            elif tr.transaction_type == "h" or tr.transaction_type == "K" or tr.transaction_type == "S":
                strToReturn += f"{tr.transaction_to} <- + {int(tr.transaction_money):_}\n"
        return gc.spacesback(strToReturn)


    
    def printTransactions(self) -> None:
        gc.cls()
        print(gc.MESSAGE)
        print(self.getPrintableStr())
        return None
