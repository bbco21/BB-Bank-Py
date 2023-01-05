from os import system

BANNER = '------------------------------------\nBB Bank\n'
PHASE = 'ALPHA'
VERSION = '1.0.0'

MESSAGE = BANNER + PHASE + VERSION + '\n'

MIN_PLAYERS = 2
MIN_MONEY = 0
START_MONEY = 2000000

def cls():
    system("cls")

def wait():
    input("\nNyomj ENTER-t a folytatashoz...")

def removespace(stringToModify: str) -> str:
    stringToModify = stringToModify.replace(" ", "<*?*>")
    return stringToModify

def spacesback(stringToModify: str) -> str:
    stringToModify = stringToModify.replace("<*?*>", " ")
    return stringToModify