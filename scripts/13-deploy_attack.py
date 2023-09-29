from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack13


ETHERNAUT_INSTANCE = "0x52D9172066F788070Ca1F74A26F3aD2902282c37"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.IGatekeeperOne(ETHERNAUT_INSTANCE)

    # check that we've won by confirming that 'entrant' = player
