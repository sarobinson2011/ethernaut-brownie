from scripts.helpful_scripts import get_account
from brownie import web3, Attack09, convert, interface

ETHERNAUT_INSTANCE = "0x3a719C8FCe06303001d3afaa338Df4C948562fb9"
PRIZE = web3.toWei(0.01, "ether")


def main():

    player = get_account()

    attack_contract = Attack09.deploy(
        ETHERNAUT_INSTANCE, {"from": player, "value": PRIZE}
    )
    print(f"attack contract deployed at: {attack_contract}\n")
