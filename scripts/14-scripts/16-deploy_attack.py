from scripts.helpful_scripts import get_account
from brownie import web3, interface


ETHERNAUT_INSTANCE = ""
GAS_LIMIT = 600000


def main():

    player = get_account()