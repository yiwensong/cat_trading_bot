from ethereum import utils
import os

def generate_key():
    private_key = utils.sha3(os.urandom(4096))
    return private_key
