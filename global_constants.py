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
if sys.platform == "win32":
    saveloc = os.getenv("APPDATA").replace("\\", "/")
    bbcoSaveLoc = saveloc + "/BBCO"
    bbbankSaveLoc = bbcoSaveLoc + "/BB-Bank"
    if not os.path.exists(bbcoSaveLoc):
        os.mkdir(bbcoSaveLoc)
    if not os.path.exists(bbbankSaveLoc):
        os.mkdir(bbbankSaveLoc)
    SAVELOCATION = bbbankSaveLoc
    SAVEGAMESFOLDER = SAVELOCATION + """/saves"""
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
        SAVEGAMESFOLDER = SAVELOCATION + "/saves/"
    except:
        raise oe.UnsupportedOsError(sys.platform)
    
ANCHOR_FILE = SAVELOCATION + "/hadrun.anchor"

ARGV = None

S = '420'


STARTING_BUDGET_FILE_CONTENT = "Bankkartyas||15000000\nTeszt||69420"



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

def wait(text: str = None):
    if text == None:
        input("\nNyomj ENTER-t a folytatashoz...")
    else:
        input(f"\n{text}\nNyomj ENTER-t a folytatashoz...")

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
