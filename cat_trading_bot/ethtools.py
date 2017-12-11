from cat_trading_bot.exceptions import InsufficientFundsException
from cat_trading_bot.exceptions import KittyNotOwnedException
from cat_trading_bot.exceptions import KittyNotListedException
from ethereum import utils
from ethereum.transactions import Transaction
import os
import web3

CRYPTOKITTIES_CONTRACT_ADDR = 0xb1690C08E213a35Ed9bAb7B318DE14420FB57d8C


class EthWallet():
    def __init__(self, key=None):
        if not key:
            key = generate_key()
        self.key = key
        self.raw_addr = utils.privtoaddr(private_key)
        self.acct_addr = utils.checksum_encode(raw_address)
        
    def send_eth(self, address, amt):
        """Sends `amt` ethereum to `address`.
        
        If you do not have enough ethereum, raises 
        `InsufficientFundsException`.
        """
        pass
    
    def list_kitty(self, kitty_id, amt):
        """Lists the cat with id `kitty_id` for sale on the
        exchange for `amt`.
        
        If you do not own the cat with that id, raises
        `KittyNotOwnedException`.
        """
        pass
    
    def buy_kitty(self, kitty_id):
        """Tries to purchase the cat with id `kitty_id`.
        
        If you do not have enough ethereum, raises
        `InsufficientFundsException`.
        If the cat you are attempting to purchase is not on sale,
        raises `KittyNotListedException`.
        """
        pass


def generate_key():
    private_key = utils.sha3(os.urandom(4096))
    return private_key
