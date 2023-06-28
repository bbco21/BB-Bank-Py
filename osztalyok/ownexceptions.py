

class UnsupportedOsError(Exception):
    def __init__(self, osType: object) -> None:
        self.errorMsg = "Unsupported os"
        if osType != None:
            self.errorMsg += f": {osType}"
        super().__init__(self.errorMsg)