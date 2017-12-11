from ethereum import utils
from ethereum.transactions import Transaction
import web3
import os


class EthWallet():
    def __init__(self, key=None):
        if not key:
            key = generate_key()
        self.key = key
        self.raw_addr = utils.privtoaddr(private_key)
        self.acct_addr = utils.checksum_encode(raw_address)


def generate_key():
    private_key = utils.sha3(os.urandom(4096))
    return private_key
