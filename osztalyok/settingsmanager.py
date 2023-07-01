""" Settings manager for BB-Bank

This scripts task is to check the saving locations integrity and managing the settings.
It creates, reads and modifies the settings file and the localization files aswell.
If its running in __main__ mode then a modifier menu appears where you can manage
the settings. Otherwise, this same dialogue can be called anywhere from the running code.
(I'm thinking about adding -s flag to init. If supplied call the settings menu.)

The basic language for this manager is English.
I don't even plan to implement more language to it, because it might confuse some people
when they try to change the language and somehow the manager is in a different language.


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!                                            TODO                                            !!!!
!!!!    Some of the variables and settings are need to be moved over here for more control.     !!!!
!!!!    Their old location is in the global_constants. Please pay attention.                    !!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


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
    * If the manager can't load the language file, it falls back to English.
"""