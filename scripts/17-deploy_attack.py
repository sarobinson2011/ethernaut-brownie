from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack17


ETHERNAUT_INSTANCE = "0x0c5193d5b956f34248CfD55F3E5b9f4dcA77421F"
GAS_LIMIT = 600000


def main():

    player = get_account()
    attack = Attack17.deploy(ETHERNAUT_INSTANCE, {"from": player})


#  watch the youtube (non-python) solutions !!
