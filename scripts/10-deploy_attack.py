from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0xc734f6B53Ac3b11afdeE4cA1dbFee83521ED267d"


def main():

    player = get_account()

    attack_contract = Attack10.deploy({"from": player})
    print(f"attack contract deployed at: {attack_contract}")
