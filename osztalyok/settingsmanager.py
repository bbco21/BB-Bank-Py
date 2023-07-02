""" Settings manager for BB-Bank

This scripts task is to check the saving locations integrity and managing the settings.
It creates, reads and modifies the settings file and the localization files aswell.
If its running in __main__ mode then a modifier menu appears where you can manage
the settings. Otherwise, this same dialogue can be called anywhere from the running code.
(I'm thinking about adding -s flag to init. If supplied call the settings menu.)

The basic language for this manager is English.
I don't even plan to implement more language to it, because it might confuse some people
when they try to change the language and somehow the manager is in a different language.


DONE                                            DONE                                            DONE
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!                                            TODO                                            !!!!
!!!!    Some of the variables and settings are need to be moved over here for more control.     !!!!
!!!!    Their old location is in the global_constants. Please pay attention.                    !!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    DONT MOVE THEM JUST MAKE THEIR VALUES DETERMINED FROM HERE
DONE                                            DONE                                            DONE


Features
--------------------------------
validateFileIntegrity
    It validates the integritiy of the files located in the SAVELOCATION directory

changeLanguage
    It changes the language. It reads the languages from the "lang" folder inside SAVELOCATION
    * You can make your own translation to the program by copying an already existing language file
    (with .lang extension) and replacing the old text with the new one in any text editor.
    When you save the new file give the new language as a name. e.g. "hungarian.lang".
    It's important because when the manager lists the available language names, it reads the name
    of the files.
    * If the manager can't load the language file, it raises an InvalidLanguageFile exception.
"""

import global_constants as gc
import json, os

class settingsManager():
    def __init__(self) -> None:
        self.validateFileStructure()
        self.initVariables()
        self.readSettings()
        self.readLangFile(self.settings["language"] + ".lang")
        gc.PRESS_ENTER = self.PRESS_ENTER
        gc.MIN_PLAYERS = self.settings["min_players"]
        gc.MIN_MONEY = self.settings["min_money"]
        gc.START_MONEY = self.settings["start_money"]
        

    def initVariables(self):
        # Elso blokk
        # Init.py-n belul a help resznel a print meassagek
        self.SAVELOC_TXT = ""
        self.HELP_HEADER = ""
        self.HELP_UNSAFE = ""
        self.HELP_HELP = ""
        self.HELP_SETTINGS = ""

        # Masodik blokk (szinten init.py)
        self.FIRSTRUN = ""
        self.SELECT_SAVE = ""
        self.NEW_SAVE = ""
        self.UNSAFE_WARN_MSG = ""
        self.MISSING_HASH_WARN = ""

        # Harmadik blokk (main.py)
        self.START_INIT = ""
        self.TRANSFER_MONEY = ""
        self.ADD_MONEY = ""
        self.REMOVE_MONEY = ""
        self.START_TILE = ""
        self.SHOW_TRANSACTIONS = ""
        self.SHOW_ALL_TRANSACTIONS = ""
        self.SETTINGS_MENU = ""
        self.EXIT = ""
        self.EXIT_AND_SAVE = ""
        self.EXIT_WITHOUT_SAVE = ""
        self.INVALID_PLAYER_ID = ""

        # Negyedik blokk (savegame.py)
        self.TRANSFERING_PLAYER = ""
        self.RECEIVING_PLAYER = ""
        self.ZERO_OR_LESS_TRANS_ERROR = ""
        self.ZERO_OR_LESS_TRANS_ERROR_ALT = ""
        self.NOT_ENOUGH_FUNDS = ""
        self.MONEY_IN = ""
        self.MONEY_IN_SYNTAX_ERROR = ""
        self.MONEY_GIVING = ""
        self.MONEY_REMOVING = ""
        self.UNKNOWN_TRANSACTION = ""
        self.ALL_TRANSACTION_PART1 = ""
        self.ALL_TRANSACTION_PART2 = ""
        self.FAILED_TRANSACTION_VALIDATION = ""
        self.FAILED_FILE_VALIDATION = ""
        self.NAME_OF_THE_SAVE = ""
        self.NUMBER_OF_PLAYERS = ""
        self.NAME_OF_THE_PLAYER = ""

        # Otodik blokk (global_constants.py)
        self.PRESS_ENTER = ""

        # GENERAL BLOKK
        self.OPTION = ""
        self.INVALID_OPTION = ""

    def readLangFile(self, fileName: str):
        # Don't forget to change that if new variables added
        desiredLen = 42
        lines = []
        langData = {}
        with open(gc.LANGUAGEFOLDER + '/' + fileName, 'r') as f:
            for line in f:
                lineTmp = line
                if lineTmp.strip() != "":
                    lines.append(line)
                else:
                    pass
        if len(lines) == desiredLen:
            for line in lines:
                tmp = str(line)
                tmp = tmp.split(" = ")
                tmp[0] = tmp[0].strip()
                tmp[1] = tmp[1].strip()
                tmp[1] = tmp[1].replace('"', '')
                tmp[1] = tmp[1].replace("\\n", "\n")
                langData[tmp[0]] = tmp[1]
        else:
            raise self.InvalidLanguageFile(f"desired number of lines: {desiredLen}\nreal number of lines: {len(lines)}")
        try:
            self.SAVELOC_TXT = langData["SAVELOC_TXT"]
            self.HELP_HEADER = langData["HELP_HEADER"]
            self.HELP_UNSAFE = langData["HELP_UNSAFE"]
            self.HELP_HELP   = langData["HELP_HELP"]
            self.HELP_SETTINGS = langData["HELP_SETTINGS"]
            self.OPTION = langData["OPTION"]
            self.INVALID_OPTION = langData["INVALID_OPTION"]
            self.FIRSTRUN = langData["FIRSTRUN"]
            self.SELECT_SAVE = langData["SELECT_SAVE"]
            self.NEW_SAVE = langData["NEW_SAVE"]
            self.UNSAFE_WARN_MSG = langData["UNSAFE_WARN_MSG"]
            self.MISSING_HASH_WARN = langData["MISSING_HASH_WARN"]
            self.START_INIT = langData["START_INIT"]
            self.TRANSFER_MONEY = langData["TRANSFER_MONEY"]
            self.ADD_MONEY = langData["ADD_MONEY"]
            self.REMOVE_MONEY = langData["REMOVE_MONEY"]
            self.START_TILE = langData["START_TILE"]
            self.SHOW_TRANSACTIONS = langData["SHOW_TRANSACTIONS"]
            self.SETTINGS_MENU = langData["SETTINGS_MENU"]
            self.EXIT = langData["EXIT"]
            self.EXIT_AND_SAVE = langData["EXIT_AND_SAVE"]
            self.EXIT_WITHOUT_SAVE = langData["EXIT_WITHOUT_SAVE"]
            self.SHOW_ALL_TRANSACTIONS = langData["SHOW_ALL_TRANSACTIONS"]
            self.INVALID_PLAYER_ID = langData["INVALID_PLAYER_ID"]
            self.TRANSFERING_PLAYER = langData["TRANSFERING_PLAYER"]
            self.RECEIVING_PLAYER = langData["RECEIVING_PLAYER"]
            self.ZERO_OR_LESS_TRANS_ERROR = langData["ZERO_OR_LESS_TRANS_ERROR"]
            self.ZERO_OR_LESS_TRANS_ERROR_ALT = langData["ZERO_OR_LESS_TRANS_ERROR_ALT"]
            self.NOT_ENOUGH_FUNDS = langData["NOT_ENOUGH_FUNDS"]
            self.MONEY_IN = langData["MONEY_IN"]
            self.MONEY_IN_SYNTAX_ERROR = langData["MONEY_IN_SYNTAX_ERROR"]
            self.MONEY_GIVING = langData["MONEY_GIVING"]
            self.MONEY_REMOVING = langData["MONEY_REMOVING"]
            self.UNKNOWN_TRANSACTION = langData["UNKNOWN_TRANSACTION"]
            self.ALL_TRANSACTION_PART1 = langData["ALL_TRANSACTION_PART1"]
            self.ALL_TRANSACTION_PART2 = langData["ALL_TRANSACTION_PART2"]
            self.FAILED_TRANSACTION_VALIDATION = langData["FAILED_TRANSACTION_VALIDATION"]
            self.FAILED_FILE_VALIDATION = langData["FAILED_FILE_VALIDATION"]
            self.NAME_OF_THE_SAVE = langData["NAME_OF_THE_SAVE"]
            self.NUMBER_OF_PLAYERS = langData["NUMBER_OF_PLAYERS"]
            self.NAME_OF_THE_PLAYER = langData["NAME_OF_THE_PLAYER"]
            self.PRESS_ENTER = langData["PRESS_ENTER"]
        except:
            raise self.InvalidLanguageFile()

    def readSettings(self):
        self.settings = {}
        with open(gc.SETTINGSFILE, 'r') as f:
            file = f.read()
            self.settings = json.loads(file)

    def validateFileStructure(self):
        if os.path.isfile(gc.SETTINGSFILE): pass
        else:
            with open(gc.SETTINGSFILE, 'w') as f:
                f.write(gc.SETTINGS_FILE_CONTENT)
        
        if not os.path.isdir(gc.LANGUAGEFOLDER):
            os.mkdir(gc.LANGUAGEFOLDER)

        if not os.path.exists(gc.ANCHOR_FILE):
            try:
                os.makedirs(gc.SAVEGAMESFOLDER)
            except: pass
            try:
                with open(gc.ANCHOR_FILE, 'w') as f:
                    pass
            except: pass
            try:
                with open(gc.SAVELOCATION+"/kezdotokek.levdb", 'w') as f:
                    f.write(gc.STARTING_BUDGET_FILE_CONTENT)
            except: pass
            try:
                with open(gc.SAVEGAMESFOLDER+"/hashes.levdb", 'w') as f:
                    pass
            except: pass
        
        if not os.path.isfile(gc.LANGUAGEFOLDER + "/Magyar.lang"):
            with open(gc.LANGUAGEFOLDER + "/Magyar.lang", 'w') as f:
                f.write(gc.HUNGARIAN_LANG_CONTENT)
        if not os.path.isfile(gc.LANGUAGEFOLDER + "/English.lang"):
            with open(gc.LANGUAGEFOLDER + "/English.lang", 'w') as f:
                f.write(gc.ENGLISH_LANG_CONTENT)


    # TODO Make settings menu
        # Change language and other settings

    
    def getLanguageFiles(self):
        self.availableLanguages = []
        tmpList = os.listdir(gc.LANGUAGEFOLDER)
        for language in tmpList:
            self.availableLanguages.append(language.removesuffix(".lang"))

    def setLanguage(self):
        self.getLanguageFiles()
        gc.cls()
        for i in range(len(self.availableLanguages)):
            print(f"{i+1} - {self.availableLanguages[i]}")
        userCh = int(input("Choice: ")) - 1
        if userCh in range(len(self.availableLanguages)):
            self.readLangFile(self.availableLanguages[userCh] + ".lang")
            self.settings["language"] = self.availableLanguages[userCh]
            self.saveSettings()
        else:
            input("Invalid option.\nPress ENTER to continue...")

    def saveSettings(self):
        with open(gc.SETTINGSFILE, 'w') as f:
            f.write(json.dumps(self.settings, indent=4))

    def menu(self):
        gc.cls()
        print("1 - change language")
        print("0 - go back")
        userCh = input("Option: ")
        if userCh == '0':
            return
        elif userCh == '1':
            self.setLanguage()
        else:
            input("Invalid option.\nPress ENTER and choose again.")
            self.menu()
        return
        
    class InvalidLanguageFile(Exception):
        def __init__(self, errorText) -> None:
            if errorText:
                super().__init__(f"Invalid Language File:\n{errorText}")
            else:
                super().__init__("Invalid Language File")


