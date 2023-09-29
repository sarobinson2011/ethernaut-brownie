from scripts.helpful_scripts import get_account
from brownie import web3, interface


ETHERNAUT_INSTANCE = "0xbf0cdE8daAdF37782fC6c250097a53900BfEEcaD"
GAS_LIMIT = 6000000


def main():

    player = get_account()
