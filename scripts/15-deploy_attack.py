from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack15


ETHERNAUT_INSTANCE = "0x23c8BcEB66E6798E35FE89Dc7fa331ED731B9bFe"
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    attack = Attack15.deploy(ETHERNAUT_INSTANCE, {"from": player})
