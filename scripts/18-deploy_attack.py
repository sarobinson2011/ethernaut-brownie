from scripts.helpful_scripts import get_account
from brownie import web3, interface


ETHERNAUT_INSTANCE = "0xe2801F3489fE0aBBd9A2552085e23CF9Ed85d966"
GAS_LIMIT = 6000000


def main():

    player = get_account()
