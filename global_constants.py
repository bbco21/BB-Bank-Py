from os import system
import os
import osztalyok.ownexceptions as oe
import sys

BANNER = '------------------------------------\nBB Bank\n'
PHASE = 'BETA'
VERSION = '1.0.0'

MESSAGE = BANNER + PHASE + " " + VERSION + '\n'

MIN_PLAYERS = 2
MIN_MONEY = 0
START_MONEY = 2000000


# Save location
SAVELOCATION = ""
SAVEGAMESFOLDER = ""
SETTINGSFILE = ""
if sys.platform == "win32":
    saveloc = os.getenv("APPDATA").replace("\\", "/")
    bbcoSaveLoc = saveloc + "/BBCO"
    bbbankSaveLoc = bbcoSaveLoc + "/BB-Bank"
    if not os.path.exists(bbcoSaveLoc):
        os.mkdir(bbcoSaveLoc)
    if not os.path.exists(bbbankSaveLoc):
        os.mkdir(bbbankSaveLoc)
    SAVELOCATION = bbbankSaveLoc
    SAVEGAMESFOLDER = SAVELOCATION + "/saves"
    LANGUAGEFOLDER = SAVELOCATION + "/lang"
    SETTINGSFILE = SAVELOCATION + "/settings.json"
elif sys.platform == "linux":
    homeDir = os.path.expanduser('~')
    bbcoSaveLoc = homeDir + "/.bbco"
    bbbankSaveLoc = bbcoSaveLoc + "/bb-bank"
    if not os.path.exists(bbcoSaveLoc):
        os.makedirs(bbcoSaveLoc)
    if not os.path.exists(bbbankSaveLoc):
        os.makedirs(bbbankSaveLoc)
    SAVELOCATION = bbbankSaveLoc
    SAVEGAMESFOLDER = SAVELOCATION + "/saves"
    LANGUAGEFOLDER = SAVELOCATION + "/lang"
    SETTINGSFILE = SAVELOCATION + "/settings.json"
else:
    print("This program is not implemented on this platform. You might encounter some bugs.")
    print("Please contact the developer on the following e-mail and describe the problem and the system you are using.")
    print("levente@bbco.hu")
    try:
        homeDir = os.path.expanduser('~')
        bbcoSaveLoc = homeDir + "/.bbco"
        bbbankSaveLoc = bbcoSaveLoc + "/bb-bank"
        if not os.path.exists(bbcoSaveLoc):
            os.mkdir(bbcoSaveLoc)
        if not os.path.exists(bbbankSaveLoc):
            os.mkdir(bbbankSaveLoc)
        SAVELOCATION = bbbankSaveLoc
        SAVEGAMESFOLDER = SAVELOCATION + "/saves"
        LANGUAGEFOLDER = SAVELOCATION + "/lang"
        SETTINGSFILE = SAVELOCATION + "/settings.json"
    except:
        raise oe.UnsupportedOsError(sys.platform)
    
ANCHOR_FILE = SAVELOCATION + "/hadrun.anchor"

ARGV = None

S = '420'


STARTING_BUDGET_FILE_CONTENT = "Bankkartyas||15000000\nTeszt||69420"
SETTINGS_FILE_CONTENT = '{\n    "language": "English",\n    "min_players": 2,\n    "min_money": 0,\n    "start_money": 2000000\n}'



def cls():
    if sys.platform == "win32":
        system("cls")
    elif sys.platform == "linux":
        system("clear")
    else:
        print("Console clear is not implemented yet on this platform.")
        print("Please contact the developer on the following e-mail and describe the problem and the system you are using.")
        print("levente@bbco.hu")
        try:
            system("clear")
        except:
            pass

PRESS_ENTER = ""
def wait(text: str = None):
    if text == None:
        #input("\nNyomj ENTER-t a folytatashoz...")
        input(PRESS_ENTER)
    else:
        #input(f"\n{text}\nNyomj ENTER-t a folytatashoz...")
        input(f"\n{text}{PRESS_ENTER}")

def removespace(stringToModify: str) -> str:
    stringToModify = stringToModify.replace(" ", "<*?*>")
    return stringToModify

def spacesback(stringToModify: str) -> str:
    stringToModify = stringToModify.replace("<*?*>", " ")
    return stringToModify

def removespaceSaveName(stringToModify: str) -> str:
    stringToModify = stringToModify.replace(" ", "___")
    return stringToModify

def spacesbackSaveName(stringToModify: str) -> str:
    stringToModify = stringToModify.replace("___", " ")
    return stringToModify


HUNGARIAN_LANG_CONTENT = r'''

SAVELOC_TXT = "A program mentesi helye: "
HELP_HEADER = "ROVID HOSSZU      LEIRAS"
HELP_UNSAFE = " -u   --unsafe    Minden biztonsagi ellenorzest kikapcsol"
HELP_HELP = " -h   --help      Kiirja ezt az uzenetet"
HELP_SETTINGS = " -s   --settings  Beallitasok megnyitasa es szerkesztese"

OPTION = "Valasz: "
INVALID_OPTION = "NINCS ILYEN OPCIO!\nNyomd meg az ENTER-t a folytatashoz..."

FIRSTRUN = "Elso futtatas.\nFajlstruktura letrehozasa."
SELECT_SAVE = "Valassz mentest:"
NEW_SAVE = "0 - Uj mentes letrehozasa"
UNSAFE_WARN_MSG = "FIGYELEM\nNem biztonsagos modban fut a program.\nA tranzakciok nem lesznek ellenorizve."
MISSING_HASH_WARN = "A mentesnek nincs hash-e!\nLehetseges, hogy a mentest modositottak."

START_INIT = "Kerlek az init.py-t futtasd!\nA program most megprobalja elinditani az init.py-t\nNem biztos, hogy a program igy megfeleloen fog mukodni\nHiba eseten futtasa manualisan az init.py-t"
TRANSFER_MONEY = "Utalas ket jatekos kozott"
ADD_MONEY = "Penz hozzaadasa jatekoshoz"
REMOVE_MONEY = "Penz elvetele jatekostol"
START_TILE = "START mezo"
SHOW_TRANSACTIONS = "Tranzakciok megtekintese"
SETTINGS_MENU = "Beallitasok"
EXIT = "Kilepes"
EXIT_AND_SAVE = "Mentes es kilepes"
EXIT_WITHOUT_SAVE = "Kilepes mentes nelkul"
SHOW_ALL_TRANSACTIONS = "Osszes tranzakcio megjelenitese"
INVALID_PLAYER_ID = "NINCS ILYEN SORSZAMU JATEKOS!"

TRANSFERING_PLAYER = "Utalo jatekos:"
RECEIVING_PLAYER = "Fogado jatekos:"
ZERO_OR_LESS_TRANS_ERROR = "0 osszegu vagy kisebb tranzakcio nem valosithato meg!"
ZERO_OR_LESS_TRANS_ERROR_ALT = "0 vagy negativ erteku tranzakcio nem valosithato meg!"
NOT_ENOUGH_FUNDS = "NEM ALL RENDELKEZESRE ELEGENDO EGYENLEG!"
MONEY_IN = "Osszeg: "
MONEY_IN_SYNTAX_ERROR = "Hibas a bemenet szintaxisa. Tranzakcio vegrehajtasa 0 osszeggel."
MONEY_GIVING = "Penz hozzaadasa:"
MONEY_REMOVING = "Penz elvetele:"
UNKNOWN_TRANSACTION = "ISMERETLEN TRANZAKCIO "
ALL_TRANSACTION_PART1 = "Osszesen [ "
ALL_TRANSACTION_PART2 = " ] tranzakcio"
FAILED_TRANSACTION_VALIDATION = "A tranzakciok validalasa sikertelen!\nEzt valoszinuleg a mentesi fajl helytelen modositasa okozta."
FAILED_FILE_VALIDATION = "A fajl validalasa sikertelen!\nEzt valoszinuleg a mentesi fajl helytelen modositasa okozta."
NAME_OF_THE_SAVE = "Mentes neve: "
NUMBER_OF_PLAYERS = "Jatekosok szama: "
NAME_OF_THE_PLAYER = "jatekos neve: "

PRESS_ENTER = "\nNyomj ENTER-t a folytatashoz"'''

ENGLISH_LANG_CONTENT = r'''

SAVELOC_TXT = "The programs save location: "
HELP_HEADER = "SHORT LONG        LEIRAS"
HELP_UNSAFE = " -u   --unsafe    Turns off every security measures"
HELP_HELP = " -h   --help      Prints this messega"
HELP_SETTINGS = " -s   --settings  Open settings and modify them"

OPTION = "Option: "
INVALID_OPTION = "INVALID OPTION!\nPress ENTER to continue..."

FIRSTRUN = "First run.\nCreating file structure..."
SELECT_SAVE = "Choose save:"
NEW_SAVE = "0 - Create new save"
UNSAFE_WARN_MSG = "WARNING\nProgram runs in unsafe mode\nTransactions won't be validated."
MISSING_HASH_WARN = "This save doesn't have a hash.\nThe save might be modified by someone."

START_INIT = "Please run the init.py\nThe program tries to run init.py\nThere might be some problems if you run the program like this\nIn case of malfunction please manually run init.py"
TRANSFER_MONEY = "Transfer money between players"
ADD_MONEY = "Add money to player"
REMOVE_MONEY = "Remove money from player"
START_TILE = "START tile"
SHOW_TRANSACTIONS = "Show transactions"
SETTINGS_MENU = "Options"
EXIT = "Exit"
EXIT_AND_SAVE = "Save and exit"
EXIT_WITHOUT_SAVE = "Exit without saving"
SHOW_ALL_TRANSACTIONS = "Show all transaction"
INVALID_PLAYER_ID = "NO PLAYER WITH THIS ID!"

TRANSFERING_PLAYER = "Transfering player:"
RECEIVING_PLAYER = "Receiving player:"
ZERO_OR_LESS_TRANS_ERROR = "Transaction with 0 or less amount of money is not executable!"
ZERO_OR_LESS_TRANS_ERROR_ALT = "Transaction with 0 or negative amount of money is not executable!"
NOT_ENOUGH_FUNDS = "NOT ENOUGH FUNDS FOR THIS TRANSACTION!"
MONEY_IN = "Amount: "
MONEY_IN_SYNTAX_ERROR = "Syntax error. Executing transaction with 0 money."
MONEY_GIVING = "Add money:"
MONEY_REMOVING = "Remove money:"
UNKNOWN_TRANSACTION = "UNKNOWN TRANSACTION "
ALL_TRANSACTION_PART1 = "Overall [ "
ALL_TRANSACTION_PART2 = " ] transaction(s)"
FAILED_TRANSACTION_VALIDATION = "Validation of the transactions failed!\nThis is likely caused by modifying the save file."
FAILED_FILE_VALIDATION = "Validation of the save file failed!\nThis is likely caused by modifying the save file."
NAME_OF_THE_SAVE = "Save name: "
NUMBER_OF_PLAYERS = "Player count: "
NAME_OF_THE_PLAYER = "player name: "

PRESS_ENTER = "\nPress ENTER to continue..."'''