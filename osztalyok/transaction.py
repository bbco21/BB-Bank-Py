

# Letrehozza a tranzakcio osztalyt
# Egy tranzakcio objektum tartalmaz minden informaciot a tranzakciorol
class Transaction:
    def __init__(self, transaction_type, transaction_from, transaction_to, money, player_budget) -> None:
        self.transaction_type = transaction_type
        self.transaction_from = transaction_from
        self.transaction_to = transaction_to
        self.transaction_money = money
        self.player_budget = player_budget

        
    # Visszakuld egy mentesi stringet az objektumrol
    def getSaveString(self) -> str:
        # TODO a self.player_budget a jatekos akkori penzet tartalmazza
        #      mivel hozzaadtam ezt, ezert ezt at kene gondolnom, hogy miket baszhat el
        return str(self.transaction_type+'||'+self.transaction_from+'||'+self.transaction_to+'||'+str(self.transaction_money)+'||'+str(self.player_budget))
        