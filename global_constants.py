from os import system
import sys

BANNER = '------------------------------------\nBB Bank\n'
PHASE = 'ALPHA'
VERSION = '1.0.0'

MESSAGE = BANNER + PHASE + VERSION + '\n'

MIN_PLAYERS = 2
MIN_MONEY = 0
START_MONEY = 2000000

def cls():
    if sys.platform == "win32":
        system("cls")
    elif sys.platform == "linux":
        system("clear")
    else:
        print("Console clear is not implemented yet on this platform.")
        print("Please contact the developer on the following e-mail and describe the problem and the system you are using.")
        print("levente@bbco.hu")

def wait():
    input("\nNyomj ENTER-t a folytatashoz...")

def removespace(stringToModify: str) -> str:
    stringToModify = stringToModify.replace(" ", "<*?*>")
    return stringToModify

def spacesback(stringToModify: str) -> str:
    stringToModify = stringToModify.replace("<*?*>", " ")
    return stringToModify