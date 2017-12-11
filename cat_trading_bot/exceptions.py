class KittyException(Exception):
    pass
    
class InsufficientFundsException(KittyException):
    pass

class KittyNotOwnedException(KittyException):
    pass

class KittyNotListedException(KittyException):
    pass
